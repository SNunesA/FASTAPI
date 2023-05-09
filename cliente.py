import requests

URL = "http://127.0.0.1:8000"

while True:
    nome = input("Digite o nome: ")
    if nome == "":
        break
    idade = input("Digite a idade: ")

    registro = {
        "nome": nome, 
        "idade": idade
    }

    response = requests.post(f"{URL}/cadastrar", json=registro)
    print(response.status_code)
    print(response.json())