produto1 = float(input("digite o preco do produto 1: "))
produto2 = float(input("digite o preco do produto 2: "))
produto3 = float(input("digite o preco do produto 3: "))

menor = produto3
menor_nome = ''

if produto1 < menor:
    menor = produto1
    menor_nome = 'produto1'
    if produto2 < menor:
        menor = produto2
        menor_nome = 'produto2'
elif produto2 < menor:
    menor = produto2
    menor_nome = 'produto2'

print(f"voce deve comprar o {menor_nome}")
