#Faça um programa que preencha por leitura um vetor de 10 posições, e depois vcs vão mostar esse vetor ao contrario..
import builtins


num = []
num_backwards = []

for count in range(10):

    num.append(input("digite um numero: "))

for count in range(9, -1, -1):
    num_backwards.append(num[count])

print(num_backwards)

print(num[::-1]) # pode-se usar as funcoes de string para reverter o array

print(list(reversed(num)))# pode-se usar uma funcao built-in do python para converter e reverter um array para uma lista