import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled
load_dotenv()
set_tracing_disabled(disabled=True)
client = AsyncOpenAI(
api_key=os.getenv('API_KEY'),
base_url=os.getenv('BASE_URL'),
)
model = OpenAIChatCompletionsModel(
model=os.getenv('MODEL_NAME'),
openai_client=client,
)