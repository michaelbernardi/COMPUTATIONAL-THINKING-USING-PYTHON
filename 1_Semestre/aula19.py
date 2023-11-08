## CORREÇÃO DA PROVA
'''Utilizando apenas os conceitos que foram ensinados nesta matéria até aqui, faça um programa que:'''

#1)[1,5pt] Crie uma função que receba um número como parâmetro e
# simplesmente imprima este número com apenas 3 casas decimais e com o símbolo de número ordinal (º) após ele

# def numero_ordinal(n):
#     print(f"{n:.3f}º")
    # a princípio não vai causar erro você colocar return n ;
    # mas não foi pedido pela questão, então o melhor é não colocar
#numero_ordinal(5.69846985)

#2) [3pts] Crie uma função que receba um parâmetro chamado 'operacao',
# e depois receba quantos parâmetros numéricos o usuário queira digitar.
# A operação poderá ser uma das 2: subtração ou divisão
# A função deverá retornar apenas o resultado da operação entregue como parâmetro
# Obs: esta função deverá ser devidamente documentada, explicando o que ela realiza,
# quais são seus parâmetros, seu retorno e quais seus tipos

#opção utlizando índices de lista
# def operacoes(*args,operacao): #[2,4,8]
#     total=args[0] #args[0]=2
#     if operacao=="subtração":
#         for i in range(1,len(args)): #len é o tamanho da lista
#             total-=args[i]
#     elif operacao=="divisão":
#         for i in range(1,len(args)):
#             total/=args[i]
#     else:print("Opção inválida!")
#     return total

#opção sem utilizar índices de lista
# def operacoes(*args,operacao):
#     '''
#     Função que recebe a operação desejada e os números para realizar esta operação
#     :param args: números (int ou float) que serão utilizados na operação
#     :param operacao: "subtração" ou "divisão". Operação a ser realizada com os números
#     :return: Número com o resultado da operação
#     '''
#     if operacao=="divisão":
#         resposta=1
#         for i in args:
#             resposta/=i #resposta=respsota/i
#         return resposta
#     elif operacao=="subtração":
#         resposta=0
#         for i in args:
#             resposta-=i #resposta=resposta-i
#         return resposta
#     else:return "Resposta inválida"

#resultado_operacao=operacoes(2,4,8,operacao="divisão") #como na definição eu coloquei args primeiro, para o python saber que eu acabei de digitar os args, eu chamo o "operacao" pelo nome



#3) [2pts] Crie uma função sem parâmetros, que solicite ao usuário um número necessariamente ímpar,
# realize a verificação e force para que o número seja ímpar, e retorne este número

# def solicita_impar():
#     while True:
#         n=float(input("Diga um número ímpar"))
#         if n%2!=0: return n
#         else:
#             print("Você não digitou um número ímpar")
#

# def solicita_impar():
#     n = float(input("Diga um número ímpar"))
#     while n%2==0:
#         print("Você não digitou um número ímpar")
#         n = float(input("Diga um número ímpar"))
#     return n



#4)a) [1,5pt] Primeiro, solicite uma palavra ao usuário e force para que seja uma das 2 operações da questão 2

# def solicita_operacao():
#     while True:
#         operacao=input("Escolha uma das duas operações: 'divisão' ou 'subtração': ")
#         if operacao== "subtração" or operacao=="divisão":return operacao
#         print("Você escolheu uma opção inválida!")

#b) [2pts] Depois, crie uma função que invoque a função da questão 3 (quantas vezes forem necessárias),
# e entregue seus retornos, juntamente com a operação da letra 'a)' para a função da questão 2).
# Esta função deverá imprimir o resultado utilizando a questão 1 E retornar o valor

# def questao_4():
#     q3=solicita_impar()
#     #aqui, podem ser feitas outras lógicas para aceitar mais números, porém 1 já seria suficiente
#     operacao=solicita_operacao()
#     resultado=operacoes(q3, operacao=operacao)
#     numero_ordinal(resultado)
#     return resultado

#resultado_final=questao_4()
#print("Retorno da função questão 4:",resultado_final)


def questao4_v2(quantidade):
    args=[]
    for i in range(quantidade):
        args.append(solicita_impar())
    operacao = solicita_operacao()
    resultado = operacoes(args, operacao=operacao)
    numero_ordinal(resultado)
    return resultado

# ---------------------------------------------------------------------------------------------
# IMPORT
# trazer para a memória uma biblioteca/funções de um arquivo que você criou
## é costume universal colocar todos os imports no começo do programa, antes de qualquer linha de código

## import completo (trago todas as funções da biblioteca para a memória)
### primeira forma:
import math as m #ou posso renomear a biblioteca

# para utilizar, chamamos biblioteca.função
# print(m.sqrt(4))
# print(m.pi)

### segunda forma:
from math import *

#para utilizar, chamamos apenas a função
# print(pi)
# print(sqrt(4))

## import parcial (escolhemos algumas das funções da biblioteca para importarmos)
from math import sqrt,cos,e,pi #posso ter vários

#para utilizar, eu chamo direto a função
# print(sqrt(4))
# print(pi)


### importando de um arquivo que você criou (que esteja na mesma pasta)
import utilidades as ut
ut.numero_ordinal(5.8456845845)

from utilidades import numero_ordinal as no
no(5.9842698)

## colocando as funções da prova em um arquivo e importando
import utilidades as ut
def questao_4():
    q3=ut.solicita_impar()
    #aqui, podem ser feitas outras lógicas para aceitar mais números, porém 1 já seria suficiente
    operacao=ut.solicita_operacao()
    resultado=ut.operacoes(q3, operacao=operacao)
    ut.numero_ordinal(resultado)
    return resultado

resultado_final=questao_4()
print("Retorno da função questão 4:",resultado_final)