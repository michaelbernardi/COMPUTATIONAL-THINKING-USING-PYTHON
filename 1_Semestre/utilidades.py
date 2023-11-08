def numero_ordinal(n):
    print(f"{n:.3f}º")

def operacoes(*args,operacao):
    '''
    Função que recebe a operação desejada e os números para realizar esta operação
    :param args: números (int ou float) que serão utilizados na operação
    :param operacao: "subtração" ou "divisão". Operação a ser realizada com os números
    :return: Número com o resultado da operação
    '''
    if operacao=="divisão":
        resposta=1
        for i in args:
            resposta/=i #resposta=respsota/i
        return resposta
    elif operacao=="subtração":
        resposta=0
        for i in args:
            resposta-=i #resposta=resposta-i
        return resposta
    else:return "Resposta inválida"

def solicita_impar():
    n = float(input("Diga um número ímpar"))
    while n%2==0:
        print("Você não digitou um número ímpar")
        n = float(input("Diga um número ímpar"))
    return n

def solicita_operacao():
    while True:
        operacao=input("Escolha uma das duas operações: 'divisão' ou 'subtração': ")
        if operacao== "subtração" or operacao=="divisão":return operacao
        print("Você escolheu uma opção inválida!")

