#5. Desenvolva um programa que efetue a soma de todos os números ímpares
#que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

count = 0

for inpar in range(1, 500, 2):
    if inpar % 3 == 0:
        count = count + inpar

print(f"a soma dos numeros inpares e {count}")