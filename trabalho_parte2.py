
import programação.trabalho_parte1 as trabalho_parte1


def listas():


    print("-------------Digite uma opção------------")
    print("Digite 1 para ver a lista de colaboradores")
    print("Digite 2 para ver a lista em ordem alfabética")
    print("Digite 3 para ver a lista em ordem de Salário")
    print("Digite 4 para digitar cargo")
    print("Digite 5 para sair")


    while True:
        digite = input('Escolha uma opção: ')

        if digite == "1":
            trabalho_parte1.lista_colaboradores()
        
        elif digite == "2":
            trabalho_parte1.lista_alfabetica()
        
        elif digite == "3":
            trabalho_parte1.lista_salario()
        
        elif digite == "4":
            print("--Cargos existentes--\n |gerente \n |sub-gerente \n |caixa \n |repositor \n |caixa-lider")
            trabalho_parte1.por_cargo()
        
        elif digite == "5":
            print("cabou")
            break
        
        else: 
            print("Essa opção não existe.")


            


listas()
