import openai

API_KEY = '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'
modelo = 'text-davinci-003'
pergunta = 'Gere uma mensagem com 10 palavras'

openai.api_key = API_KEY

response = openai.Completion.create(
    engine=modelo,
    prompt=pergunta,
    max_tokens=1024
)

print(response.choices[0]['text'])