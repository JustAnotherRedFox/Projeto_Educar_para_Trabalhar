a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
c = int(input("digite o terceiro numero: "))

maior = a
menor = a

if maior > b and maior > c:
    maior = a
else:
    if b > c:
       maior = b
    else:
        maior = c

if menor < b and menor < c:
    menor = a
else:
    if b < c:
        menor = b
    else:
        menor = c

print(f"o numero {maior} e o maior e o numero {menor} o menor")