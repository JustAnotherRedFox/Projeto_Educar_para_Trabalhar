#6. Escreva um programa que leia um valor inicial A e imprima a seqüência de
#valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

n = int(input("digite o valor inicial: "))

count = num = n

print(f"{n}!")
while count != 1:
    count = count - 1
    print('x')
    print(count)
    
    n = n * count
    
print(f" = {n}")