#Bibliotecas
import json
from time import sleep
import os 
import requests

#Funções
def Write():
    json_file = open('sistema.json', mode='w')
    json.dump(sistema, json_file)
    json_file.close()

def Cliente():
    print('Clientes Cadastrados:')
    for c in sistema['clientes']:
        print(f'{c} ', end='')
    print('')
    cliente = input().capitalize()
    return cliente


def Cliente1(nome):
    while nome not in sistema['clientes']:
        print('Cliente não consta no sistema')
        sleep(2)
        nome = Cliente()
    return nome

def Vendedor():
    print('Selecione o Vendedor:')
    for c in sistema['vendas']:
        print(f'{c} ', end='')
    print('')
    vendedor = input().capitalize()
    return vendedor

def Vendedor1(nome):
    while nome not in sistema['vendas']:
        print('Vendedor não consta no sistema')
        sleep(2)
        nome = Vendedor()
    return nome

def Carro():
    print('Selecione o Carro:')
    for c in sistema['carros']:
        print(f'{c} ', end='')
    print('')
    carro = input().capitalize()
    return carro

def VerificaVendedor():
    if len(sistema['vendas']) == 0:
        print('Cadastros Insuficientes no Sistema')
        sleep(2)   
        return True
    return False

def VerificaCliente():
    if len(sistema['clientes']) == 0:
        print('Cadastros Insuficientes no Sistema')
        sleep(2)   
        return True
    return False


URL = "http://127.0.0.1:8000"

#Caso o arquivo não exista no diretorio
if os.path.exists("sistema.json") == False:
    json_file = open('sistema.json', mode='w')
    json_file.close()

#Caso o arquivo esteja vazio
if os.stat('sistema.json').st_size == 0:    
    sistema={"carros":[],"clientes":[],"vendas":{}}
    Write()

#Passa a estrutura {'carros':[],'clientes':[],'vendas':{vendedor:['cliente carro']}} para a variavel sistema
arq = open('sistema.json', mode='r')
sistema = json.load(arq)
arq.close()


print('Seja Bem-vindo')
op=-1
while op != 0:
    print('Escolha a opção que deseja:')
    print('0.Sair 1.Cadastrar - 2.Vender - 3.Listar - 4.Pesquisar')
    op = int(input())
    if op == 0: break
    # Cadastrar:carros a serem vendidos;clientes e vendedores;
    if op == 1:
        print("1.Carro - 2.Cliente - 3.Vendedor")
        cad = int(input())

        if cad == 1:
            x = int(input('Quantos carros deseja cadastrar? '))
            # Adiciona os modelos na lista da chave carros e depois salva no arquivo.json
            for c in range(x):
                sistema['carros'].append(input("Modelo:").capitalize())
            Write()

        if cad == 2:
            # Adiciona os nomes na lista da chave clientes
            x = int(input('Quantos clientes deseja cadastrar? '))
            for c in range(x):
                sistema['clientes'].append(input("Nome:").capitalize())
            Write()

        if cad == 3:
            # Adiciona os nomes no dicionario da chave vendas
            x = int(input('Quantos vendedores deseja cadastrar? '))
            for c in range(x):
                dic = {input("Nome:").capitalize(): []}
                sistema['vendas'].update(dic)
            Write()
        print('Cadastro Concluído')
        sleep(2)
    # Vender carros, onde é registrada a venda de um carro por um vendedor a um cliente.
    if op == 2:
        # Caso não tenha carros, clientes ou vendedores cadastrados, nao sera possivel realizar uma venda
        if VerificaVendedor():    continue
        if VerificaCliente():     continue
        if len(sistema['carros']) == 0: 
            print('Cadastros Insuficientes no Sistema')
            sleep(2)   
            continue

         # O usuário é obrigado a selecionar um cliente cadastrado
        nome = Cliente()
        cliente=Cliente1(nome)
        # O usuário é obrigado a selecionar um vendedor cadastrado
        nome = Vendedor()
        vendedor=Vendedor1(nome)
        # O usuário é obrigado a selecionar um carro cadastrado
        carro = Carro()
        while carro not in sistema['carros']:
            print('Carro não consta no sistema')
            sleep(2)
            carro = Carro()

        # O carro é removido da lista de disponiveis e é feita a relação das três informações
        sistema['carros'].remove(carro)
        sistema['vendas'][vendedor].append(f'{cliente} {carro}')
        Write()

    # Listar
    if op == 3:

        print('1.Carros Disponíveis 2.Carros Vendidos')
        cad = int(input())

        if cad == 1:
            if len(sistema['carros']) == 0: 
                print('0 Carros Disponiveis')
                sleep(2)
                continue
            for c in sistema['carros']:
                print(c, ' ', end='')
            print('')
            
        if cad == 2:
            lista=[] #lista que vai receber os carros vendidos
            for c in sistema['vendas']:
                if len(sistema['vendas'][c]) != 0:
                    for i in sistema['vendas'][c]:
                        x = i.split() #Dividindo o cliente do carro
                        lista.append(x[1]) 

            if len(lista)==0:      
                print('0 Carros Vendidos')
            else:
                for i in lista: print(i,' ',end='')
                print('')
        sleep(2)

    # Pesquisar
    if op == 4:
        print('1.Vendas por Vendedor 2.Carros por Cliente')
        cad = int(input())

        if cad == 1:
            # Caso não tenha vendedores cadastrados, não há como pesquisar as vendas
            if VerificaVendedor():    continue
            # O usuário é obrigado a selecionar um vendedor cadastrado
            nome = Vendedor()
            nome=Vendedor1(nome)

            # Quantidade de vendas e as vendas realizadas
            print(len(sistema['vendas'][nome]), ' Venda(s)')
            for c in sistema['vendas'][nome]:
                print(c)

        if cad == 2:
            # Caso não tenha clientes, não há como pesquisar as compras
            if VerificaCliente():     continue
            nome = Cliente()
            nome=Cliente1(nome)

            lista = [] #lista que vai receber os carros comprados
            for c in sistema['vendas']:
                if len(sistema['vendas'][c]) != 0:
                    for i in sistema['vendas'][c]:
                        x = i.split() #Dividindo o cliente do carro
                        if x[0] == nome:
                            lista.append(x[1])

            #  Quantidade de carros e os carros comprados
            print(len(lista), ' Carro(s)')
            for i in lista:
                print(i)
        sleep(2)
