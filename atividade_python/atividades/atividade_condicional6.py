a = float(input("digite um numero: "))
b = float(input("digite outro numero: "))
c = float(input("digite um outro numero: "))

maior = a
menor = a
medio = a

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

if a != maior and a != menor:
    medio = a
elif b != maior and b != menor:
    medio = b
else:
    medio = c

print(f"{maior} -> {medio} -> {menor}")
