#cadastro de cliente, listagem de cliente, deletar cliente, buscar cliente
from time import sleep


class ClientesDB_V2:
    #construtor
    def __init__(self):

        #self.__id = Id
        #self.__nome = nome
        #self.__email = email 
        #self.__telefone = telefone
        #self.__endereco = endereco
        #self.__nascimento = nascimento
        #self.__genero = genero
        #self.__cpf = cpf
    
    
        #DICIONARIO
        self.clientes = []
        self.nomes = {}
        #self.email = {}
        #self.telefone = {}
        #self.endereco = {}
        #self.nascimento = {}
        #self.genero = {}
        self.cpf = {}

    #CADASTRO DE CLIENTE
    def cadastrar(Id):
        
        #try:
        print('\n' + '-'*50)
        Id += 1
        nome = input("digite o nome: ").strip().capitalize()
        #email = input("digite o email: ").strip()
        #telefone = input("digite o telefone: ").strip()
        #endereco = input("digite o endereco: ").strip().capitalize()
        #nascimento = input("digite a data de nascimento[dd/mm/aa]: ").strip()
        #genero = input("digite o genero[M/F: ")[0].strip().upper()
        cpf = input("digite o cpf: ").strip()

        cadastro_data = [nome, cpf]

        cadastro = ClientesDB_V2()
        #cadastro.inserir(cadastro_data)
        cadastro.inserir(str(Id), nome, cpf)
        #cadastro.inserir(str(Id), nome, email, telefone, endereco, nascimento, genero, cpf)
        #except:
        print('[ERROR], porfavor tente novamente')

        print('\nCadastro realizado com sucesso')
        print('-'*50)
        return Id, cadastro
        

    def listar(cadastro):
        
        
        try:
            print('\n' + '-'*50)
            cadastro.listar_clientes()
        except:
            print("cadastro nao encontrado.\nID incorreto ou inesistente")
        
        print('-'*50)



    #INSERSAO DE DADOS
    def inserir(self, Id, nome, cpf):
        #self.clientes.append(cadastro_data)
        
        self.nomes.update({Id: nome})
        #self.email.update({Id: email})
        #self.telefone.update({Id: telefone})
        #self.endereco.update({Id:endereco})
        #self.nascimento.update({Id: nascimento})
        #self.genero.update({Id: genero})
        self.cpf.update({Id: cpf})
        
    #LISTAGEM DE CLIENTES
    '''
    def listar_clientes(self):
        for item in self.clientes:
            print(f"nome: {item[0]}")
            print(f"cpf: {item[1]}")
            print(len(self.clientes))'''
        
    def listar_clientes(self):
        for Id in self.nomes.items():
            print(f"ID: {str(Id)}")
            print(f"nome: {self.nomes.get(Id)}")
            print(f"cpf: {self.cpf.get(Id)}")
            print(f"quantidade cadastrada: {len(self.nomes)}")
        
    #EXCLUSAO DE DADOS
    def deletar(self, Id):
        del self.nomes[Id]
        #del self.email[Id]
        #del self.telefone[Id]
        #del self.endereco[Id]
        #del self.nascimento[Id]
        #del self.genero[Id]
        del self.cpf[Id]

    #BUSCA DE DADOS
    def buscar(self, Id):
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

