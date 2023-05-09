import requests
from time import sleep
URL = "http://127.0.0.1:8000"

print('Seja Bem-vindo a lista de tarefas')
op=-1
while op != 0:
    print('Escolha a opção que deseja:')
    print('0.Sair 1.Cadastrar - 2.Listar')
    op = int(input())
    #Fecha a execução
    if op == 0: break
    # Cadastrar
    if op == 1:
        x = int(input('Quantas tarefas deseja cadastrar? '))
        for c in range(x):
            nome=input("Nome da tarefa:")
            descricao=input("Descrição:")
            data=input('Data (DD/MM/AA):')
            registro = {
            "nome": nome, 
            "descricao": descricao,
            "data":data
            }
            response = requests.post(f"{URL}/cadastrar", json=registro)
            print("Tarefa cadastrada!")
            sleep(1)
    # Listar
    if op == 2:
        response= requests.get(f"{URL}/listar")
        dados=response.json()
        
        if len(dados) == 0: 
            print('Nenhuma Tarefa na Lista')
        for i in dados:
            for c in dados[i]:     
                print(dados[i][c])
            print('')
            

       
        



    
   