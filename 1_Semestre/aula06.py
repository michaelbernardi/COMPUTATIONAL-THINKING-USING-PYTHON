# Exercício:
'''
utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
seus respectivos nomes, e diga:
1) a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja
 um número negativo
2) quantas vezes a pessoa mais velha é mais velha que a mais nova,
limitando a resposta a 2 casas decimais
3) para cada pessoa, diga:
a) se ela for maior de idade, há quanto tempo ela fez 18 anos
    E quanto tempo falta para se aposentar
(assumindo que a idade de aposentadoria é 75 anos);
b) se ela for menor de idade, quantos anos faltam para ela fazer 18 anos
    E se ela ainda é criança (menor de 12 anos) ou já é adolescente (maior ou igual a 12 anos)
'''

nome_colega = input("Diga o nome do seu amigo")
nome_usuario = input("Diga o seu nome")

#lembrando que só pode fazer isto se tiver certeza que o número digitado pelo usuário vai ser um inteiro
#para garantir, pode colocar float(input)
idade_colega = int(input(f"Diga idade do {nome_colega}: "))
idade_usuario = int(input("Diga a sua idade{}: ".format(nome_usuario)))

# 1) a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja
#  um número negativo
print()
print(" ITEM 1")
## comparadoções retornam uma variável bool(lógica)
## else é TUDO O QUE NÃO ESTÁ ESCRITO no if
## comparação de igualdade é ==

#diferenca_de_idade = idade_colega>idade_usuario <- True ou False
#opção 1
print("opção 1")
if idade_colega>idade_usuario: #entra no if quando o colega é mais velho
    diferenca_de_idade = idade_colega - idade_usuario
    print(f"{nome_colega} tem idade superior a {diferenca_de_idade} "
          f"em relacao a sua,{nome_usuario}")
else:  #else não precisa de condição
    print(f"Você, {nome_usuario} tem idade superior a {idade_usuario - idade_colega} "
          f"em relacao a{nome_colega}")

#opção 2
print("opção 2")
if idade_usuario>idade_colega:
    print(f"Você, {nome_usuario} tem idade superior a { idade_usuario- idade_colega} "
          f"em relacao a{nome_colega}")
else:
    diferenca_de_idade_2 = idade_colega - idade_usuario
    print(f"{nome_colega} tem idade superior a {diferenca_de_idade_2} "
          f"em relacao a sua,{nome_usuario}")

#opção 3
print("opção 3")
diferenca_de_idade_3 = idade_colega - idade_usuario

if diferenca_de_idade_3>0: #colega é mais velho
    print(f"{nome_colega} tem idade superior a {diferenca_de_idade_3} "
          f"em relacao a sua,{nome_usuario}")

else: # você é mais velho OU vocês tem a mesma idade => o colega NÃO é mais velho
    diferenca_de_idade_3*=(-1)  #é equivalente a: diferenca_de_idade_3 = diferenca_de_idade_3 * (-1)
    print(f"Você, {nome_usuario} tem idade superior a {diferenca_de_idade_3} "
          f"em relacao a{nome_colega}")


#2) quantas vezes a pessoa mais velha é mais velha que a mais nova,
# limitando a resposta a 2 casas decimais
print()
print(" ITEM 2")
#opção 1
print("opção 1")
diferenca_de_idade_3 = idade_colega - idade_usuario
if diferenca_de_idade_3 > 0:  # colega é mais velho
    vezes_mais_velho = idade_colega/idade_usuario  #o resultado de uma divisão em python é sempre um float (4/2 = 2.0)
    print(f"O {nome_colega} é {vezes_mais_velho:.2f} vezes mais velho que voce,{nome_usuario}")

else:  # você é mais velho OU vocês tem a mesma idade => o colega NÃO é mais velho
    vezes_mais_velho = idade_usuario / idade_colega
    print(f"Voce,{nome_usuario} é {vezes_mais_velho:.2f} vezes mais velho que {nome_colega}")

#opção 2 - sem utilizar a subtração
print("opção 2")

if idade_colega > idade_usuario:  # colega é mais velho
    vezes_mais_velho = idade_colega/idade_usuario  #o resultado de uma divisão em python é sempre um float (4/2 = 2.0)
    print(f"O {nome_colega} é {vezes_mais_velho:.2f} vezes mais velho que voce,{nome_usuario}")

else:  # você é mais velho OU vocês tem a mesma idade => o colega NÃO é mais velho
    vezes_mais_velho = idade_usuario / idade_colega
    print(f"Voce,{nome_usuario} é {vezes_mais_velho:.2f} vezes mais velho que {nome_colega}")
#
# 3) para cada pessoa, diga:
# a) se ela for maior de idade, há quanto tempo ela fez 18 anos
#     E quanto tempo falta para se aposentar
# (assumindo que a idade de aposentadoria é 75 anos);
# b) se ela for menor de idade, quantos anos faltam para ela fazer 18 anos
#     E se ela ainda é criança (menor de 12 anos) ou já é adolescente (maior ou igual a 12 anos)

## tratamento para o usuário
if idade_usuario>=18:
    quanto_tempo_fez_18=idade_usuario-18
    tempo_para_se_aposentar=75 - idade_usuario
    print("{} fez 18 anos há {} anos".format(nome_usuario,quanto_tempo_fez_18))
    print("Faltam {} anos para {} se aposentar".format(tempo_para_se_aposentar,nome_usuario))

else: #usuario tem menos de 18 anos
    tempo_para_fazer_18=18-idade_usuario
    print(f"Faltam {tempo_para_fazer_18} anos para {nome_usuario} fazer 18 anos")
    #dentro de um if ou de um else, eu posso ter outro il/else
    if idade_usuario<12:
        print(f"{nome_usuario} é uma crinça")
    else: # o usuário tem menos de 18 e mais de ou exatamente 12 anos, ou seja 12<=idade_usuario<18
        print(f"{nome_usuario} é um adolescente")

### não se esqueçam de criar exemplos para todos os casos possíveis do seu programa!!



## tratamento para o colega
if idade_colega>=18:
    quanto_tempo_fez_18=idade_colega-18
    tempo_para_se_aposentar=75 - idade_colega
    print("{} fez 18 anos há {} anos".format(nome_colega,quanto_tempo_fez_18))
    print("Faltam {} anos para {} se aposentar".format(tempo_para_se_aposentar,nome_colega))

else:# usuario tem menos de 18 anos
    tempo_para_fazer_18=18-idade_colega
    print(f"Faltam {tempo_para_fazer_18} anos para {nome_colega} fazer 18 anos")
    #dentro de um if ou de um else, eu posso ter outro il/else
    if idade_colega<12:
        print(f"{nome_colega} é uma crinça")
    else: # o usuário tem menos de 18 e mais de ou exatamente 12 anos, ou seja 12<=idade_usuario<18
        print(f"{nome_colega} é um adolescente")




print('opcao3')
diferenca_idade_3 = idade_colega - idade_usuario
if diferenca_idade_3 > 0: #colega é mais velho, faz a diferenca e compara com 0
    print(f"{nome_colega} é {diferenca_idade_3} anos mais velho do que {nome_usuario}")
else: #vc é mais velho
    #opçao 1:
    diferenca_idade_3 *= (-1)  # compactado - é quivalente a: diferencade idade 3 - diferenca de idade3(x-)
    print(f"{nome_usuario} é {diferenca_idade_3} anos mais velho do que {nome_colega}")
    #opçao 2
    print(f"{nome_usuario} é {idade_usuario-idade_colega} anos mais velho do que {nome_colega}")
    #opçao 3
    diferenca_idade_invertida=idade_usuario-idade_colega
    print(f"{nome_usuario} é {diferenca_idade_invertida} anos mais velho do que {nome_colega}")


#EXERCÍCIO

'''
utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
seus respectivos nomes, e diga, colocando os nomes nas respostas:
1) se seus nomes possuem a mesma quantidade de letras
2) quantos porcento a idade do mais velho representa da idade do mais novo,
limitando a resposta a 1 casa decimal E 
a) se a pessoa mais velha é maior de idade
b) se a pessoa mais nova é uma criança (possui menos de 12 anos)
3) para cada pessoa, diga:
a) se ela for maior de idade, se ela já se aposentou OU quanto tempo falta para se aposentar
(assumindo que a idade de aposentadoria é 75 anos);
b) se ela for menor de idade, qual sua idade em meses

OBS: criem casos de teste para todas as possibilidades que vocês identificarem
'''