## CORREÇÃO DA PROVA

'''Utilizando apenas os conceitos que foram ensinados nesta matéria até aqui, faça um programa que:
1) [0.25pt] Solicite o nome do usuário e de uma outra pessoa
a. A partir de agora, todas as menções a cada um (usuário ou outra pessoa) deverão ser pelo nome

2) [1.5pt] Diga quantas vezes o nome maior (em quantidade de caracteres) é maior que o menor,
limitado a 2 casas decimais

3) [0.25pt] Utilizando seus nomes, solicite suas alturas, em cm (ex: 185 cm)

4) Considerando que a altura média de um jogador da NBA é de 2,01m, diga, para cada pessoa:
a. [1pt] Se ela for mais alta que ou estiver nesta média, quantos centímetros ela é mais alta
b. [2pts] Se ela for mais baixa que esta média, quantos porcento da sua própria altura ela teria
que ter a mais para chegar a esta média (limitado a 3 casas decimais)

5) [0.25pt] Solicite agora, a idade de cada usuário

6) [0.5pt] Diga se a idade dos dois é igual
a. [1pt] Caso não seja igual, diga, utilizando um número inteiro, quantos anos o mais velho
tem a mais que o segundo

7) [0.25pt] Diga a média de idade entre as 2 idades

8) [3pts] O programa deve conter também, em forma de comentário em bloco,
exemplos de inputs e outputs para cada uma das condições possíveis que
vocês identificaram e programaram.
Estes comentários podem ser tanto item a item, quanto ao final de tudo.
'''

# 1) [0.25pt] Solicite o nome do usuário e de uma outra pessoa
# a. A partir de agora, todas as menções a cada um (usuário ou outra pessoa) deverão ser pelo nome

nome_usuario = input("Me informe seu nome")
nome_usuario_2 = input(f"{nome_usuario}, digite o nome do seu colega")

# 2) [1.5pt] Diga quantas vezes o nome maior (em quantidade de caracteres) é maior que o menor,
# limitado a 2 casas decimais

# if len(nome_usuario)>len(nome_usuario_2):
#     print(f"{nome_usuario} é {len(nome_usuario)/len(nome_usuario_2)}  vezes maior que {nome_usuario_2}")
# ### este if ^^^ não está fechado por um else
#
# if len(nome_usuario)<len(nome_usuario_2):
#     print(f"{nome_usuario_2} é {len(nome_usuario_2) / len(nome_usuario)}  vezes maior que {nome_usuario}")
# ### este if ^^^ está fechado por este else \/\/
# else: #entra usuário 1 NÃO FOR MENOR que usuário 2
#     print(print(f"{nome_usuario} é {len(nome_usuario)/len(nome_usuario_2)}  vezes maior que {nome_usuario_2}"))
# #não está coberto o caso de serem iguais
# # ou faz mais um if (que neste caso só tem 3 opções) ou faz apenas if/else


##############################################################################################################
quantidade_de_letras_usuario_1=len(nome_usuario)
quantidade_de_letras_usuario_2=len(nome_usuario_2)

if quantidade_de_letras_usuario_1>quantidade_de_letras_usuario_2:
    quantas_vezes=quantidade_de_letras_usuario_1/quantidade_de_letras_usuario_2
    print(f"{nome_usuario} tem {quantidade_de_letras_usuario_1} letras, e isto é {quantas_vezes:.2f} vezes"
          f"maior do que o {nome_usuario_2}, que tem {quantidade_de_letras_usuario_2}")
else:  #está incluído o caso de serem iguais
    quantas_vezes=quantidade_de_letras_usuario_2/quantidade_de_letras_usuario_1
    print(f"{nome_usuario_2} tem {quantidade_de_letras_usuario_2} letras, e isto é {quantas_vezes:.2f} vezes"
          f"maior do que o {nome_usuario}, que tem {quantidade_de_letras_usuario_1}")
'''
temos 3 condições possíveis neste cenário:
usuario1>usuario2
Ex: Maria e Joao. Sairia o print da linha 59
usuario2>usuario1
Ex: Joao e Maria. Sairia o print da linha 63
usuario1==usuario2
Ex: Maria e Paulo. Sairia o print da linha 63
'''


# 3) [0.25pt] Utilizando seus nomes, solicite suas alturas, em cm (ex: 185 cm)
altura_usuario = float(input("{} diga a sua altura em cm".format(nome_usuario)))
altura_usuario2 = float(input("{} diga a sua altura em cm".format(nome_usuario_2)))


# 4) Considerando que a altura média de um jogador da NBA é de 2,01m, diga, para cada pessoa:
# a. [1pt] Se ela for mais alta que ou estiver nesta média, quantos centímetros ela é mais alta
altura_media=201
if altura_usuario>=altura_media: #201
    #diferenca_de_altura=altura_media-altura_usuario  #é um número negativo
    diferenca_de_altura =  altura_usuario -altura_media
    print(f"{nome_usuario} é {diferenca_de_altura} cm mais alto do que a média da NBA")

# b. [2pts] Se ela for mais baixa que esta média, quantos porcento da sua própria altura ela teria
# que ter a mais para chegar a esta média (limitado a 3 casas decimais)
else:
    resposta= ((altura_media-altura_usuario)/altura_usuario)*100 #= 8,64%
    print(f"{nome_usuario} teria que ter {resposta:.3f}% a mais da sua propria altura para chegar à media")




if altura_usuario2>=201:
    diferenca_de_altura2 =  altura_usuario2 -altura_media
    print(f"{nome_usuario_2} é {diferenca_de_altura2} cm mais alto do que a média da NBA")

else:
    resposta= ((altura_media-altura_usuario2)/altura_usuario2)*100 #= 8,64%
    print(f"{nome_usuario_2} teria que ter {resposta:.3f}% a mais da sua propria altura para chegar à media")
'''
caso tenhamos a altura > ou = à média:
será printado a diferenca_de_altura
ex: altura_usuario = 202. diferenca_de_altura=1
ex: altura_usuario = 201. diferenca_de_altura=0
caso tenhamos a altura < que a média:
será printada a respsota
ex: altura usuario=185cm. print: 8,64%
'''


# 5) [0.25pt] Solicite agora, a idade de cada usuário
idade_usuario = int(input("{} diga a sua idade em anos".format(nome_usuario)))
idade_usuario_2 = int(input("{} diga a sua idade em anos".format(nome_usuario_2)))

# 6) [0.5pt] Diga se a idade dos dois é igual

if idade_usuario_2==idade_usuario:
    print("as idades de {} e {} são iguais".format(nome_usuario,nome_usuario_2))
# a. [1pt] Caso não seja igual, diga, utilizando um número inteiro, quantos anos o mais velho
# tem a mais que o segundo
else:
    if idade_usuario<idade_usuario_2:
        diferenca_de_idade=int(idade_usuario_2-idade_usuario) #caso o input seja float
        #print(f'a diferença de idade entre {nome_usuario} e {nome_usuario_2}é de {diferenca_de_idade} anos')
        print(f"{nome_usuario_2} é {diferenca_de_idade} anos mais velho que {nome_usuario}")
    else: #só entra aqui se idade_usuario>idade_usuario_2
        diferenca_de_idade = int(idade_usuario - idade_usuario_2) #caso o input seja float
        #print(f'a diferença de idade entre {nome_usuario} e {nome_usuario_2}é de {diferenca_de_idade} anos')
        print(f"{nome_usuario} é {diferenca_de_idade} anos mais velho que {nome_usuario_2}")

'''
temos 3 casos distintos:
usuario 1 mais velho
vai sair o print da linha 133
ex: idade_usuario_1 = 30, idade_usuario_2=29

usuario 2 mais velho
vai sair o print da linha 129
ex: idade_usuario_1 = 29, idade_usuario_2=30

os 2 da mesma idade
vai sair o print da linha 122
ex: idade_usuario_1 = 30, idade_usuario_2=30
'''

#7) [0.25pt] Diga a média de idade entre as 2 idades
idade_media = (idade_usuario+idade_usuario_2)/2

print(f'a média entre {nome_usuario} e {nome_usuario_2} é de {idade_media} anos')

'''
como não há condicionais nem formatação, a resposta é sempre direta, do mesmo formato
ex: idade_usuario_1 = 29, idade_usuario_2=31. Média = 30.0
'''
