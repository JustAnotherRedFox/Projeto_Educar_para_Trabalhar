
time1 = str(input("digite o nome do primeiro time: "))
time2 = str(input("digite o nome do segundo time: "))

gols_time1 = int(input(f"quantos gols {time1} marcou? "))
gols_time2 = int(input(f"quantos gols {time2} marcou? "))

if gols_time1 > gols_time2:
    print(f"{time1} venceu!")
elif gols_time2 > gols_time1:
    print(f"{time2} venceu!")
elif gols_time1 == gols_time2:
    print("empate")
else:
    print("ERRO, tente novamente")