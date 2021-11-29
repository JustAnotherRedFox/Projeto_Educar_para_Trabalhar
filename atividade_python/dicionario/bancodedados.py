class BancoDeDados:
    def __init__(self, id, nome, rg):
        self.__id = id
        self.__nome = nome
        self.__rg = rg

        self.nomes = {}
        self.rg = {}

        def inserir(self, id, nome, rg):
            self.nomes.update({id: nome})
            self.rg.update({id: rg})

        def lista_clientes(self):
            for id, nome in self.nomes.items():
                print(f"ID: {id}")
                print(f"nome: {nome}")
                print(f"RG: {self.rg.get(id)}")

        def deletar(self, id):
            del self.nomes[id]
            del self.rg[id]
