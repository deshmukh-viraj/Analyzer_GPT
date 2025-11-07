import streamlit as st
import asyncio
import os
from config.model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container
from agents.data_analyzer import GetDataAnalyzerAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult



st.title("Analyzer gpt - Digital Data Analyzer")

uploaded_file = st.file_uploader('Upload your CSV file', type='csv')
task = st.text_input("Enter your task", value="Can you give a me number of columns in my data (file is data.csv)")


async def run_analyzer(docker, model_client, task):

    try:
        await start_docker_container(docker)
        team = GetDataAnalyzerAgent(model_client)
        
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print(msg := f"{message.source} : {message.content}")
                #yield msg
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
        
        if not os.path.exists('temp'):
            os.makedirs('temp')
        with open('temp/data.csv', 'wb') as f:
            f.write(uploaded_file.getbuffer())


    model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    error = asyncio.run(run_analyzer(docker, model_client, task))
    if error:
        st.error(f"An error occurred: {error}")

else:
    st.warning("Please upload the CSV file")

