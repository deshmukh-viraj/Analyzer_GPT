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

st.title("Analyzer gpt - Digital Data Analyzer")

uploaded_file = st.file_uploader('Upload your CSV file', type='csv')
task = st.text_input(
    "Enter your task",
    value=f"Can you give me the number of columns in my data ({uploaded_file.name if uploaded_file else 'yourfile.csv'})"
)


async def run_analyzer(docker, model_client, task):

    try:
        await start_docker_container(docker)
        team = getDataAnalyzerTeam(docker, model_client)
        
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print(msg := f"{message.source} : {message.content}")
                #yield msg
                if msg.startswith('user'):
                    with st.chat_message('user',avatar='🦸‍♂️'):
                        st.markdown(msg)
                elif msg.startswith('Data_Analyzer_Agent'):
                    with st.chat_message('Data Analyst', avatar='👽'):
                        st.markdown(msg)
                elif msg.startswith('CodeExecutor'):
                    with st.chat_message('Code Executor', avatar='🦹‍♂️'):
                        st.markdown(msg)
                
            elif isinstance(message,TaskResult):
                print(msg:= "Stop Reason: {message.stop_reason}")
                #yield msg
                st.markdown(msg)
        return None
    except Exception as e:
        print(e)
        return e
    finally:
        await stop_docker_container(docker)

if st.button("Run Analysis"):
    if uploaded_file is not None and task:
        filename = uploaded_file.name
        save_path = os.path.join('temp', filename)

        if not os.path.exists('temp'):
            os.makedirs('temp')
        with open(save_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())


    model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    error = asyncio.run(run_analyzer(docker, model_client, task))
    if error:
        st.error(f"An error occurred: {error}")
    if os.path.exists('temp/output.png'):
        st.image('temp/output.png', caption='Analysis File')

else:
    st.warning("Please upload the CSV file")

