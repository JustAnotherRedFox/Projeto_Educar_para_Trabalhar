valor_imprestimo = float(input("digite o valor do imprestimo: "))
parcelas = int(input("digite a quantidade de parcelas: "))
salario = float(input("digite o salario: "))

valor_parcelas = valor_imprestimo / parcelas

if valor_parcelas < (salario * (30/100)):
    print(f"o emprestimo esta aprovado, e sera no valor de R${valor_parcelas} em {parcelas} meses")

else:
    print("o valor excede 30% do seu salario, o emprestimo nao podera ser efetuado!")