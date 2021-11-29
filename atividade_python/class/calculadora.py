#Criar um classe chamada calculadora que faça soma, subtração, divisão e multiplicação. Crie um metodo para cada operação e simule o funcionamento
from time import sleep

class Calculadora:
    #construtor
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2
        

    def multiplicar(self):
        print(f"{self.__number1} X {self.__number2} : {self.__number1 * self.__number2}")

    def dividir(self):
        print(f"{self.__number1} / {self.__number2} : {self.__number1 / self.__number2}")

    def somar(self):
        print(f"{self.__number1} + {self.__number2} : {self.__number1 + self.__number2}")

    def subtrair(self):
        print(f"{self.__number1} - {self.__number2} : {self.__number1 - self.__number2}")


#instanciando e chamando o objeto
print('='*50)
while True:

    menu = input('''O que deseja fazer?
    [*] para multiplicar
    [/] para dividir
    [+] para somar
    [-] para subrair
    [0] para encerrar o programa.
    digite sua escolha: ''')

    print('\n')

    if menu == '0':
        print('-'*50)
        print("Programa sendo encerrado...")
        print('-'*50, '\n')
        sleep(0.7)
        break

    elif menu != '*' and menu != '/' and menu != '+' and menu != '-':

        print('=' * 50)
        print("escolha invalida tente novamente!")

    else:
        print('='*50)
        n1 = float(input("digite o primeiro numero: "))
        n2 = float(input("digite o segundo numero: "))
        request = Calculadora(n1, n2)

        if menu == '*':
            request.multiplicar()

        elif menu == '/':
            request.dividir()

        elif menu == '+':
            request.somar()

        elif menu == '-':
            request.subtrair()

    print('='*50 + '\n')
 