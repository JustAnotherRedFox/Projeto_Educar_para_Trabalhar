class Pessoa:
    
    #construtor
    def __init__(self, nome, sexo, cpf, ativo):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__ativo = ativo

    def set_nome(self,nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_sexo(self):
        return self.__sexo

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    def set_ativo(self, ativo):
        self.__ativo = ativo

    def get_ativo(self):
        return self.__ativo

    def desativar(self):
        self.__ativo = False
        print("A pessoa foi desativada com sucesso")

    def ativar(self):
        self.__ativo = True
        print("A pessoa foi ativada com sucesso")

#instanciando o objeto
pessoa1 = Pessoa("João", "M", "123456", True)

pessoa1.set_nome('Rafael')
pessoa1.set_ativo(False)
pessoa1.set_sexo('F')

print('Nome: ', pessoa1.get_nome())
print('Sexo: ', pessoa1.get_sexo())
print('CPF: ', pessoa1.get_cpf())
print('Ativo: ', pessoa1.get_ativo())

