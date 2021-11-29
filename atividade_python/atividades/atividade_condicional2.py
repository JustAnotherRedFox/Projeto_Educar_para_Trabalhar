salario = float(input("digite seu salario: "))
tempo_servico = float(input("digite o tempo de servico: "))

bonus = 0

if tempo_servico >= 5:
    bonus = salario + (salario * (20/100))

elif tempo_servico < 5 and tempo_servico > 0:
    bonus = salario + (salario * (10/100))

else:
    print('valor invalido tente novamente!')

print(f"o bonus sera de R${bonus}")