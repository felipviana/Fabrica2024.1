#Fazer um for, while, e duas funções, uma com retorno e outra sem

def parOuImpar(x):
    if x%2 == 0:
        return "É par"
    else :
        return "É impar"
def funcSemRetorno(x,y):
    soma = x + y

lista = [1,2,3,4,5]

count = 1
for numeros in lista:
    print(f"O {count}° numero da lista que é {numeros} {parOuImpar(numeros)}")
    count +=1

count = 1
variavel = 0
while(variavel <len(lista)):
    print(f"O {count}° numero da lista que é {lista[variavel]} é {parOuImpar(lista[variavel])}")
    variavel +=1
    count +=1

