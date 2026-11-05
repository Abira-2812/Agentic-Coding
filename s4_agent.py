# s4_agent.py
from agents import Agent, Runner
from llm import model

INSTRUCTIONS = 'You are a clinic assistant. Help patients schedule appointments, answer common medical questions, and provide general assistance.'

agent = Agent(INSTRUCTIONS, model=model)

while True:
    user_input = input('Enter message (or quit): ')
    if user_input.lower() == 'quit':
        break
    result = Runner.run_sync(agent, user_input)
    print(result.final_output)