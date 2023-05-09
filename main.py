from fastapi import FastAPI, Request
import json 

app = FastAPI()
agenda = dict()
id_count = 0

# Métodos CRUD
@app.post("/cadastrar")
async def cadastrar(request: Request):
    global id_count
    global agenda

    id_ = id_count
    id_count += 1
    
    dados = await request.json()
    agenda[id_] = dados
    print(agenda)
    return {"id": id_}

@app.get('/listar')
async def list():
    return agenda

# Métodos de salvamento
@app.on_event("shutdown")
async def salvar():
    global agenda
    print(agenda)
    with open("dados.json", "w") as file:
        json.dump(agenda, file)

@app.on_event("startup")
async def carregar():
    global agenda
    global id_count
    try:
        with open("dados.json", "r") as file:
            agenda = json.load(file)
        for key in agenda:
            if int(key) > id_count:
                id_count = int(key)
        id_count += 1
    except:
        print("problema ao abrir o arquivo")

