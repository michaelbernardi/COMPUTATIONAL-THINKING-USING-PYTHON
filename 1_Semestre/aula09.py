## Exercícios

'''Exercícios:
1)	Solicite um número do usuário.
Diga a menor nota de real que é maior que este número.
Caso não exista, diga “Não existe nota de real maior do que este número”'''

# valores de notas de real
# 200,100,50,20,10,5,2
# ex: 70 R: 100
# temos 8 possibilidades:
# maior que 200, entre 200 e 100, entre 100 e 50,
# entre 50 e 20, entre 20 e 10, entre 10 e 5, entre 5 e 2,
# e menor que 2

#possíveis casos: 0,2,5,10,20,50,100,200,-50,500,500.947628, 0.574, 7.5874266
# if 0>numero:## ou poderia fazer if 2>numero>=0, e tratar o número negativo no else
#     print("Este número é negativo")
# elif 2>numero:
#     print("A menor nota maior que {} é a de 2 reais".format(numero))
# elif 5>numero>=2: #seria o mesmo que 5>numero and numero>2
#     print("A menor nota maior que {} é a de 5 reais".format(numero))
# elif 10>numero>=5:
#     print("A menor nota maior que {} é a de 10 reais".format(numero))
# elif 20>numero>=10:
#     print("A menor nota maior que {} é a de 20 reais".format(numero))
# elif 50>numero>=20:
#     print("A menor nota maior que {} é a de 50 reais".format(numero))
# elif 100>numero>=50:
#     print("A menor nota maior que {} é a de 100 reais".format(numero))
# elif 200>numero>=100:
#     print("A menor nota maior que {} é a de 200 reais".format(numero))
# elif 200<=numero: #é o mesmo que numero>=200
#     print("Não existe nota de real maior do que {}".format(numero))
# else:
#     pass

## exercício extra: repita o exercício anterior,
# desta vez começando com a comparação numero>=200

'''
2)	Solicite um número ao usuário.
Diga se este número é igual a 0.
Se não for, diga se ele é par ou ímpar'''
# temos 3 possibilidades: igual a 0, ser par !=0,ou ser ímpar
# testes: 0, 1, 2, -1, -2, 0.0, 0.5, 0.6, 2.1,2.2, -2.2
# if numero==0: #necessariamente o primeiro teste tem que ser este
#     print(f"O número digitado,{numero}, é 0")
# elif numero%2==0: #ele é par
#     print(f"O número digitado,{numero}, é par e diferente de 0")
# else:
#     print(f"O número digitado,{numero}, é impar e diferente de 0")

'''3)	Solicite 3 números ao usuário.
Diga o menor deles'''
# numero1=float(input("Favor digitar um número")) #float para não correr o risco de perder informação
# numero2=float(input("Favor digitar outro número")) #float para não correr o risco de perder informação
# numero3=float(input("Favor digitar mais um outro número")) #float para não correr o risco de perder informação
#
# #     20     10        15
# if numero3>numero1<numero2:
#     print("o numero 1 {} é o menor".format(numero1))
#
# #       30      10      20
# elif numero3>numero2<numero1: #é o mesmo que numero3>numero2 and numero1>numero2
#
#     print("o numero 2 {} é o menor".format(numero2))
#
# #       35      10      10.1
# elif numero2>numero3<numero1:
#     print("o numero 3 {} é o menor".format(numero3))
#
# elif numero3==numero2==numero1:
#     print(f"Todos são iguais, então podemos dizer que {numero1} é menor")
#
# # opção 1
# elif numero3==numero2>numero1:
#     print("o menor é o numero 1 {}".format(numero1))
# elif numero3 == numero2 < numero1:
#     print("os menores numeros são iguais ({}), e são os numeros 2 e 3" \
#           .format(numero3))
# ### é equivalente a:
# # opção 2
# elif numero3==numero2:
#     if numero3>numero1:
#         print("o menor é o numero 1 {}".format(numero1))
#     else: #numero3<numero1
#         print("os menores numeros são iguais ({}), e são os numeros 2 e 3"\
#               .format(numero3))
#

#
# else:
#     #provisoriamente
#     print("situação inicialmente inesperada")
#     print(numero1,numero2,numero3)


'''4)	Solicite ao usuário (separadamente) o mês do ano, e o dia atual.
 Diga em qual estação estamos
ex: 28 de março -> primeiro input = 3, segundo input = 28
Outono : De 22 de março a 21 de junho.
Inverno: De 22 de junho a 23 de setembro.
Primavera: De 24 de setembro a 21 de dezembro.
Verão: De 22 de dezembro a 21 de março.

similar ao das notas, só que agora cada mês tem mais condições
'''



## MATCH/CASE
# ele foi pensado para igualdades
'''
sintaxe:
match variável:
    case outra_variável:  #ele vai executar uma comparação DE IGUALDADE
        ação
    [...]
    case _:
        ação
'''
num=2

match num: # é uma comparação de igualdade
    case 0: #caso este número seja 0:
        print("o numero é 0") #faça isso
    case 1: #caso este número seja 1:
        print("o numero é 1")
    case 2: #caso este número seja 2:
        print("o número é 2")
    case _: #equivalente ao else (ou seja, se não for igual a nenhum acima)
        print(f"{num} é um número que não é 0,1 ou 2")

# é equivalente a:
if num==0:
    print("o numero é 0")
elif num==1:
    print("o numero é 1")
elif num==2:
    print("o numero é 2")
else:
    print(f"{num} é um número que não é 0,1 ou 2")

#exemplo de comparação de desigualdade no match/case

num=3

match num:
    case _ if num>0:
        print("o número é maior que 0")
#é quivalente a
if num>0:
    print("o número é maior que 0")







# https://codingbat.com/python