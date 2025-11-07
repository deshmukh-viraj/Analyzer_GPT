import asyncio
from team.analyzer import getDataAnalyzerTeam
from agents.data_analyzer import GetDataAnalyzerAgent
from agents.code_executor import GetCodeExecutorAgent
from config.model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def main():
    model_client = get_model_client()
    docker = getDockerCommandLineExecutor()
    
    team = getDataAnalyzerTeam(docker, model_client)

    try:
        task = "Can you give the graph of died and survived passenger in my titanic.csv data and save output as output.png"

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            print('=' * 70)
            if isinstance(message, TextMessage):
                print(message.source, ":" ,message.content)
            elif isinstance(message, TaskResult):
                print("Stop Reason:", message.stop_reason)
            
    
    except Exception as e:
        print(e)
    finally:
         await stop_docker_container(docker)



if __name__ == "__main__":
    asyncio.run(main())
