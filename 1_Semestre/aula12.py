## EXERCÍCIOS:


## imprima a tabuada do número 5, entre 0 e 10, inclusive
# 1) refaçam o exercício anterior, mas agora com while
#começamos criando nosso contador
# i=0
# numero_do_enunciado=5
# while i<=10:
#     print(i*numero_do_enunciado)
#     i+=1


# 2) Solicite dois número ao usuário,
# sendo que o segundo deverá ser obrigatoriamente
# maior que o primeiro

# n1=float(input("Diga um número "))
# n2=float(input("Diga um número maior que o anterior "))
#
# while n2<=n1:
#     print("o segundo número não é maior que o primeiro")
#     n2 = float(input(f"Diga um número maior que {n1} "))


# 3) Solicitar um número obrigatoriamente inteiro positivo
# do usuário,
# e calcular seu fatorial

##fatorial de um número é a multiplicação de todos os que vieram antes dele (sem o 0)
## ex: 3! = 3*2*1 = 6
## ex: 0! = 1
#n=float(input("Digite um número inteiro positivo"))

#para saber se é inteiro:
##  podemos comparar ele com o int() dele
##  podemos comparar ele com a divisão inteira dele por 1 (que é a forma manual de fazer int() )

# #pra saber se é positivo: >=0
# while n<0 or int(n)!=n:
#     print("Seu número não atendeu às condições")
#     n = float(input("Digite um número inteiro positivo"))
#
# n=int(n) #podemos fazer isto porque já garantimos que é inteiro
# # e temos que fazer porque o range não aceita float
# # ex:n=5
# fatorial=1
#
# for i in range(1,n+1):
#     print("a")
#     fatorial*=i
# print(f"O fatorial de {n} é {fatorial}")
# #
# fatorial=1
# for i in range(n,0,-1):
#     print("a")
#     fatorial*=i
# print(f"O fatorial de {n} é {fatorial}")

# print(n)
# print(type(n))
# print()
# n=float(n)
# print(n)
# print(type(n))
# print()
# n2=int(n)
# print(n2)
# print(type(n2))
# print(n2==n)

##print(float(n)//1==float(n))


### CONTINUE, PASS E BREAK
# break = quebra o loop-> sair do loop
# pass = passe (não faz nada)
# continue = avance o loop (ou seja, volta pro topo do loop). Não faz o que estiver abaixo dele no loop
#           No caso do for, avança o contador

# i=0
# while i<=5:
#     i += 1
#     if i==3:continue
#     print(i)

for i in range(5):
    if i==3:continue
    print(i)

## EXERCÍCIOS
# 1) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 2) imprima a tabuada do número 5, de 0 e 10, inclusive.
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 3) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o segundo número

