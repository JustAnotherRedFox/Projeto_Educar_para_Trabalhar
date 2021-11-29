ano_nasc = int(input("digite seu ano de nascimento: "))
ano_atual = int(input("digite o ano atual: "))

age = ano_atual - ano_nasc

if age > 18 and age < 100:
    print('voce pode votar')
elif age < 18 and age > 0:
    print('voce nao pode votar')
else:
    print('idade invalida')