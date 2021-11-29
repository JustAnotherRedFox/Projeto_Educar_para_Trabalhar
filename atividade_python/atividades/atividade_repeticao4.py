#4. Desenvolver um programa que leia um número determinado de valores
#e calcule e escreva a média aritmética dos valores lidos,
#a quantidade de valores positivos, a quantidade de valores negativos.

num = float(input("digite um numero para ser calculado, e 0 para parar o programa: "))

mediaS = countN = countP = 0

while True:

    mediaS = mediaS + num


    if num == 0:
        break

    if num < 0:
        countN = countN + 1

    elif num > 0:
        countP = countP + 1

    num = float(input("digite o proximo numero(ou '0' para encerrar o programa): "))

count = countP + countN
media = mediaS / count

print(f"a media dos {count} numeros digitados sera de: {media}")
print(f"e possui {countP} numeros positivos, e {countN} negativos")
