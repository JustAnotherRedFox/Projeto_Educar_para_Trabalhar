#cadastro de cliente, listagem de cliente, deletar cliente, buscar cliente
from time import sleep

#DICIONARIOS
clientes = []
class Color:
    #textBlack = '\033[30m'
    ErrorColor = '\033[1;31m'
    MenuColor = '\033[32m'
    WarningColor = '\033[33m'
    ExitColor = '\033[34m'
    #textPurple = '\033[35m'
    #textCyan = '\033[36m'
    #textWhite = '\033[37m'

    #backgroundBlack = '\033[40m'
    #backgroundRed = '\033[41m'
    #backgroundGreen = '\033[42m'
    #backgroundYelow = '\033[43m'
    #backgroundBlue = '\033[44m'
    #backgroundPurple = '\033[45m'
    #backgroundCyan = '\033[46m'
    #backgroundWhite = '\033[47m'

    #styleBold = '\033[1m'
    #styleUnderline = '\033[2m'
    endColor = '\033[0m'


#MENU
def menu():
    while True:

        print("{:=^50}".format(' Menu Inicial '))
        menu = input(f'''{Color.MenuColor}
            [C].Cadastrar Cliente
            [L].Listar Clientes
            [D].Deletar Cliente
            [B].Buscar Cliente
            [S].Sair
            {Color.endColor}
            Digite a opcao correspondente: ''').strip().upper()

        if menu == 'S':
            print('-'*50)
            print(f'{Color.ExitColor}Aguarde... Encerrando Programa{Color.endColor}')
            print('-'*50)
            sleep(0.7)
            break

        elif menu != 'C'and menu != 'L' and menu != 'D' and menu != 'B' and  menu != 'S':
            print(f"\n{Color.ErrorColor}[ERROR] Opcao Invalida, Tente Novamente [ERROR]{Color.endColor}")

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
                    confirm = input(f"{Color.WarningColor}[WARNING] Tem certeza? Esta acao nao podera ser Desfeita! [WARNING]{Color.endColor}\n[S/N]: ")[0].upper()

                    if confirm == 'S':
                        deletar(del_Id)
                        erro = 0

                    elif confirm == 'N':
                        print('\nExclusao Cancelada')

                    else:
                        erro = 1 / 0
                except:
                    print(f"{Color.ErrorColor}[ERROR] Cadastro Nao Encontrado [ERROR]{Color.endColor}\nID incorreto ou nao existente")
                    erro = 1

                if confirm == 'S' and erro == 0:
                    print('\nCadastro Deletado com Sucesso')
                
                print('-'*50)

            #MENU - BUSCAR CADASTROS
            elif menu == 'B':
                try:
                    print('\n' + '-'*50)
                    bus_Id = int(input("digite o ID a qual deseja encontrar: "))
                    buscar(bus_Id)

                except:
                    print('-'*50)
                    print(f"{Color.ErrorColor}[ERROR] Cadastro Nao Encontrado [ERROR]{Color.endColor}\nID nao encontrado ou nao existente")

                print('-'*50)
        
#CADASTRO DE CLIENTE
def cadastrar():
    
    try:
        #print('\n' + '-'*50)
        print('{:=^50}'.format(' Cadastro '))
        
        nome = input("digite o nome: ").strip().capitalize()
        email = input("digite o email: ").strip()
        telefone = input("digite o telefone: ").strip()[:14]
        endereco = input("digite o endereco: ").strip().capitalize()
        nascimento = input("digite a data de nascimento[dd/mm/aaaa]: ").strip()[:10]
        genero = input("digite o genero[M/F]: ")[0].strip().upper()
        cpf = input("digite o cpf: ").strip()[:14]

        if genero == 'F':
            genero = 'Feminino'
            erro = 0

        elif genero == 'M':
            genero = 'Masculino'
            erro = 0

        else:
            genero = 1 / 0
        
        cadastro_data = [nome, email, telefone, endereco, nascimento, genero, cpf]

        clientes.append(cadastro_data)


    except:
        print('\n' + '-'*50)
        print(f'{Color.ErrorColor}[ERROR] Porfavor Tente Novamente [ERROR]{Color.endColor}')
        print('-'*50)
        erro = 1

    if erro == 1:
        pass

    else:
        print('\nCadastro realizado com sucesso')
        print('-'*50)

#LISTAGEM DE CLIENTES
def listar_clientes():
    print('-'*50)
    if len(clientes) == 0:
        print(f"{Color.ErrorColor}[ERROR] Cadastro Nao Encontrado [ERROR]{Color.endColor}\nporfavor cadastre um ID primeiro")

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
    if len(clientes) == 0:
        return 1 / 0

    else:
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