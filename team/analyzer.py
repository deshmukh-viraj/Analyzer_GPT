from agents.code_executor import GetCodeExecutorAgent
from agents.data_analyzer import GetDataAnalyzerAgent
from autogen_agentchat.teams import RoundRobinGroupChat

def getDataAnalyzerTeam(docker, model_client):

    code_executor_agent = GetCodeExecutorAgent(docker)

    data_analyzer_agent = GetDataAnalyzerAgent(model_client)

    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_executor_agent],
        max_turns=10
    )
    return team


