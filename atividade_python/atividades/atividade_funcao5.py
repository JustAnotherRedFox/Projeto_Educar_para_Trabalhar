#5. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def numCount(n):
    #lengthNum = len(str(n))
    return len(str(n))

number = int(input("digite um numero: "))

print(f"o numero {number} possui: {numCount(number)} digitos")