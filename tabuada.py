# 3 - Escreva um programa que exiba a tabuada do número digitado, onde o usuário possa digitar
# o inicio e o fim da tabuada.
n = int(input("Digite um numero da tabuada:"))
i = int(input("Digite o numero de inicio da tabuada:"))
f = int(input("Digite o numero final da tabuada:"))
for c in range(f - i + 1):
    print(f"{n} x {i} = {n * i} ")
    i += 1
