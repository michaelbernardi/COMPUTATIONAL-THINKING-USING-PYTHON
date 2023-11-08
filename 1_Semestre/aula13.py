## EXERCÍCIOS
# 1) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# quando o enunciado pede "a/o" soma, multiplicação, elemento, etc; quer dizer apenas o resultado final
## teria que imprimir todos, caso o enunciado pedisse todos os elementos, todas as somas, "até n-ésimo elemento", etc

## fazendo com o for primeiro
# ex: 3 -> 1+2+3=6
# soma=0
# for i in range(1,101):
#     soma+=i # é o mesmo que soma=soma+i
# print("A soma dos números inteiros positivos de 1 a 100 é {}".format(soma))
#
# ## fazendo com o while
# contador = 1
# soma_while = 0
# while contador<=100: #ou contador<101
#     soma_while+=contador
#     contador+=1
# print("A soma dos números inteiros positivos de 1 a 100 é {}".format(soma_while))
#
# ##caso quisesse todos:
# ### for
# soma=0
# for i in range(1,101):
#     soma+=i
#     print(f"A soma dos números inteiros positivos de 1 a {i} é {soma}")
#
# ### while
# contador = 1
# soma_while = 0
# while contador<=100: #ou contador<101
#     soma_while+=contador
#     print("A soma dos números inteiros positivos de 1 a {} é {}".format(contador, soma_while))
#     contador+=1
#



# 2) imprima a tabuada do número 5, de 0 e 10, inclusive.
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# while True:
#     n1 = float(input("Diga um número inteiro para início da tabuada"))
#     if n1==int(n1):break
#     else:
#         print("Você não digitou um número nas condições necessárias. Favor tente novamente")
#         continue
#
# while True:
#     n2 = float(input("Diga um número inteiro para o final da tabuada"))
#     if n2==int(n2):break
#     else:
#         print("Você não digitou um número nas condições necessárias. Favor tente novamente")
#         continue

# n1=float(input("Diga um número inteiro para início da tabuada"))
# while n1!=int(n1):
#     print("Você não digitou um número nas condições necessárias. Favor tente novamente")
#     n1 = float(input("Diga um número inteiro para início da tabuada"))
#
# n2 = float(input("Diga um número inteiro para o final da tabuada"))
# while n2 != int(n2):
#     print("Você não digitou um número nas condições necessárias. Favor tente novamente")
#     n2 = float(input("Diga um número inteiro para o final da tabuada"))
#
# n1=int(n1)  # 5
# n2=int(n2)  # 2
# #tabuada do número 5, de 0 e 10, inclusive.
# range(11)
# for i in range(n1,n2+1,1): #o range só aceita números inteiros
#     print(5*i)
## precebemos que n1 não pode ser maior que n2 nesta configuração
### temos 2 formas de resolver: OU travar para que n2 seja maior que n1
### OU fazer um if, e escrever o range de acordo

# EXERCÍCIO: fazer as duas opções


# 3) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número,
# faça a tabuada dele do 0 até o segundo número
'''
Ex:n1=3
n2=5
tabuada do 1, de 0 a 5;
tabuada do 2, de 0 a 5;
tabuada do 3, de 0 a 5'''

# n1=int(input("Diga o número que vai ser feita a tabuada"))
# n2=int(input("Diga até qual número esta tabuada vai ser feita"))
## temos que forçar a ser inteiro, pois o range só trabalha com números inteiros
### EXERCÍCIO: FORÇAR A SER INTEIRO
#
# # vamos começar com o que já fizemos: ex: tabuada do 5, de 0 a n2
# for i in range(n2+1):
#     print(i*5)
#
# #agora , vamos fazer um número variar de 1 a n1:
# for i in range(1,n1+1):
#     print(i)

n1=int(input("Diga o número que vai ser feita a tabuada"))
n2=int(input("Diga até qual número esta tabuada vai ser feita"))
# por fim, vamos juntar os loops
## ao juntar os loops, eu não posso ter o mesmo nome para o contador
## eu tenho que nomear o contador de forma diferente
# for i in range(1,n1+1):
#     print ("tabuada do ",i)
#     for j in range(n2+1): #todo este range do j vai ser executado para cada valor de i
#         print(f"{i}*{j}=",i*j) # é o mesmo que  print(f"{i}*{j}={i*j}")
#     print()

### agora, fazer com while
i=1
while i<=n1:
    j=0
    print("tabuada do ", i)
    while j<=n2:
        print(f"{i}*{j}=", i * j)
        j+=1
    i+=1
    print()
# lembrando que o while não altera o contador, então temos que manualmente incrementar E resetar

#EXERCÍCIOS:
# 1)No exemplo anterior, travar para que o número seja inteiro

# 2)imprima a tabuada do número 5, de 0 e 10, inclusive.
# # Depois, adapte o programa para receber dois números do usuário: o de início e o de fim

# for i in range(n1,n2+1,1): #o range só aceita números inteiros
#     print(5*i)
## precebemos que n1 não pode ser maior que n2 nesta configuração
### temos 2 formas de resolver: OU travar para que n2 seja maior que n1
### OU fazer um if, e escrever o range de acordo
# EXERCÍCIO: fazer as duas opções


# 3) faça um programa que imprima apenas os números pares no intervalo de n1 (inclusive) até n2 (exclusive)
# onde n1 e n2 são números dados pelo usuário, e deverão ser inteiros. Além disto, n2 deve ser maior que n1

# 4) faça um programa que , ao usuário digitar um número, obrigatoriamente inteiro, imprima os 20 números subsequentes
# Caso, após estes 20 número sejam negativos, dizer quanto falta para chegar a 0

# 5) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos