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

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            print('=' * 70)
            print(message)
    
    except Exception as e:
        print(e)
    finally:
         await stop_docker_container(docker)



    if __name__ == "__main__":
        asyncio.run(main())