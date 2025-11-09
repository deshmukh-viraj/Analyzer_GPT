import streamlit as st
import asyncio
import os
from config.model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container
from agents.data_analyzer import GetDataAnalyzerAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from autogen_agentchat.agents import CodeExecutorAgent
from team.analyzer import getDataAnalyzerTeam
import subprocess


st.title("Analyzer gpt - Digital Data Analyzer")

uploaded_file = st.file_uploader('Upload your CSV file', type=['csv'])

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None
# task = st.text_input(
#     "Enter your task",
#     value=f"Can you give me the number of columns in my data ({uploaded_file.name if uploaded_file else 'yourfile.csv'})"
# )
task = st.chat_input("Enter Your Task:  ")

async def run_analyzer(docker, model_client, task, uploaded_path):

    try:
        await start_docker_container(docker)

        try:
            container_id = subprocess.check_output(
                "docker ps -q --latest", shell=True, text=True
            ).strip()
            print(f"Detected running container: {container_id}")
        except subprocess.CalledProcessError:
            container_id = None

        if not container_id:
            st.error("Failed to detect a running Docker container.")
            return

        file_name = os.path.basename(uploaded_path)
        container_path = f"/workspace/{file_name}"
        copy_cmd = f"docker cp {uploaded_path} {container_id}:{container_path}"
        subprocess.run(copy_cmd, shell=True, check=True)
        print(f"File copied to container: {container_path}")

        team = getDataAnalyzerTeam(docker, model_client)

        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)
        
        final_task = f"""
            You have been provided a CSV dataset that has already been uploaded for you.
            The exact file path is '{container_path}' inside your working directory.
            Whenever you write code to read the CSV, always use:
                df = pd.read_csv('{container_path}')
            Do NOT use 'your_file.csv' or any placeholder filename.

            Now, perform this task: {task}
            """

        async for message in team.run_stream(task=final_task):
            if isinstance(message,TextMessage):
                print(msg := f"{message.source} : {message.content}")
                #yield msg
                
                if msg.startswith('user'):
                   
                    with st.chat_message('user',avatar='🦸‍♂️'):
                        st.markdown(f"user : {task}")
                elif msg.startswith('Data_Analyzer_Agent'):
                    with st.chat_message('Data Analyst', avatar='👽'):
                        st.markdown(msg)
                elif msg.startswith('CodeExecutor'):
                    with st.chat_message('Code Executor', avatar='🦹‍♂️'):
                        st.markdown(msg)
                
                # Store the actual message content for session state
                if msg.startswith('user'):
                    st.session_state.messages.append(f"user : {task}")
                else:
                    st.session_state.messages.append(msg)
                
            elif isinstance(message,TaskResult):
               
                print(msg := f"Stop Reason: {message.stop_reason}")
                #yield msg
                st.markdown(msg)
                st.session_state.messages.append(msg)
        
        st.session_state.autogen_team_state = await team.save_state()
        
        st.rerun()
        
    except Exception as e:
        print(e)
        return e
    finally:
        await stop_docker_container(docker)

if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)
    


if task:
    if uploaded_file is not None:
        os.makedirs('temp', exist_ok=True)
        save_path = os.path.join('temp', uploaded_file.name)
        with open(save_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        model_client =get_model_client()
        docker = getDockerCommandLineExecutor()
        
       
        asyncio.run(run_analyzer(docker, model_client, task, save_path))
    
        if os.path.exists('temp/output.png'):
            st.image('temp/output.png', caption='Analysis File')

    else:
        st.warning("Please upload the CSV file before entering a task")
        
else:
    st.info("Waiting for your task...")