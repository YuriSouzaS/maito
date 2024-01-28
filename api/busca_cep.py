import requests
import jsons

cep = "09951090"
url2 = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url2)

y = response.json()

some_instance = jsons.load(y)
some_dict = jsons.dump(some_instance)

print(some_dict)
# criar uma classe com metodos de retorno