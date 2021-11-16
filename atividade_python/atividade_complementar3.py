nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))
peso1 = float(input('digite o primeiro peso do aluno: '))
peso2 = float(input('digite o segundo peso do aluno: '))

media_ponderada = (nota1 * peso1) + (nota2 * peso2) / (peso1 + peso2)
print(f"a media ponderada do aluno sera: {media_ponderada}")