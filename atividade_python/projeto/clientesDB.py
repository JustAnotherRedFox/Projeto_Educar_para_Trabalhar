#cadastro de cliente, listagem de cliente, deletar cliente, buscar cliente


class ClientesDB:
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
        self.nomes = {}
        #self.email = {}
        #self.telefone = {}
        #self.endereco = {}
        #self.nascimento = {}
        #self.genero = {}
        self.cpf = {}

    #INSERSAO DE DADOS
    def inserir(self, Id, nome, cpf):
        self.nomes.update({Id: nome})
        #self.email.update({Id: email})
        #self.telefone.update({Id: telefone})
        #self.endereco.update({Id:endereco})
        #self.nascimento.update({Id: nascimento})
        #self.genero.update({Id: genero})
        self.cpf.update({Id: cpf})
        
    #LISTAGEM DE CLIENTES
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

