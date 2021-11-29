#1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(n1, n2, n3):
    return n1 + n2 + n3

#num1 = float(input("digite um numero: "))
#num2 = float(input("digite outro numero: "))
#num3 = float(input("digite um outro numero: "))

num = []

for count in range(0, 3):
    num.append(int(input("digite um numero: ")))

print("a soma dos numeros digitados e: ", soma(num[0], num[1], num[2]))