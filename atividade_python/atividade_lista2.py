#Faça um programa que leia um vetor vet de 20 posições. O programa deve gerar, a partir do vetor lido, um outro vetor pos que contenha apenas os valores inteiros positivos de vet.
vet = [0] * 6
pos = []

for count in range(len(vet)):
    vet[count] = int(input("digite um numero: "))

    if vet[count] > 0:
        pos.append(vet[count])
    
print(f"o vetor e: {vet}")
print(f"os valores inteiros possitivos sao: {pos}")