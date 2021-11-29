from time import sleep
from clientesDB import ClientesDB
#from cliente import Cliente

Id = 0


while True:
    
    print("cadastro")
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
        print("erro tente novamente")

    else:
        if menu == 'C':
            Id += 1
            nome = input("digite o nome: ")
            #Id = int(input("digite a ID: "))
            cpf = input("digite o cpf: ")
            
            cadastro = ClientesDB(Id, nome, cpf)
            cadastro.inserir(Id, nome, cpf)
           
            
            
        elif menu == 'L':
            
            
            cadastro.listar_clientes()
            

        elif menu == 'D':
            try:
                del_Id = int(input("digite o id a qual deseja deletar(esta acao nao poderar ser desfeita!): "))
                cadastro.deletar(del_Id)
            except:
                print("cadastro nao encontrado.\nid incorreto ou nao existente")

        elif menu == 'B':
            try:
                bus_Id = int(input("digite o id a qual deseja encontrar: "))
                cadastro.buscar(bus_Id)
            except:
                print("cadastro nao encontrado.\nID nao encontrado ou nao existente")
            
