#Um programa que fale o nome de 5 times de futebol
import random
times = ["Atlético", "Bahia", "Botafogo", "Corinthias", "Cruzeiro", "Flamengo", "Fluminense", "Santos", "Vasco", "São Paulo"]
timesListados = []
timeTemporario = ""
print("Times gerados aleatoriamente:\n")
for i in range(10):
    variavel = 0
    while variavel == 0:
        timeTemporario = random.choice(times)
        if timeTemporario in timesListados:
            variavel = 0
        elif (timeTemporario in timesListados) == False:
            timesListados.append(timeTemporario)
            variavel = 1

print(timesListados)