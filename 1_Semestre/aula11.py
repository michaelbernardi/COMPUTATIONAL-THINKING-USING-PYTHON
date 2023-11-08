#para cada numero de 0 a 4, imprima a soma dos anteriores a ele (positivos)
'''
vamos escrever os números anteriores (positivos) a cada um e sua soma
0: nenhum -> 0
1: 0      -> 0
2: 1,0    -> 1
3: 2,1,0  -> 3
4: 3,2,1,0-> 6
'''
# soma=0
# # lembrando que range(5) = [0,1,2,3,4]
# for i in range(5): #para cada numero de 0 a 4
#     print(i)
#     soma+=i  #igual a soma=soma+i , ou seja, eu pego o que eu tinha e adiciono um número


#imprima apenas o quinto elemento da sequencia fibonacci
# fibonacci é a soma dos 2 números anteriores: 0,1,1,2,3,5,8,13,21
# anterior=0
# atual=1
# for i in range(3,6): #[3,4,5]
#     soma=anterior+atual
#     anterior=atual
#     atual=soma
#
# #este print só vai ser executado quando o for acabar
# print(atual)





## EXERCÍCIO:
# Faça um programa em loop que imprima esta imagem:
'''
*
**
***
****
*****
****
***
**
*
'''
# o range, se eu não disser o contrário, começa do 0
estrela="*"
#print(estrela*10)  #eu posso multiplicar strings

#
# for i in range(1,10):#[1,2,3,4,5,6,7,8,9] = 9 itens
#     #o primeiro i vale 1
#     if i<=5:
#         print(estrela*i)
#     else:
#         # quando i for 6, imprime 4 estrelas
#         # quando i for 7, imprime 3 estrelas
#         # quando i for 8, imprime 2 estrelas
#         # quando i for 9, imprime 1 estrela
#         print(estrela* (10-i) )
# #paramos na "metade" (quinto elemento)
#
## vamos fazer agora para que o tamanho seja variável
# n=int(input("Diga a quantidade de linhas (ímpar)"))
# # no nosso primeiro exemplo, n=9
# for i in range(1,n+1): #[1,2,3...,n] num total de N itens
#     if i<=((n+1)//2):
#         print(estrela * i)
#     else:
#         print(estrela * (n+1-i))





### WHILE  (enquanto) #damos a condição que tem que ser verdade para que continue

#para imprimir os números de 0 a 4
# numero=0
# while numero<=4: #não estou aumentando o número aqui. Apenas verifica se é verdade
#     print(numero)
#     # é necessário incrementar o contador. EU tenho que fazer o critério de parada
#     numero=numero+1  #ou numero+=1
# print("\nFora do loop")
# print(numero)
'''
no começo, numero=0
fazemos a verificação ( 0 <=4?) True
entramos no loop
    print(0)
    numero=1
fazemos a verificação ( 1 <=4?) True
entramos no loop
    print(1)
    numero=2
fazemos a verificação ( 2 <=4?) True
    print(2)
    numero=3
fazemos a verificação ( 3 <=4?) True
    print(3)
    numero=4
fazemos a verificação ( 4 <=4?) True
    print(4)
    numero=5
fazemos a verificação ( 5 <=4?) False
---> Fim do loop!

print(5)
'''


# num=int(input("Diga uma quantidade de linhas que seja um número ímpar positivo"))
#
# while num%2==0 or num<0: #testando se ele é par
#     if num%2==0 and num<0:
#         print("este número é par e negativo, digite novamente")
#     elif num%2==0:
#         print("este número é par, digite novamente")
#     else:
#         print("este número é negativo, tente novamente")
#
#     num = int(input("Diga uma quantidade de linhas que seja um número ímpar positivo"))
#
# for i in range(1,num+1): #[1,2,3...,n] num total de N itens
#     if i<=((num+1)//2):
#         print(estrela * i)
#     else:
#         print(estrela * (num+1-i))

## imprima a tabuada do número 5, entre 0 e 10, inclusive
# provavelmente é mais fácil/direto trabalhar com um for, quando temos uma condição pré-estabelecida ("entre 0 e 10")

numero_do_enunciado=5

for i in range(11): #[0 1 2 3 4 5 6 7 8 9 10] = 11 itens
    print(numero_do_enunciado*i)

#também é possível fazer com WHILE


## EXERCÍCIOS:

# 1) refaçam o exercício anterior, mas agora com while

# 2) Solicite dois número ao usuário, sendo que o segundo deverá ser obrigatoriamente maior que o primeiro

# 3) Solicitar um número obrigatoriamente inteiro positivo do usuário, e calcular seu fatorial

# 4) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
