
import trabalho_parte1_def

trabalho_parte1_def.listas()

while True:
        digite = input('\nEscolha uma opção: ')
        
        if digite == "1":
            trabalho_parte1_def.lista_colaboradores()
            trabalho_parte1_def.listas()

        elif digite == "2":
            trabalho_parte1_def.lista_alfabetica()
            trabalho_parte1_def.listas()
        elif digite == "3":
            trabalho_parte1_def.lista_salario()
            trabalho_parte1_def.listas()

        elif digite == "4":
            trabalho_parte1_def.por_cargo()
            trabalho_parte1_def.listas()
        
        elif digite == "5":
            print("cabou")
            break
        
        else: 
            print("Essa opção não existe.")


