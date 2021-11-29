a = float(input("digite o primeiro lado: "))
b = float(input("digite o segundo lado: "))
c = float(input("digite o terceiro lado: "))

if a == b == c:
    print("o triangulo e equilatero")

elif a != b != c and a != c :
    print("o triangulo e escaleno")

else:
    print("o triangulo e isosceles")