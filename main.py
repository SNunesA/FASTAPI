from fastapi import FastAPI, Request
#Fastapi é um framework web de alta performance para construir APIs com suporte a tipagem de dados. 
# Request: é uma classe do módulo fastapi que representa uma requisição HTTP recebida pela aplicação.
import json 

app = FastAPI()
tarefas = dict()
id_count = 0

# Métodos CRUD
# Quando um cliente envia uma requisição HTTP POST para /cadastrar, a função cadastrar que recebe um objeto Request como argumento é executada.
@app.post("/cadastrar")
async def cadastrar(request: Request):
    global id_count
    global tarefas
    # cria um novo identificador único para cada tarefa.
    id_ = id_count
    id_count += 1
    # lê os dados enviados pelo cliente no corpo da requisição HTTP
    dados = await request.json()
    tarefas[id_] = dados
    print(tarefas)
     
# Quando um cliente envia uma requisição HTTP GET para /listar, a função listar é executada.
@app.get('/listar')
async def list():
    return tarefas

# Define a função salvar para ser executada quando o servidor é encerrado.
@app.on_event("shutdown")
async def salvar():
    global tarefas
    print(tarefas)
    with open("dados.json", "w") as file:
        json.dump(tarefas, file)

# Define a função carregar para ser executada quando o servidor é iniciado.
@app.on_event("startup")
async def carregar():
    global tarefas
    global id_count
    try:
        with open("dados.json", "r") as file:
            tarefas = json.load(file)
        # Percorre as chaves do dicionário agenda para encontrar o maior identificador único já usado e atualiza a variável id_count
        for key in tarefas:
            if int(key) > id_count:
                id_count = int(key)
        id_count += 1
    except:
        print("problema ao abrir o arquivo")

