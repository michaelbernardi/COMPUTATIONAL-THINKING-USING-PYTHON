## FUNÇÕES (cont)
# usando funções para organizar o código/ realizar tarefas repetitivas
# def print_pctg(numero):
#     print(f"{numero:.2f}%")
#
#
#
# n=25.3454543454345
#
# #na hora de chamar a função, temos que fornecer um argumento que exista neste momento
# #tenho que passar algo que exista. Neste caso, 'n'
# print_pctg(n)
# print(n)
#
# # solicitar 3 números necessariamente inteiros
# n1=float(input("Diga um número inteiro"))
#
# while n1!=int(n1):
#     print("Você não digitou um número inteiro")
#     n1 = float(input("Diga um número inteiro"))
#
# n2=float(input("Diga um segundo número inteiro"))
#
# while n2!=int(n2):
#     print("Você não digitou um número inteiro")
#     n2 = float(input("Diga um segundo número inteiro"))
#
# n3=float(input("Diga um terceiro e último número inteiro"))
#
# while n3!=int(n3):
#     print("Você não digitou número inteiro")
#     n3 = float(input("Diga um terceiro e último número inteiro"))
#
# n1=int(n1)
# n2=int(n2)
# n3=int(n3)


#### criando funções para organizar este código
# começando com a mensagem de erro
def msg_erro():
    print("Você não digitou número inteiro")

#função que solicita e guarda na memória um número do usuário
def solicita_numero(condicao,ordem): #posso definir na ordem que eu quiser
    #porém, na hora de utilizar, tenho que seguir a mesma ordem
    numero=float(input(f"Diga um {ordem}º número {condicao}"))  #criando o número
    return numero

#função para substituir o while
def verifica_inteiro(numero,condicao,ordem):
    while numero!=int(numero):
        msg_erro()
        numero = solicita_numero(condicao, ordem)
    return int(numero) #que agora é garantidamente inteiro

def input_numero(condicao,ordem):
    numero = solicita_numero(condicao, ordem)
    numero = verifica_inteiro(numero, condicao, ordem)
    return numero #necessariamente, no nosso exemplo, inteiro

# solicitar 3 números necessariamente inteiros

#eu estou colocando na memória, com o nome de n1, o retorno da função 'input_numero'
# n1=input_numero("inteiro",1)
# n2=input_numero("Inteiro",2)
# n3=input_numero("Inteiro",3)

# criar uma função que solicite ao usuário e imprima na tela N
# números necessariamente inteiros
#N=8 #exemplo

def imprime_n_inteiros(N):
    """
    Aqui é o espaço para a documentação da função.\n
    Podemos escrever qualquer coisa, mas a ideia é que sirva de explicação para quem for utilizar a função\n
    Geralmente, escrevemos um breve texto e, abaixo, os parâmetros (argumentos) e o retorno
    :param N: Numero inteiro para o range do loop
    :return: None (apenas imprime)
    """
    print(f"Solicitando ao usuário {N} números inteiros")
    print()
    for i in range(N): #range(N)=[0,1,2,3,4,5,6,7]
        print("Número {} de {}".format(i+1,N))
        num_temp = input_numero("inteiro",i+1)
        print(num_temp)
        print("------------")
    print("Fim!")

N=input_numero("inteiro",1)
imprime_n_inteiros(N)


###EXERCÍCIO
## adaptar a(s) nossa(s) funções para que, ao a pessoa alterar a condição,
# esta condição seja satisfeita
# condições possíveis: pos/neg/int/float/par/ímpar/diferentes*

# isto que vocês fizeram funciona para combinação de condições?
### se não, como implementamos a escolha combinada?