#cadastro de cliente, listagem de cliente, deletar cliente, buscar cliente
from time import sleep



#DICIONARIO
clientes = []
nomes_dic = {}



#MENU
def menu():
    while True:

        print("================ cadastro ===================")
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
                    del_Id = input("digite o ID a qual deseja deletar: ")
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
                    bus_Id = input("digite o ID a qual deseja encontrar: ")
                    buscar(bus_Id)
                except:
                    print("cadastro nao encontrado.\nID nao encontrado ou nao existente")

                print('-'*50)
        
#CADASTRO DE CLIENTE
def cadastrar():
    
    try:
        print('\n' + '-'*50)
        
        nome = input("digite o nome: ").strip().capitalize()
        #email = input("digite o email: ").strip()
        #telefone = input("digite o telefone: ").strip()
        #endereco = input("digite o endereco: ").strip().capitalize()
        #nascimento = input("digite a data de nascimento[dd/mm/aa]: ").strip()
        #genero = input("digite o genero[M/F: ")[0].strip().upper()
        cpf = input("digite o cpf: ").strip()

        cadastro_data = [nome, cpf]
        clientes.append(cadastro_data)


        #cadastro.inserir(str(Id), nome, email, telefone, endereco, nascimento, genero, cpf)
    except:
        print('[ERROR], porfavor tente novamente')

    print('\nCadastro realizado com sucesso')
    print('-'*50)

#LISTAGEM DE CLIENTES
def listar_clientes():
    for item in clientes:
        print(f"nome: {item[0]}")
        print(f"cpf: {item[1]}")
        print(len(clientes))

    
#EXCLUSAO DE DADOS
def deletar(Id):
    del self.nomes[Id]
    #del self.email[Id]
    #del self.telefone[Id]
    #del self.endereco[Id]
    #del self.nascimento[Id]
    #del self.genero[Id]
    del self.cpf[Id]

#BUSCA DE DADOS
def buscar(Id):
    print(f"ID: {Id}")
    print(f"nome: {self.nomes.get(Id)}")
    #print(f"email: {self.email.get(Id)}")
    #print(f"telefone: {self.telefone.get(Id)}")
    #print(f"endereco: {self.endereco.get(Id)}")
    #print(f"nascimento: {self.nascimento.get(Id)}")
    #print(f"genero: {self.genero.get(Id)}")
    print(f"CPF: {self.cpf.get(Id)}")


#EXEMPLO DE DADO
#cadastro = Cliente(1, 'Rafael', 'rafael@gmail.com', '(71)900001111', 'rua fernado queiros', '20/12/1966', 'M', '123312434')


menu()