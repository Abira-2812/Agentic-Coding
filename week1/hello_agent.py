from agents import Agent, Runner
from llm import model


agent = Agent(
name='Assistant',
instructions='Answer concisely.' ,
model=model,
)
result = Runner.run_sync(agent, 'Write a haiku about Karachi.')
print(result.final_output)