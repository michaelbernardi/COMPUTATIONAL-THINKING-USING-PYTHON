# ## ESTRUTURAS DE DECISÃO
# # # revisão if/elif/else
#
# # if condicao1:  # SEMPRE DEVE EXISTIR e Vir primeiro
# #     <acao, caso condicao seja verdadeira>
# # elif condicao2:    # Necessita de um if antes
# #     < acao, caso  condicao1 seja false e condicao2 seja    verdadeira >
# # elif condicao3:
# #     ...
# # ...
# # elif condicaoN:
# #     ...
# # else: # Necessita de um if antes, podendo ter elif.
# #     <acao caso TODAS as condicoes sejam falsas>
#
# # combinações possíveis
# # if
# # if / elif (vários elifs)
# # if / else
# # if / elif (vários elifs) / else
#
#
# #
# # # estrutura match-case (introduzida no Python 3.10)
# #
#
# # x = int(input("Digite o número desejado: "))
# # entrada = input("Digite s ou N: ")
#
# # match entrada:
# #     case 's':
# #         print("Caso afirmativo")
# #     case 'N':
# #         print("Caso negativo")
# #     case _:
# #         print("Nenhuma opção válida foi selecionada.")
#
# # #Exemplos
#
# # Menu s / N
# # selecao = input("Digite s para sim ou n para não")
# # match selecao:
# #     case "s":
# #         print("A opção 'sim' foi selecionada")
# #     case "n":
# #         print("A opção 'não' foi selecionada")
#
# ## Menu de opções
# # selecao = input("Digite uma opção de 0 a 3: ")
# #
# # match selecao:
# #     case "0":
# #         print("Você selecionou a opção 0.")
# #     case "1":
# #         print("Você selecionou a opção 1.")
# #     case "2":
# #         print("Você selecionou a opção 2.")
# #     case "3":
# #         print("Você selecionou a opção 3.")
# #     case _:
# #         print("Opção inválida!")
#
# # # Exercício 1: Menu s / N com vários casos
# # # Forma 1: escrever opção a opção
# # selecao = input("Digite s para sim ou n para não: ")
# # match selecao:
# #     case "s":
# #         print("A opção 'sim' foi selecionada")
# #     case "S":
# #         print("A opção 'sim' foi selecionada")
# #     case "Sim":
# #         print("A opção 'sim' foi selecionada")
# #     case "sim":
# #         print("A opção 'sim' foi selecionada")
# #     case "n":
# #         print("A opção 'não' foi selecionada")
# #     case "N":
# #         print("A opção 'não' foi selecionada")
# #     case "não":
# #         print("A opção 'não' foi selecionada")
# #     case "Não":
# #         print("A opção 'não' foi selecionada")
# #     case _:
# #         print("Opção inválida")
#
# # # Forma 2: utilizar combinações (operador |)
# # selecao = input("Digite s para sim ou n para não: ")
# #
# # match selecao:
# #     case "s" | "S" | "Sim" | "sim":
# #         print("A opção 'sim' foi selecionada")
# #     case "n" | "N" | "Não" | "não":
# #         print("A opção 'não' foi selecionada")
# #     case _:
# #         print("Opção inválida")
#
# # # Forma 3: utilizar combinações (operador |) e preprocessamento
# # selecao = input("Digite s para sim ou n para não: ")
# # if len(selecao) > 1:
# #     selecao = selecao[0]
# #
# # selecao = selecao.lower()  # converte pra minúsculo
# #
# # match selecao:
# #     case "s":
# #         print("A opção 'sim' foi selecionada")
# #     case "n":
# #         print("A opção 'não' foi selecionada")
# #     case _:
# #         print("Opção inválida")
#
# # # Códigos de erro HTTP
# # codigo_retorno = int(input("Qual foi o código de retorno da API? "))
# #
# # match codigo_retorno:
# #     case 100 | 101 | 103:
# #         print("Código do tipo 1XX - Informativo")
# #     case 200 | 201 | 203:
# #         print("Código do tipo 2XX - Sucesso")
# #     case 300 | 301 | 303:
# #         print("Código do tipo 3XX - Redirecionamento")
# #     case 400 | 401 | 402:
# #         print("Erro do tipo 4XX - Erro do cliente")
# #     case 500 | 501 | 502:
# #         print("Erro do tipo 5XX - Erro do servidor")
# #     case _:
# #         print("Código desconhecido")
#
# # # Exercício 2: reescrever com divisão inteira
# # codigo_retorno = int(input("Qual foi o código de retorno da API? "))
# # familia_do_codigo = codigo_retorno // 100
# #
# # match familia_do_codigo:
# #     case 1:
# #         print("Código do tipo 1XX - Informativo")
# #     case 2:
# #         print("Código do tipo 2XX - Sucesso")
# #     case 3:
# #         print("Código do tipo 3XX - Redirecionamento")
# #     case 4:
# #         print("Erro do tipo 4XX - Erro do cliente")
# #     case 5:
# #         print("Erro do tipo 5XX - Erro do servidor")
# #     case _:
# #         print("Código desconhecido")
#
# ### TODO: REVISAR
# # # Exercício 3: Crie um programa que use a instrução match para verificar o tipo de uma variável (int, float, string)
# # # e imprima uma mensagem adequada com base no tipo.
# # # x = ?
# # # match pra ver e imprimir o tipo de x
# # x = "lfhjdasdjpasjd"
# # # x = 342134
# # # x = 234234.0
# # # x = True
# # tipo_x = type(x)
# # tipo_inteiro = type(int())
# #
# # match tipo_x:
# #     case tipo_inteiro:
# #         print("inteiro")
# #     # case type(float()):
# #     #     print("float")
# #     # case type(str()):
# #     #     print("String")
# #     # case type(bool()):
# #     #     print("Boolean")
# #     # case _:
# #     #     print("tipo não definido")
#
#
# # # Exercício 4: Escreva um programa que solicite ao usuário um número de 1 a 7
# # # e imprima o dia da semana correspondente (por exemplo, 1 = domingo, 7 = sábado, etc.).
# # # Utilize:
# # dia_numerico = input("Digite o número correspondente ao dia da semana.\n" +
# #                      "\tExemplo: 1 para Domingo, 7 para Sábado.\n")
# #
# # # # a - estruturas condicionais if, elif e else.
# # # if dia_numerico == "1":
# # #     print("Domingo")
# # # elif dia_numerico == "2":
# # #     print("Segunda-feira")
# # # elif dia_numerico == "3":
# # #     print("Terça-feira")
# # # # falta implementar os dias 4, 5 e 6
# # # elif dia_numerico == "7":
# # #     print("Sábado")
# # # else:
# # #     print("Entrada inválida.")
# #
# # # b - match
# # match dia_numerico:
# #     case "1":
# #         print("Domingo")
# #     case "2":
# #         print("Segunda-feira")
# #     # Falta implementar os casos de 3, 4, 5, 6 e 7
# #     case _:
# #         print("Entrada inválida")
#
# # # Exercício 5: Crie um programa para verificar se uma string inserida pelo usuário é uma vogal,
# # # uma consoante ou nenhum dos dois, utilizando:
# # # Observação: Não se esqueça de validar o tamanho da string.
# #
# # # leio uma letra do teclado
# letra = input("Digite uma letra: ")
#
# # operador ternário
# # valido o tamanho da string, forçando a ter len == 1
# letra = letra[0] if len(letra) > 1 else letra
# # converte para lower-case (minúsculo)
# letra = letra.lower()
# #
# # # a - A instrução match
# # # match letra:
# # #     # caso letra seja vogal
# # #     case 'a' | 'e' | 'i' | 'o' | 'u':
# # #         print("É uma vogal")
# # #     # case consoantes:  # falta digitar as consoantes
# # #     case _:
# # #         print("Não é vogal, nem consoante")
# #
# # b - o operador `in`
# # x in coleção  # "EM", checa se o valor de x está dentro da coleção
# import string
#
# alfabeto = string.ascii_lowercase  # remover as vogais e obter apenas as consoantes
#
# consoantes = alfabeto.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
# if letra in 'aeiou':
#     print("é uma vogal")
# elif letra in consoantes:  # definir consoantes
#     print('é uma consoante')
# else:
#     print("não é vogal, nem consoante")
#
#
#
#
#
#
#
#
#
#
#
# for  i vai início-final:
#     executo uma ação
#
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(10):
#     print(i)
#
# vogais = 'aeiou'
#
# for letra in vogais:
#     print(letra)
#
# for i in range(len(vogais)):
#     print(vogais[i])
#
#
# # import string
# # alfabeto = string.ascii_lowercase  # remover as vogais e obter apenas as consoantes
# # vogais = 'aeiou'
# # # consoantes = alfabeto.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
# #
# #
# # consoantes = alfabeto
# # for vogal in vogais:
# #     consoantes = consoantes.replace(vogal, '')
# #
# # print("Vogais: ", vogais)
# # print("Consoantes: ", consoantes)
#
#
#
#
#


# Exercício 6: Escreva um programa que determine se um número é divisível por 3 e/ou 5.
# Se for divisível por 3, imprima "Divisível por 3."
# Se for divisível por 5, imprima "Divisível por 5."
# Se for divisível por ambos, imprima "Divisível por 3 e 5."
# Caso contrário, imprima "Não é divisível por 3 nem 5."

#
# n = int(input("Digite um número: "))
#
# if n % 3 == 0 and n % 5 == 0:
#     print("É divisível por 3 e por 5.")
# elif n % 5 == 0:
#     print("É divisível por 5.")
# elif n % 3 == 0:
#     print("É divisível por 3.")
# else:
#     print("Não é divisível nem por 3, nem por 5.")

## Dada uma sequência numérica (ex: 1234980624898429) verifique se cada algarismo:
# Exercício 6 - b: Escreva um programa que determine se um número é divisível por 3 e/ou 2.
# Se for divisível por 3, imprima "Divisível por 3."
# Se for divisível por 2, imprima "Divisível por 2."
# Se for divisível por ambos, imprima "Divisível por 3 e 2."
# Caso contrário, imprima "Não é divisível por 3 nem 2."

# 0293802982390850239
seq = input("Digite sua sequência numérica: ")
num_div_2 = 0
num_div_3 = 0
num_div_2_e_3 = 0
num_else = 0

for n in seq:
    n = int(n)
    print(f"O algarismo {n} ", end="\t")
    if n % 3 == 0 and n % 2 == 0:
        print("É divisível por 3 e por 2.")
        num_div_2_e_3 += 1
    elif n % 2 == 0:
        print("É divisível por 2.")
        num_div_2 += 1
    elif n % 3 == 0:
        print("É divisível por 3.")
        num_div_3 += 1
    else:
        print("Não é divisível nem por 3, nem por 2.")
        num_else += 1

print("O número de divisíveis por 2 e 3 é ", num_div_2_e_3)
print("O número de divisíveis por 2 é", num_div_2)
print("O número de divisíveis por 3 é ", num_div_3)
print("O número de não divisíveis por 2 nem por 3 é ", num_else)
