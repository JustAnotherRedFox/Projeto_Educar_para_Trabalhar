# perguntar o genero e parar qunado digitar 'FIM' e quntar vezer digitou f ou m

gender = str(input("digite o genero[F ou M]: "))
countM = countF = 0

while True:
    if gender == 'M':
        countM = countM + 1
    elif gender == 'F':
        countF = countF + 1
    elif gender == 'FIM':
        print("foi contado {} Mulheres e {} Homems".format(countF, countM))
        break
    else:
        print("genero invalido, tente novamente.")

    gender = str(input("digite o genero[F ou M]: "))