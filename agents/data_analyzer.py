from autogen_agentchat.agents import AssistantAgent
from agents.prompts.DataAnalyzerPrompt import DATA_ANALYZER_MSG
from config.model_client import get_model_client

model_client = get_model_client()

def getDataAnalyzerAgent(model_client):
    data_analyzer_agent = AssistantAgent(
        name = "Data_Analyzer_Agent",
        description='An agent which helps with solving Data Analysis task and gives the code as well',
        model_client=model_client,
        system_message=DATA_ANALYZER_MSG
    )

    return data_analyzer_agent