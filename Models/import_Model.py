from transformers import pipeline
# Importacao da biblioteca Transformers

# cada variavel abaixo é um modelo de IA Diferente
    # Estao puxando resportas do Tipo Text
model = pipeline('text-generation', model='openai-gpt')
model1 = pipeline('text-generation', model='gpt2')
model2 = pipeline('text-generation', model='distilgpt2')

prompt = input("Digite Seu prompt: ")
    # Esta solicitando um dado para o usuario

result = model(prompt, max_length=50, truncation = True)
    # esta atribuindo esse dado a outra variavel e Truncando (limitando o numero de Tokens)

print(result)
    # Solicitando o retorno da variavel