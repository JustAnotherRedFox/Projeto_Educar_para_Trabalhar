print("escolha um numero para mostrar o dia da semana correspondente:")
print("1-domingo, 2-segunda, 3-terca, 4-quarta, 5-quinta, 6-sexta, 7-sabado")
num = int(input("digite o numero escolhido: "))

if num == 1:
    print('o dia escolhido e Domingo')
elif num == 2:
    print('o dia escolhido e segunda')
elif num == 3:
    print('o dia escolhido e terca')
elif num == 4:
    print('o dia escolhido e quarta')
elif num == 5:
    print('o dia escolhido e quinta')
elif num == 6:
    print('o dia escolhido e sexta')
elif num == 7:
    print('o dia escolhido e sabado')
else:
    print(f"voce escolheu {num}, este e um numero nao listado, tente novamente")