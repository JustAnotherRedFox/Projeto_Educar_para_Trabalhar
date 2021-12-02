from time import sleep

#DICIONARIOS
clientes = []
class Color:

    ErrorColor = '\033[1;31m'
    MenuColor = '\033[32m'
    WarningColor = '\033[33m'
    ExitColor = '\033[34m'

    endColor = '\033[0m'

class Message:
    ErrorMessage = '[ERROR] Opcao Invalida, Tente Novamente [ERROR]'
    ErrorCadastroMessage = '[ERROR] Cadastro Nao Encontrado [ERROR]'
    ErrorIdMessage = '[ERROR] ID Nao Encontrado ou Inexistente [ERROR]'
    WarningMessage = '[WARNING] Tem certeza? Esta acao nao podera ser Desfeita! [WARNING]'


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
            Digite a Opcao Desejada: ''').strip().upper()

        if menu != 'C'and menu != 'L' and menu != 'D' and menu != 'B' and  menu != 'S':
            print(f"\n{Color.ErrorColor}{Message.ErrorMessage}{Color.endColor}")

        else:
            #MENU - CADASTRAR CLIENTE
            if menu == 'C':
                cadastrar()
                
            #MENU - LISTAR CLIENTE
            elif menu == 'L':
                listar()

            #MENU - DELETAR CADASTROS
            elif menu == 'D':
                deletar()

            #MENU - BUSCAR CADASTROS
            elif menu == 'B':
                buscar()

            #MENU - ENCERRAR PROGRAMA
            elif menu == 'S':
                print('-'*50)
                print(f'{Color.ExitColor}Aguarde... Encerrando Programa{Color.endColor}')
                print('-'*50)
                sleep(0.7)
                break
        
#CADASTRO DE CLIENTE
def cadastrar():
    
    try:
        #print('\n' + '-'*50)
        print('{:=^50}'.format(' Cadastro '))

        #para sesativar o auto-gerado cadastro comente o codigo
        #check = 'N'
        check = input('deseja um cadastro auto-gerado?[Y/N]: ')

        if check == 'Y':
            nome = 'Rafell Barcel'
            email = 'Rafell.2020@gmail.com'
            telefone = '(71)98888-0000'
            endereco = 'Rua Fernando Morais'
            nascimento = '20/12/1944'
            genero = 'Masculino'
            cpf = '000.000.000-34'
            erro = 0

        else:
            nome = input("digite o nome: ").strip().capitalize()
            email = input("digite o email: ").strip()
            telefone = input("digite o telefone: ").strip()[:14]
            endereco = input("digite o endereco: ").strip().capitalize()
            nascimento = input("digite a data de nascimento[dd/mm/aaaa]: ").strip()[:10]
            genero = input("digite o genero[M/F]: ")[0].strip().upper()
            cpf = input("digite o cpf: ").strip()[:14]

            if genero == 'F':
                genero = 'Feminino'

            elif genero == 'M':
                genero = 'Masculino'

            else:
                genero = 1 / 0
        
        cadastro_data = [nome, email, telefone, endereco, nascimento, genero, cpf]

        clientes.append(cadastro_data)

        print('\nCadastro realizado com sucesso')
        print('-'*50)

    except:
        print('\n' + '-'*50)
        print(f'{Color.ErrorColor}{Message.ErrorMessage}{Color.endColor}')
        print('-'*50)
  
#LISTAGEM DE CLIENTES
def listar():
    print('-'*50)
    if len(clientes) == 0:
        print(f"{Color.ErrorColor}{Message.ErrorCadastroMessage}{Color.endColor}\n{Message.ErrorIdMessage}")

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
def deletar():
    try:
        print('\n' + '-'*50)
        del_Id = int(input("digite o ID a qual deseja deletar: "))
        confirm = input(f"{Color.WarningColor}{Message.WarningMessage}{Color.endColor}\n[S/N]: ")[0].upper()

        if confirm == 'S' and len(clientes) != 0:
            del(clientes[del_Id])
            sleep(0.7)
            print('\nCadastro Deletado com Sucesso')

        elif confirm == 'N' and len(clientes) != 0:
            print('\nExclusao Cancelada')

        else:
            erro = 1 / 0
    except:
        print(f"{Color.ErrorColor}{Message.ErrorCadastroMessage}{Color.endColor}\n{Message.ErrorIdMessage}")

    print('-'*50)

#BUSCA DE DADOS
def buscar():
    try:
        print('\n' + '-'*50)
        bus_Id = int(input("digite o ID a qual deseja encontrar: "))

        if len(clientes) == 0:
            error = 1 / 0

        else:    
            print('-'*50)
            sleep(0.8)

            print(f"ID: {bus_Id}")
            print(f"Nome: {clientes[bus_Id][0]}")
            print(f"Email: {clientes[bus_Id][1]}")
            print(f"Telefone: {clientes[bus_Id][2]}")
            print(f"Endereco: {clientes[bus_Id][3]}")
            print(f"Data de nascimento: {clientes[bus_Id][4]}")
            print(f"Genero: {clientes[bus_Id][5]}")
            print(f"CPF: {clientes[bus_Id][6]}")
            print('-'*50)

    except:
        print('-'*50)
        print(f"{Color.ErrorColor}{Message.ErrorCadastroMessage}{Color.endColor}\n{Message.ErrorIdMessage}")
    
menu()