nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
nota3 = float(input('digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print("parabens voce tirou 10")
elif media >= 7 and media <10:
    print("voce foi aprovado")
elif media < 7 and media >= 5:
    print("voce esta de recuperacao")
elif media < 5 and media > 0:
    print("voce foi reprovado")
else:
    print("[ERROR], valor invalido")