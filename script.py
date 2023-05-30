import openai
from get_env import print_env

env = print_env(['app_key'])

openai.api_key = env['app_key']

model_engine = 'text-davinci-003'

while True:
    print(50*'-')
    prompt = input('Escreva algo:')
    print('O GPT está processando sua mensagem...')

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.5,
    )

    print(50*'-')
    response = completion.choices[0].text
    print(response)
    print(50*'-')
    print(50*'-')
    saida = input('Você deseja sair do chat?')

    if saida == 'sim':
        break