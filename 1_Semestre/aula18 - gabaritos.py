
### EXERCÍCIOS ADICIONAIS

#1) escreva uma função que receba como argumento um número e retorne seu fatorial

def fatorial(n):
    fatorial = 1
    while n>0:
        fatorial*=n
        n-=1
    return fatorial


#2) escreva uma função que solicite ao usuário um número e force para que ele seja positivo e inteiro,e retorne este número

def positivo_inteiro():
    while True:
        n=float(input("Diga um número inteiro e positivo: "))
        if n==int(n) and n>=0: return n
        print("Você não digitou um número inteiro e positivo")

#3) escreva uma função que combine as funções dos exercícios anteriores
# (ou seja, uma função sem parâmetros que utilize o retorno da segunda função como parâmetro da primeira)

def combina():
    n=positivo_inteiro()
    resposta=fatorial(n)
    return resposta

#4) Crie uma função que receba uma palavra e retorne ela toda em letras maiúsculas

def maiusculas(palavra):
    return palavra.upper()


#5) Cria uma função que receba uma palavra e uma condição ('maiúscula' ou 'minúscula') e retorne a palavra na condição solicitada

def muda_palavra(condicao,palavra):
    if condicao=="maiuscula":
        return palavra.upper()
    elif condicao=="minuscula":
        return palavra.lower()
    else:
        return "condição invalida"

#6) Crie uma função que receba 2 números (inicio e fim), e imprima os números pares neste intervalo (incluindo o início e fim)

def pares(inicio,fim):
    for i in range(inicio,fim+1):
        if i%2==0: print(i)

#7) Crie uma função que receba 2 números e imprima sua soma, multiplicação, divisão e subtração.
# Estes prints deverão ser formatados para serem bem explícitos no que está sendo mostrado (incluindo os números originais);
# E esta função deverá estar devidamente documentada, explicando tudo o que ela realiza, seus parâmetros e possíveis retornos

def operacoes(n1,n2):
    '''
    Função que realiza e imprime,separadamente, as quatro operações básicas (soma, multiplicação, divisão e subtração) entre os 2 argumentos
    :param n1: float ou int
    :param n2: float ou int
    :return: None (apenas imprime)
    '''
    soma = n1+n2
    multiplicacao = n1*n2
    divisao=n1/n2
    subtracao=n1-n2

    print(f"A soma de {n1} e {n2} é {soma}")
    print(f"A multiplicacao de {n1} por {n2} é {multiplicacao}")
    print(f"A divisao de {n1} por {n2} é {divisao}")
    print(f"A subtracao de {n1} e {n2} é {subtracao}")
