#importando a class Produto do archivo Produto(.py)
from Produto import Produto

#instanciando o objeto
produto1 = Produto(201, 'shampoo', 1000, 'disponivel', 20, True)

#substituindo valores da classe pelo metodo set
produto1.set_codigo('404')
produto1.set_status('produto nao encontrado')
produto1.set_estoque(00)
produto1.desativar()

#chamando os valores da classe pelo metodo get
produto1.get_codigo()
produto1.get_descricao()
produto1.get_preco()
produto1.acrescimo()
produto1.get_status()
produto1.get_estoque()
produto1.get_ativo()
produto1.estoque_status()