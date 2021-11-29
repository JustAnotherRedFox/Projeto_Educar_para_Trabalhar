def calculoMedia(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def aprovacao(media):
    if media >= 7 and media <= 10:
        print("aprovado")

    elif media < 7 and media > 0:
        print("reprovado")
    
    else:
        print("[error] numero imvalido")

n = 0

while n < 5:
    nota1 = float(input("digite a nota 1: "))
    nota2 = float(input("digite a nota 2: "))
    nota3 = float(input("digite a nota 3: "))

    media = calculoMedia(nota1, nota2, nota3)
    print(f"a media e {media}")

    aprovacao(media)
    n = n + 1

