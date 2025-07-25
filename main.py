import asyncio
from team.analyzer import getDataAnalyzerTeam
from agents.data_analyzer import GetDataAnalyzerAgent
from agents.code_executor import GetCodeExecutorAgent
from config.model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container


async def main():
    model_client = get_model_client()
    docker = getDockerCommandLineExecutor

    team = getDataAnalyzerTeam(docker, model_client)

    try:
        task = "Can you tell me how many rows and columns in directory"