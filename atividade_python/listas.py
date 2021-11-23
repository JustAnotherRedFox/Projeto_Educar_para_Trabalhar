#lista = ['joao', 23, 'jovem', 50.3, True]

#print(f"nome: {lista[0]}, idade: {lista[1]}, era:{lista[2]}, peso: {lista[3]}, homem: {lista[4]}")

cadastroRequest = ['nome', 'ano de nascimento', 'peso', 'genero']
cadastroResponse = ['', '', '', '']
count = 0

while True:

    cadastroResponse[count] = str(input(f"digite o {cadastroRequest[count]} do cadastrado: "))
    if count == 1:
        cadastroResponse[count] = str(abs(int(cadastroResponse[count]) - 2021))
    count += 1

    if count == 4:
        print(f"cadastrado: {cadastroResponse[0]}, idade: {cadastroResponse[1]}, peso: {cadastroResponse[2]}, genero: {cadastroResponse[3]}")
        count = 0

    elif cadastroResponse[count - 1] == '':
        break

#para se colocar casas decimais usa-se :.2f, para duas casas decimais