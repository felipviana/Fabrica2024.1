#Fazer uma aplicação que o usuário entra com o cep e retorna a ele a localização, através da api

import requests

entrada=input("Digite seu cep(sem pontuação por favor c:):\n")
json = requests.get(f'https://viacep.com.br/ws/{entrada}/json/')
retorno =json.json()
print(f"Sua localidade é:\n {retorno}")
