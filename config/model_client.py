from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("SERPER_API_KEY")


def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model = "gemini-2.0-flash",
        api_key = api_key
    )

    return model_client
