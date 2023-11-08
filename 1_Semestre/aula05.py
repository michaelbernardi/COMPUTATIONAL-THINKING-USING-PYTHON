#exercício da aula anterior
## calcular o menor número de notas necessárias para pagar
# este custo mensal

#ainda falta descobrir o quanto o troco importa
# completar o problema utilizando moedas para chegar ao valor exato

# custo_mensal = 266.66
# quanto_falta = custo_mensal%200
# #[...]
#
# #substitui o valor do "quanto_falta"
# quanto_falta = quanto_falta%10
# quanto_falta = quanto_falta-10
# quanto_falta-= 10
#print(266.66%200) # =266.66 - (266.66//200 * 200)

# ESTRUTURAS CONDICIONAIS - simples (if) - "se"

# if 1>0:
#     #dentro do if
#     print("1>0")
#     print("blablabla")
#     print("outra linha")
#     contador = 1
#     if 2==0:
#         print(contador)
#         contador+=1
#         print(contador)
#     contador+=1
#     #numero1=input("qualquer coisa")
#     print(contador)
# #estou fora do if

# minha_idade=30
# idade_colega=40
#if aceita composições
# if minha_idade>idade_colega:
#     print("você é mais velho ")
#
# # else = Todo o resto
# else:  #você não escreve condições
#     print("você não é mais velho")

# utilizando apenas if e else, faça um programa que diga
# a diferença de idade entre você e um colega, e seus nomes,
# sem que a resposta seja um número negativo
#
# seu_nome = input("Diga seu nome: ")
# sua_idade = float(input("Olá,{}\nDiga a sua idade ".format(seu_nome)))
#
#
# nome_do_colega = input("Diga o nome do seu colega: ")
# idade_colega = float(input("Olá {}, amigo de {}\nDiga a idade de um colega ".\
#                      format(nome_do_colega,seu_nome)))
# ## primeira forma de fazer
# diferenca_de_idade=sua_idade-idade_colega
#
# if diferenca_de_idade<0:
#     diferenca_de_idade *= -1
#     print(diferenca_de_idade)
# else:
#     print(diferenca_de_idade)
#
# ## segunda forma de fazer
# if sua_idade>idade_colega:
#     print(sua_idade-idade_colega)
# else:
#     print(idade_colega-sua_idade)
#
# # terceira forma
# if sua_idade-idade_colega>0:
#     print(sua_idade-idade_colega)
# else:
#     print(idade_colega - sua_idade)
#     #ou
#     print((sua_idade-idade_colega)*(-1))
#

#cada else "fecha" um if

# variavel = 2
#
# if variavel==2:
#     variavel+=1
#     print(variavel)
#
# print(variavel)
#
# if variavel==2:
#     variavel+=2
#
# print(variavel)


