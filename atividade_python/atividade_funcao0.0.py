#funcao sem retorno
def soma(a, b):
    result = a + b
    print(f"a soma e {result}")

#funcao com retorno
def soma2(a, b):
    result = a + b
    return result

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

soma(num1, num2)