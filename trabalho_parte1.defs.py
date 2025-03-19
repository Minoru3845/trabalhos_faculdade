
lista_de_colaboradores = [
        {"nome": "Bruno", "CPF": "123.123.123-00", "cargo": "gerente", "salario": 4000},
        {"nome": "Cesar", "CPF": "789.345.123-00", "cargo": "sub-gerente", "salario": 3000},
        {"nome": "Gabi", "CPF": "123.567.123-00", "cargo": "caixa", "salario": 1900},
        {"nome": "Lukinha", "CPF": "344.589.123-00", "cargo": "repositor", "salario": 1800},
        {"nome": "Gui", "CPF": "122.256.098-00", "cargo": "caixa-lider", "salario": 2500},
        ]

def lista_colaboradores():
    print(f"{'\n|.Lista de Colaboradores.|'}")
    
    for colaborador in lista_de_colaboradores:
        print(f"|Nome: {colaborador["nome"]}, CPF:{colaborador["CPF"]}, Cargo:{colaborador["cargo"]}, Salario:{colaborador["salario"]}")

def lista_alfabetica():
    print(f"{'\n|.Lista por ordem alfabetica.|'}")
    
    for colaborador in sorted(lista_de_colaboradores, key= lambda x : x['nome']):
        print(f"|.Nome: {colaborador["nome"]}, CPF:{colaborador["CPF"]}, Cargo:{colaborador["cargo"]}, Salario:{colaborador["salario"]}")

def lista_salario():
    print(f"{'\n|.Por ordem de salário.|'}")
    
    for colaborador in sorted(lista_de_colaboradores, key= lambda x: x["salario"]):
        print(f"|.Nome: {colaborador["nome"]}, CPF: {colaborador["CPF"]}, Cargo: {colaborador["cargo"]}, Salario: {colaborador["salario"]}")


def por_cargo():
    funcionario = input('\nDigite um cargo: ')

    lista_nova = []

    for colaborador in lista_de_colaboradores:
        if colaborador['cargo'].lower() == funcionario:
            lista_nova.append(colaborador)

    if lista_nova: 
        for colaborador in lista_nova:
            print(f"|.Nome: {colaborador["nome"]}, CPF:{colaborador["CPF"]}, Cargo:{colaborador["cargo"]}, Salario:{colaborador["salario"]}")

    else:
        print("O cargo nao esta na lista")