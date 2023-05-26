import openai

API_KEY = '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'
modelo = 'text-davinci-003'
pergunta = 'Gere uma mensagem com 10 palavras'

openai.api_key = API_KEY

#GERAR IMAGEM
response = openai.Image.create(
    prompt='Gere uma bandeira',
    size='512x512',
    n=1
)
print(response.data[0]['url'])

#GERAR TEXTO
# response = openai.Completion.create(
#     engine=modelo,
#     prompt=pergunta,
#     max_tokens=1024
# )
# print(response.choices[0]['text'])