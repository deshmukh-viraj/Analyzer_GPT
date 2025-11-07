from agents.code_executor import GetCodeExecutorAgent
from agents.data_analyzer import GetDataAnalyzerAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination


def getDataAnalyzerTeam(docker, model_client):

    data_analyzer_agent = GetDataAnalyzerAgent(model_client)
    code_executor_agent = GetCodeExecutorAgent(docker)

    termination_condition = TextMentionTermination('STOP')
    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_executor_agent],
        max_turns=10,
        termination_condition=termination_condition
    )
    return team


