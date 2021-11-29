#cadastro de cliente, listagem de cliente, deletar cliente, buscar cliente
from cliente import Cliente

class ClientesDB():
    #construtor
    def __init__(self, Id, nome, cpf):

        self.__id = Id
        self.__nome = nome
        #self.__email = email 
        #self.__telefone = telefone
        #self.__endereco = endereco
        #self.__nascimento = nascimento
        #self.__genero = genero
        self.__cpf = cpf
    
    
        #dicionario
        self.nomes = {self.__id: self.__nome}
        #self.email = {}
        #self.telefone = {}
        #self.endereco = {}
        #self.nascimento = {}
        #self.genero = {}
        self.cpf = {self.__id, self.__cpf}

    def inserir(self, Id, nome, cpf):
        self.nomes.update({Id: nome})
        #self.email.update({Id: email})
        #self.telefone.update({Id: telefone})
        #self.endereco.update({Id:endereco})
        #self.nascimento.update({Id: nascimento})
        #self.genero.update({Id: genero})
        self.cpf.update({Id: cpf})
        
    
    def listar_clientes(self):
        for Id, nome in self.nomes.items():
            print(f"id: {str(Id)}")
            print(f"nome: {str(nome)}")
            print(f"cpf: {self.cpf.get(Id)}")
            print(f"quantidade cadastrada: {len(self.nomes)}")
        

    def deletar(self, Id):
        del self.nomes[Id]
        #del self.email[Id]
        #del self.telefone[Id]
        #del self.endereco[Id]
        #del self.nascimento[Id]
        #del self.genero[Id]
        del self.cpf[Id]

    def buscar(self, Id):
        print(f"ID: {Id}")
        print(f"nome: {self.nomes[Id]}")
        #print(f"email: {self.email[Id]}")
        #print(f"telefone: {self.telefone[Id]}")
        #print(f"endereco: {self.endereco[Id]}")
        #print(f"nascimento: {self.nascimento[Id]}")
        #print(f"genero: {self.genero[Id]}")
        print(f"CPF: {self.cpf[Id]}")
    

#instanciando o objeto
#rafael = Cliente(1, 'Rafael', 'rafael@gmail.com', '(71)900001111', 'rua fernado queiros', '20/12/1966', 'M', '123312434')

