#3. Desenvolva um programa que receba dez números do usuário e imprima a metade de cada número.

for count in range(10):
    num = float(input("digite um numero a ser dividido: "))
    half = num / 2
    
    print(half)