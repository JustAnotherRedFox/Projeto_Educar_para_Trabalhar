# classe
# Sintaxe

# marca, memoria, placa de video
class Computador:
    # construtor
    def __init__(self, marca, memoria, placa):  
        self.marca = marca
        self.memoria = memoria
        self.placa = placa

    def Ligar(self):
        print('Estou ligando..')

    def Desligar(self):
        print('Estou desligando..')

    def ExibirInformacoes(self):
        print(self.marca, self.memoria, self.placa)

    pass

computador1 = Computador('Asus', '8GB', 'Nvidia')
computador2 = Computador('Dell', '10GB', 'Geforce')
computador3 = Computador('Ace', '16GB', 'ATM')

computador2.Ligar()
computador2.ExibirInformacoes()
computador2.Desligar()

