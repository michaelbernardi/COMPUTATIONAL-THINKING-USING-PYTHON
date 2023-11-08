'''Utilizando apenas os conceitos que foram ensinados nesta matéria até aqui, faça um programa que:'''

# 1)
# a) [1pt] Solicite dois números ao usuário: n1 e n2.
# Estes números deverão ser inteiros e n1 deve ser menor que n2.
#
# print()
# print("-"*20)
# print("Questão 1")
#
# n1=float(input("Diga um número inteiro"))
# while n1//1!=n1:
#     print("Você não digitou um número inteiro")
#     n1 = float(input("Diga um número inteiro"))
#
# n2=float(input("Diga um outro número inteiro, maior que o primeiro"))
# while n2//1!=n2 or n2<=n1:
#     print("Você não digitou um número inteiro ou digitou um número maior ou igual ao primeiro")
#     n2 = float(input(f"Diga um outro número inteiro, maior que o {n1}"))
# n1=int(n1)
# n2=int(n2)
# # b) [1pt] Realize e imprima a soma de todos os números de n1 (exclusive) até n2 (inclusive)
# soma=0
# for i in range(n1+1,n2+1): #ex n1=5, n2=7: [6,7]. Soma=13
#     soma+=i
# print(f"A soma de todos os números de {n1} (exclusive) até {n2} (inclusive) é :",soma)
#
#
# # 2)
# # a) [1.5pt] Solicite dois números ao usuário: n1 e n2.
# # Estes números deverão ser negativos, inteiros e diferentes entre si.
# #
# print()
# print("-"*20)
# print("Questão 2")
# n1=float(input("Diga um número inteiro negativo"))
# while n1//1!=n1 or n1>=0:
#     print("Você não digitou um número inteiro negativo")
#     n1 = float(input("Diga um número inteiro negativo"))
#
# n2=float(input("Diga um número inteiro negativo diferente do primeiro"))
# while n2//1!=n2 or n2>=0 or n2==n1:
#     print("Você não digitou um número inteiro negativo diferente do primeiro")
#     n2 = float(input(f"Diga um número inteiro negativo diferente de {n1}"))
#
# n1=int(n1)
# n2=int(n2)
# # b) [1.5pt] Utiliando uma estrutura de loops (laços),
# # faça uma rotina que imprima os 6 números anterioes ao maior dos dois (entre n1 e n2),
# # e os 5 posteriores ao menor
#
# #ex: n1= -5 -> -6,-7,-8,-9,-10,-11
# #    n2= -8 -> -7,-6,-5,-4,-3
# if n1>n2: #6 numeros antes do n1, e 5 numeros depois do n2
#     for i in range(n1-1,n1-7,-1):
#         print(i)
#     print()
#     #o for reseta o 'i' automaticamente para a gente
#     # se fosse o while,teria que resetar manualmente o 'i'
#     for i in range(n2+1,n2+6):
#         print(i)
#
# #ex: n1=-9 -> -8,-7,-6,-5,-4
# #    n2=-4 -> -5,-6,-7,-8,-9,-10
# else: #n2 é o maior
#     for i in range(n2-1,n2-7,-1):
#         print(i)
#     print()
#     for i in range(n1+1,n1+6):
#         print(i)
#
#
#
#
# # 3) Solicite dois números ao usuário: n1 e n2.
# # a) [1.5pt] n1 deve ser ímpar e positivo; e n2 deve ser par e negativo.
# # enquanto o usuário digitar um número que não antenda a estas condições,
# # o programa deverá dizer exatamente qual característica do número não estava de acordo
# # com o que foi solicitado
# print()
# print("-"*20)
# print("Questão 3")
#
# n1=float(input("Diga um número ímpar positivo: "))
# while n1%2==0 or n1<0:
#     if n1%2==0 and n1<0:
#         print("Você digitou um número par e negativo")
#         n1 = float(input("Diga um número ímpar positivo: "))
#     elif n1%2==0:
#         print("Você digitou um número par.")
#         n1 = float(input("Diga um número ímpar positivo: "))
#     else:
#         print("Você digitou um número negativo")
#         n1 = float(input("Diga um número ímpar positivo: "))
#
# n2=float(input("Diga um número par negativo"))
# while n2%2!=0 or n2>=0:
#     if n2%2!=0 and n2>=0:
#         print("Você digitou um número ímpar positivo")
#         n2 = float(input("Diga um número par negativo"))
#
#     elif n2%2!=0:
#         print("Você digitou um número ímpar")
#         n2 = float(input("Diga um número par negativo"))
#     else:
#         print("Você digitou um número positivo")
#         n2 = float(input("Diga um número par negativo"))
#
#
# # b) [2pt] Caso algum dos dois (ou os dois) não sejam números inteiros,
# # diga qual dos dois possui a maior parte decimal
#
# if n1//1!=n1 or n2//1!=n2:
#     parte_decimal_n1=  n1 - (n1//1)
#     parte_decimal_n2 = n2 - (n2//1)
#     if parte_decimal_n1>parte_decimal_n2:
#         print(f"N1 ({n1}) possui maior parte decimal que {n2}")
#     elif parte_decimal_n1<parte_decimal_n2:
#         print(f"N2 ({n2}) possui maior parte decimal que {n1}")
#     else:
#         print(f"As partes decimais de {n1} e {n2} são iguais")
# else:
#     print("Os dois números são inteiros")
#



# 4) [1.5pt] Escreva aqui, em forma de comentário em bloco,
# um exemplo de input(s) e output(s) para cada questão anterior

'''
--------------------
Questão 1
Diga um número inteiro5
Diga um outro número inteiro, maior que o primeiro8
A soma de todos os números de 5 (exclusive) até 8 (inclusive) é : 21

--------------------
Questão 2
Diga um número inteiro negativo-5
Diga um número inteiro negativo diferente do primeiro-7
-6
-7
-8
-9
-10
-11

-6
-5
-4
-3
-2

--------------------
Questão 3
Diga um número ímpar positivo: 9
Diga um número par negativo-6
Os dois números são inteiros

Process finished with exit code 0

'''



#___________________________________________________________________________________________

#Corrigindo o exercício 5 da aula 13

# 5) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos

n=float(input("Diga um número inteiro entre 1 e 20"))
while n//1!=n or n<1 or n>20:
    print("Você digitou um número que não atende às condições")
    n = float(input("Diga um número inteiro entre 1 e 20"))
n=int(n)

i=1
maior_valor=float('-inf') #menor valor possível no python   #menor do que -999999999999999999999999999999999999999
menor_valor=float('inf')  #maior valor possível no python   #maior do que 99999999999999999999999999999999999999999
soma=0
media=0
n_neg=0
n_pos=0
while i<=n:
    n_temp=float(input(f"Diga o {i}º número de um total de {n}: "))

    soma+=n_temp
    media=soma/n

    if n_temp>=0: n_pos+=1
    else: n_neg+=1

    if n_temp>maior_valor: maior_valor=n_temp
    if n_temp<menor_valor: menor_valor=n_temp

    i+=1

print(f"O maior valor é {maior_valor}")
print(f"O menor valor é {menor_valor}")
print(f"A soma dos valores é {soma}")
print(f"a médida dos valores é {media}")
print(100*n_neg/n,"% dos valores foram negativos")
print(100*n_pos/n,"% dos valores foram positivos")
#for i in range(1,n+1):