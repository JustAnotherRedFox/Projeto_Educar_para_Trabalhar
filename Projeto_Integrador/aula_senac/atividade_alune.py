nota1 = float(1)
nota2 = float(2)
nota3 = float(3)

media = (nota1 + nota2 + nota3) / 3

if (media < 5):
    print(f"reprovado, {media} ")
elif (media >= 5 and media < 7):
    print(f"recuperacao, {media} ")
elif (media >= 7 and media <= 10):
    print(f"aprovado, {media}")
else:
    print(f"[ERROR], {media}")
