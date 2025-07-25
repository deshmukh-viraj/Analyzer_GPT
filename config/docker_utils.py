from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from constants import WORK_DIR_DOCKER, TIMEOUT_DOCKER

def getDockerCommandLineExecutor():
    docker = DockerCommandLineCodeExecutor(
        work_dir = WORK_DIR_DOCKER,
        timeout = TIMEOUT_DOCKER
    )
    return docker


async def start_docker_container(docker):
    print("starting docker container")
    await docker.start()

async def stop_docker_container(docker):
    print("docker container stop")
    await docker.stop()