#3. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, 
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    taxaImposto = custo + (custo * (taxaImposto/100))
    return taxaImposto


taxa = float(input("digite a porcentagem de imposto: "))
custo = float(input("digite o custo: "))

taxaMaisImposto = somaImposto(taxa, custo)
print(f"a venda foi de R${custo:.2f} e com um Imposto de {taxa:.0f}%, o valor final sera de R${taxaMaisImposto}")