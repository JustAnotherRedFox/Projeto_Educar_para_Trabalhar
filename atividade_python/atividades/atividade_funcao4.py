#4. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def backward(num):

    numBackward = str(num)[::-1]
    return numBackward

number = int(input("digite um numero: "))

print(backward(number))