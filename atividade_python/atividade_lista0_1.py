notas = []

notas.append(eval(input('digite a primeira nota: ')))
notas.append(eval(input('digite a segunda nota: ')))
notas.append(eval(input('digite a terceira nota: ')))

print(notas)

print(notas[0])
print(notas[1])
print(notas[2])

print(len(notas)) #retorna  a quantidade de elementos em um array, lista, ...
#para selecionar um valor do final para o comeco usa-se numeros negativos ex.: -1 = ultimo, -2 = penultimo ...