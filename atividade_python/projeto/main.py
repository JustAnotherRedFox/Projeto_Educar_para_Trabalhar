from time import sleep
from clientesDB import ClientesDB

Id = 0


while True:
    
    print("================ cadastro ===================")
    #MENU
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
        #CADASTRAR CLIENTE
        if menu == 'C':
            try:
                print('\n' + '-'*50)
                nome = input("digite o nome: ").strip().capitalize()
                Id += 1
                #Id = int(input("digite a ID: "))
                cpf = input("digite o cpf: ").strip()

                cadastro = ClientesDB()
                cadastro.inserir(str(Id), nome, cpf)
            except:
                print('[ERROR], porfavor tente novamente')

            print('\nCadastro realizado com sucesso')
            print('-'*50)

        #LISTAR CADASTROS
        elif menu == 'L':
            
            try:
                print('\n' + '-'*50)
                cadastro.listar_clientes()
            except:
                print("cadastro nao encontrado.\nID incorreto ou inesistente")
            
            print('-'*50)

        #DELETAR CADASTROS
        elif menu == 'D':
            try:
                print('\n' + '-'*50)
                del_Id = input("digite o ID a qual deseja deletar: ")
                confirm = input("Tem certeza? Esta acao nao podera ser Desfeita![S/N]: ")[0].upper()
                if confirm == 'S':
                    cadastro.deletar(del_Id)
                else:
                    pass
            except:
                print("cadastro nao encontrado.\nID incorreto ou nao existente")

            if confirm == 'S':
                print('\nCadastro deletado com sucesso')
            elif confirm == 'N':
                print('\nExclusao cancelada')
            
            print('-'*50)

        #BUSCAR CADASTROS
        elif menu == 'B':
            try:
                print('\n' + '-'*50)
                bus_Id = input("digite o ID a qual deseja encontrar: ")
                cadastro.buscar(bus_Id)
            except:
                print("cadastro nao encontrado.\nID nao encontrado ou nao existente")

            print('-'*50)
            
