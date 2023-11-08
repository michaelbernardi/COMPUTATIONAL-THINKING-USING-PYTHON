# relembrar operadores aritméticos e lógicos ##############################################################
## lembrar da ordem de realização das operaçõs:
### **, depois * e /, depois +-
#### para mudar a ordem, utilizar ()

## lembrando que, na comparação, se as variáveis forem de tipos diferentes, retorna False
## lembrando que comparação é ==
### = é designação

# outros tipos de formatação/funções em string ##############################################################
# num = 23
# print(f"Número {num}")
# print(f"Número {num:5d}")
# print(f"Número {num:05d}")
# print(f"Número {num:>05d}")
# print(f"Número {num:<05d}")
# print(f"Número {num:^06d}")

# para CRESCER a quantidede de caracteres, é igual ao 'd'
nome = 'FIAP'
# print(f"Nome = {nome:>10s}")
# print(f"Nome = {nome:>010s}")
# print(f"Nome = {nome:*<10s}")
# print(f"Nome = {nome:<10s}")
# print(f"Nome = {nome:^10s}")
# print(f"Nome = {nome:^010s}")

# para LIMITAR a quantidade de caracteres, é igual ao 'f'
## aqui não aceita < > ^
nome_grande="FIAP COM MAIS DO QUE DEZ CARACTERES"
# print(f"Nome = {nome_grande:>.10}")
# print(f"Nome = {nome_grande:<.10}")
# print(f"Nome = {nome_grande:^.10}")

Num_float=12.0123456789
# print('{:>10f}'.format(Num_float))
# print(f'{Num_float:>10f}')
#
#print('{:*>10f}'.format(Num_float))
#print('{:.10f}'.format(Num_float))
#print('{:.3f}'.format(Num_float))
# print('{:*^10.2f}'.format(Num_float))


# nome = "Computational Thinking using Python"
# tamanho = len(nome) # Conta os caracteres da string
# todas_maiusculas = nome.upper() # Converte tudo em maiúsculo
# todas_minusculas = nome.lower() # Converte tudo em minúsculo
# iniciais_maiusculas = nome.title() # Somente as iniciais em maiúsculo
# nome_capitalize = nome.capitalize()
#
# print(f"{nome} possui {tamanho} caracteres")
# print(f"Tudo maiúsculo: {todas_maiusculas}")
# print(f"Tudo minúsculo: {todas_minusculas}")
# print(f"Iniciais maiúsculas: { iniciais_maiusculas }")
# print(f"Primeira maiúscula: { nome_capitalize }")

# salvando as mudanças
# nome = "Paulo Caixeta"
# nome_formatado = '{:#<40}'.format(nome)
# print(nome_formatado)
# nome_formatado = '{:*^40}'.format(nome)
# print(nome_formatado)
# nome_formatado = '{: >40}'.format(nome)
# print(nome_formatado)


# exercícios ##############################################################
# ######### Observação: Resolver este exercício utilizando somente os comandos de entrada, saída e processamento de dados


# Exercício 1. Dado um numero pelo usuário, calcular o dobro e o quadrado
# obs: ao imprimir, colocar junto o número original
#numero_original=int(input("Diga um número"))
# [...]
#print("O dobro do número {} é {}, e seu quadrado é {}".format(numero_original,dobro,quadrado))


# Exercício 2. Dados três números pelo usuário, calcular sua média,
# e a razão entre o primeiro e o último
#[...]
#media_de_3_numeros= (numero_1+numero2+numero3)/3
# obs: definir a resposta a 10 caracteres, sendo 3 decimais

# Exercício 3. Dado um numero pelo usuário, exibir o anterior e posterior
# (Ex: input=20, resposta=19 e 21)
# numero_original = input("Diga um número")
# numero_original_int=int(numero_original)
#
# proximo_numero = numero_original_int+1
# numero_anterior = numero_original_int-1
#
# print()

# Exercício 3.1 Dado um numero pelo usuário, exibir o posterior
# (Ex: input=20, resposta= 21)
# numero_original = input("Diga um número")
# numero_original_int=int(numero_original)
#
# numero_original_int = numero_original_int + 1
# # isto é equivalente a:
# numero_original_int+=1

# Exercício 4. Dados dois numeros pelo usuário, calcular a potência entre eles

# Exercício 5. Dado um numero pelo usuário, exibir o proximo multiplo de 5
numero_original=float(input("Diga um número"))
multiplo_anterior_de_5 = numero_original // 5  # 8//5 = 1
proximo_multiplo_de_5 = multiplo_anterior_de_5*5 +5  #1*5 + 5 = 10
print("O proximo multiplo de 5 é",proximo_multiplo_de_5)


num = int(input("Digite um número: "))
falta_para_chegar_a_mutiplo_de_5 = 5 - num % 5  # 5 - 8%5 = 5-3 =2
prox_multiplo = num + (falta_para_chegar_a_mutiplo_de_5) #8 + 2
print("O próximo múltiplo de 5 é:", prox_multiplo)
'''
Exemplos:
Input: 8   -> Output: 10
Input: 15 ->  Output: 20
Input: 1  ->  Output: 5
Input: 89 ->  Output: 90'''



numero_1 = float( input("Digite o Número 1 ") )
numero_2 = float( input("Digite o Número 2 ") )
numero_3 = float( input("Digite o Número 3 ") )
media = (numero_1+numero_2+numero_3) / 3
razao = (numero_1 / numero_3)
#
print(f"A média foi {media:10.3f} ")
print("A média foi {:10.3f}".format(media))
#
#formato="{:10.3f}"
#print(formato.format(media))
print(f"A Razão entre o Primeiro e o último é {razao:10.3f}")
# 0.7142857142857143
