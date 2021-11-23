#2. Faça um programa, com uma função que necessite de um argumento. A função retornao valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def valor(num):
    if num > 0:
        return 'positivo'

    elif num <= 0:
        return 'negativo'

n = float(input("digite um numero: "))

print(valor(n))