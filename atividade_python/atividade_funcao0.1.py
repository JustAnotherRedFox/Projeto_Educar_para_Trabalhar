#Escreva uma função para calcular se um dado inteiro é par ou ímpar.
def par_impar(request):
    response = ''

    if request % 2 == 0:
        response = "o numero digitado e par."
        #tambem e possivel somente usar: return 'o numero digitado e par'

    else:
        response = "o numero digitado e impar"
        #tambem e possivel somente usar: return 'o numero digitado e impar'

    return response
    #se utilzado o return da maneira acima nem a variavel nem este return seriam necessarios


num = int(input("digite um numero para saber se e par ou impar: "))
print(par_impar(num))