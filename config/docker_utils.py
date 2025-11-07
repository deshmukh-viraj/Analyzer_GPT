from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORK_DIR_DOCKER, TIMEOUT_DOCKER
import os 

def getDockerCommandLineExecutor():
    temp_dir = os.path.abspath('temp')    
    docker = DockerCommandLineCodeExecutor(
        work_dir = temp_dir,
        timeout = TIMEOUT_DOCKER,
        bind_dir=temp_dir
    )
    return docker


async def start_docker_container(docker):
    print("starting docker container")
    await docker.start()
    print("Docker container STARTED")

async def stop_docker_container(docker):
    print("docker container stop")
    await docker.stop()
    print("Docker container END")