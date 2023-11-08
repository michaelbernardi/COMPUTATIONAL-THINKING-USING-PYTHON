
## Alguns conceitos para auxiliar:
# 1)
# def verifica_par(numero):
#     return numero%2==0 #o resultado já é naturalmente um booleano, então eu retorno diretamente ele

#----------------------------------------------------------------
# 2)
#quando eu tenho uma variável ou um retorno que vai ser uma booleana (True ou False), eu posso colocar direto no "If"
# if verifica_par(5): print("é par")
# else: print("é impar")
#
# e_par=verifica_par(4)
# if e_par: print("é par")
# else:print("é impar")

#-----------------------------------------------------------------
# 3) #ao criar uma variável na estrutura if-else, eu posso fazer em uma linha:
# if n%2==0:
#     tipo="par"
# else:
#     tipo="impar"

#é igual a:
# n=4
# tipo="par" if (n%2==0) else 'impar'
# print (tipo)

## EXERCÍCIO DA AULA PASSADA

# isto que nós fizemos na aula passada funciona para combinação
# de condições?
### se não, como implementamos a escolha combinada?

# def verificar_par(numero):return numero%2==0
#
# def verificar_positivo(numero): return numero>=0
#
# n=float(input("Diga um número positivo e par"))
# while True:
#     if verificar_par(n) and verificar_positivo(n):
#         #para que alguma coisa aconteça, tem que ser antes do break
#         break
#         #nada aqui funciona mais, pois já saímos do loop
#     else:
#         n = float(input("Diga um número positivo e par"))


## EXERCÍCIOS
#1) a) escreva uma função que execute e retorne a soma E a multiplicação
# de todos os números passados como parâmetro

'''lembrando que:
- *args aceita múltiplas entradas, e as armazena em um lista
- só colocamos asterísco (*) na definição. Ou seja, na hora de usar, é apenas args
--- então, nós podemos interar no próprio args

- o range vai criar uma lista para mim, utilizando os números inteiros que eu passei como argumento
-- ex: range(5) -> [0,1,2,3,4] #necessariamente sequencial, de acordo o step
'''
def soma_multiplica(*args):
    soma=0 #tenho que definir antes do loop, senão vai ser re-criado todas as vezes que o loop acontecer
    multiplica=1
    for i in args: #ou seja, eu vou pegar um por um, todos os itens da lista args, na ordem com a qual foram escritos
        soma=soma+i
        multiplica*=i
    #fora do for, neste caso, nós fazemos o return
    #lembrando que o return acaba a função naquele ponto
    return soma,multiplica

# 1)b) imprima na tela o resultado da função anterior,
# com pelo menos 5 números como parâmetros. Na hora de imprimir,
# formate a frase de resposta de maneira a ficar bem claro para o usuário
# o que cada número significa

## lembrando que:
#ao chamar esta função, eu tenho que fornecer 2 variáveis de memória
# porque a função retorna 2 variáveis
# e a ordem destas variáveis vai ser sempre a mesma
soma,produto=soma_multiplica(5,7,1,9,-68,49,147,0) # args=[5,7,1,9,-68,49,147,0]
# print(f'A soma dos números é {soma}')
# print(f"O produto dos números é {produto}")


# 1)c) Agora, escreva aqui embaixo uma modificação da função anterior
# para que seja possível incluir no print os números digitados

def soma_multiplica(*args):
    soma=0
    multiplica=1
    for i in args:
        soma=soma+i
        multiplica*=i
    return soma,multiplica,args
soma,produto,numeros_digitados=soma_multiplica(5,7,1,9,-68,49,147,0) # args=[5,7,1,9,-68,49,147,0]
#
# print(f'A soma dos números {numeros_digitados} é {soma}')
# print(f"O produto dos números {numeros_digitados} é {produto}")


# 1)d)
# modificar a função da 1)a) para que a função tenha como argumento
# a operação que queremos fazer: soma OU multiplicação, e a função
# deve retornar APENAS o que foi passado como parâmetro. Documente
# a sua função, descrevendo o que ela faz, qual(is) argumento(s) e retorno(s)
# e seus tipos

def soma_multiplica(operacao,*args):
    '''
    Função que recebe a operação a ser realizada, e uma lista de valores
    numéricos para realizar a operação.
    :param operacao: str, "soma" ou "multiplicacao"
    :param args: tupla contendo apenas números
    :return: retorna um número resultado da operação escolhida
    '''
    if operacao=="soma":
        soma = 0
        #loop que percorre a lista com os parâmetros e soma cada um deles
        for i in args:
            soma=soma+i
        return soma #tem que ser fora do for, senão ele não completa o loop

    elif operacao=="multiplicacao":
        multiplica = 1
        for i in args:
            multiplica*=i
        return multiplica
    else: return "Resposta inválida"


#outra opção
# def soma_multiplica(operacao,*args):
#     '''
#
#     :param operacao:
#     :param args:
#     :return:
#     '''
#     soma=0
#     multiplica=1
#     for i in args:
#         soma=soma+i
#         multiplica*=i
#     if operacao=="soma":return soma
#     elif operacao=="multiplicacao":return multiplica
#     else:return "Resposta inválida"
#

# 2) Escreva uma função que receba 3 números como parâmetros:
#    n, maior, menor;
# retorne dizendo se n está entre maior e menor

def esta_entre(n,maior,menor): #
    return menor<n<maior  #menor<n and maior>n

print(esta_entre(5,2,10))  #a ordem SEMPRE importa! Tem que ser a mesma da definição da função


### EXERCÍCIOS ADICIONAIS

#1) escreva uma função que receba como argumento um número e retorne seu fatorial

#2) escreva uma função que solicite ao usuário um número e force para que ele seja positivo e inteiro,e retorne este número

#3) escreva uma função que chame combine as funções dos exercícios anteriores
# (ou seja, uma função sem parâmetros que utilize o retorno da segunda função como parâmetro da primeira)

#4) Crie uma função que receba uma palavra e retorne ela toda em letras maiúsculas

#5) Cria uma função que receba uma palavra e uma condição ('maiúscula' ou 'minúscula') e retorne a palavra na condição solicitada

#6) Crie uma função que receba 2 números (inicio e fim), e imprima os números pares neste intervalo (incluindo o início e fim)

#7) Crie uma função que receba 2 números e imprima sua soma, multiplicação, divisão e subtração.
# Estes prints deverão ser formatados para serem bem explícitos no que está sendo mostrado (incluindo os números originais);
# E esta função deverá estar devidamente documentada, explicando tudo o que ela realiza, seus parâmetros e possíveis retornos
