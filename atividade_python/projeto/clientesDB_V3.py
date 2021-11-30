#cadastro de cliente, listagem de cliente, deletar cliente, buscar cliente
from time import sleep

#DICIONARIO
clientes = []

#MENU
def menu():
    while True:

        print("{:=^50}".format(' Menu Inicial '))
        menu = input('''
            [C].Cadastrar Cliente
            [L].Listar Clientes
            [D].Deletar Cliente
            [B].Buscar Cliente
            [S].Sair
        Digite a opcao correspondente: ''').strip().upper()

        if menu == 'S':
            print('Aguarde... Encerrando Programa')
            sleep(0.7)
            break

        elif menu != 'C'and menu != 'L' and menu != 'D' and menu != 'B' and  menu != 'S':
            print("[ERROR] escolha invalida, tente novamente")

        else:
            #MENU - CADASTRAR CLIENTE
            if menu == 'C':
                cadastrar()
                
            #MENU - LISTAR CLIENTE
            elif menu == 'L':
                listar_clientes()

            #MENU - DELETAR CADASTROS
            elif menu == 'D':
                try:
                    print('\n' + '-'*50)
                    del_Id = int(input("digite o ID a qual deseja deletar: "))
                    confirm = input("Tem certeza? Esta acao nao podera ser Desfeita![S/N]: ")[0].upper()
                    if confirm == 'S':
                        deletar(del_Id)
                    else:
                        pass
                except:
                    print("cadastro nao encontrado.\nID incorreto ou nao existente")

                if confirm == 'S':
                    print('\nCadastro deletado com sucesso')
                elif confirm == 'N':
                    print('\nExclusao cancelada')
                
                print('-'*50)

            #MENU - BUSCAR CADASTROS
            elif menu == 'B':
                try:
                    print('\n' + '-'*50)
                    bus_Id = int(input("digite o ID a qual deseja encontrar: "))
                    buscar(bus_Id)
                except:
                    print("cadastro nao encontrado.\nID nao encontrado ou nao existente")

                print('-'*50)
        
#CADASTRO DE CLIENTE
def cadastrar():
    
    try:
        print('\n' + '-'*50)
        print('{:=^50}'.format(' Cadastro '))
        
        nome = input("digite o nome: ").strip().capitalize()
        email = input("digite o email: ").strip()
        telefone = input("digite o telefone: ").strip()
        endereco = input("digite o endereco: ").strip().capitalize()
        nascimento = input("digite a data de nascimento[dd/mm/aa]: ").strip()
        genero = input("digite o genero[M/F]: ")[0].strip().upper()
        cpf = input("digite o cpf: ").strip()

        if genero == 'F':
            genero = 'Feminino'

        elif genero == 'M':
            genero = 'Masculino'

        #Para textes rapidos descomente esta linha e comente a de baixo/no cadastro pode-se colocar qualquer coisa
        #cadastro_data = ['Rafael', 'rafael@gmail.com', '(71)900001111', 'rua fernado queiros', '20/12/1966', 'Masculino', '1233.1243-34']

        cadastro_data = [nome, email, telefone, endereco, nascimento, genero, cpf]
        clientes.append(cadastro_data)


    except:
        print('[ERROR], porfavor tente novamente')

    print('\nCadastro realizado com sucesso')
    print('-'*50)

#LISTAGEM DE CLIENTES
def listar_clientes():
    print('-'*50)
    if len(clientes) == 0:
        print("cadastro nao encontrado.\nporfavor cadastre um ID primeiro")

    else:
        print(f"Clientes Cadastrados: {len(clientes)}")
        print('-'*50)
        for pessoa in clientes:
            
            print(f"ID: {clientes.index(pessoa)}")
            print(f"nome: {pessoa[0]}")
            print(f"genero: {pessoa[5]}")
            print(f"cpf: {pessoa[6]}")
            
            print('-'*50)

    
#EXCLUSAO DE DADOS
def deletar(del_Id):
    del(clientes[del_Id])

#BUSCA DE DADOS
def buscar(bus_Id):
    print('-'*50)
    print(f"ID: {bus_Id}")
    print(f"Nome: {clientes[bus_Id][0]}")
    print(f"Email: {clientes[bus_Id][1]}")
    print(f"Telefone: {clientes[bus_Id][2]}")
    print(f"Endereco: {clientes[bus_Id][3]}")
    print(f"Data de nascimento: {clientes[bus_Id][4]}")
    print(f"Genero: {clientes[bus_Id][5]}")
    print(f"CPF: {clientes[bus_Id][6]}")


menu()