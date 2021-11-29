#Criar uma classe chamada Produto, e ele tem os seguintes campos: codigo, descrição, preço, status, estoque.
#Criar metodo para acrescentar 10% no valor do produto
#Criar metodo para ativar e desativar o produto
#Criar metodo para verificar se o estoque esta positivo ou negativo

class Produto:

    #construtor
    def __init__(self, codigo, descricao, preco, status, estoque, ativo):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__status = status
        self.__estoque = estoque
        self.__ativo = ativo

    def acrescimo(self):
        acrescimo = self.__preco + (self.__preco * (10/100))
        print(f"preco com acrescimo: R${acrescimo:.2f}")

    def estoque_status(self):
        if self.__estoque > 0:
            print("\nseu estoque esta positivo")

        elif self.__estoque == 0:
            print("\nseu estoque esta vazio")

        elif self.__estoque < 0:
            print("\nseu estoque esta negativo")

    def ativar(self):
        self.__ativo = True
        print("o produto foi ativado com sucesso.\n")

    def desativar(self):
        self.__ativo = False
        print("o produto foi desativado com sucesso.\n")

    #setters
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_descricao(self, descricao):
        self.__descricao = descricao
    
    def set_preco(self, preco):
        self.__preco = preco

    def set_status(self, status):
        self.__status = status
    
    def set_estoque(self, estoque):
        self.__estoque = estoque


    #getters
    def get_codigo(self):
        print(f"codigo:  {self.__codigo}")

    def get_descricao(self):
        print(f"descricao: {self.__descricao}")

    def get_preco(self):
        print(f"preco:  R${self.__preco:.2f}")

    def get_status(self):
        print(f"status:  {self.__status}")

    def get_estoque(self):
        print(f"estoque:  {self.__estoque}")
    
    def get_ativo(self):
        print(f"ativo:  {self.__ativo}")

'''
#instaciacao do objeto
produto1 = Produto(201, 'shampoo', 1000, 'disponivel', 20, True)

#substituindo valores
produto1.set_codigo('404')
produto1.set_status('produto nao encontrado')
produto1.set_estoque(00)
produto1.desativar()

#chamando os valores
produto1.get_codigo()
produto1.get_descricao()
produto1.get_preco()
produto1.acrescimo()
produto1.get_status()
produto1.get_estoque()
produto1.get_ativo()
produto1.estoque_status()
'''
