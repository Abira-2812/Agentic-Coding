
from agents import Agent, Runner
from llm import model

def ask_agent(question, role='helpful assistant'):
    agent = Agent(
        name='Helper',
        instructions=f'You are a {role}. Answer in 3 short lines.',
        model=model,
    )

    result = Runner.run_sync(agent, question)
    return result.final_output


name = input('Aap ka naam: ')
question = input('Sawal: ')

print(f'Salam {name}!')
print(ask_agent(question))

print('---')

print(ask_agent(question, role='strict teacher'))
