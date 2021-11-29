#7. Escreva um programa que receba vários números
#e ao final imprima o maior número digitado. O algoritmo acaba quando se digita –9999; 

num = float(input("digite um numero: "))

maior = count = 0

while True:
    if num == -9999:
        break
    
    else:
        count = count + 1
        num = float(input("digite outro numero(ou digite -9999 para encerrar): "))

        if count <= 1:
            maior = num

        else:
            if num > maior:
                maior = num

print(f"o maior numero digitado foi {maior}")
