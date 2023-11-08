## *ARGS e **KWARGS (KeyWord Args)


def soma_dos_numeros(*args):
    soma=0
    for i in args:
        soma+=i #soma=soma+i
    return soma

# soma=soma_dos_numeros(10,5,1,5,7,9,50,5444)
# print(soma)

def cadastra_no_sistema(**kwargs):
    print(kwargs)
nome="Paulo"
#cadastra_no_sistema(nome=nome,
#                    idade=30,
#                    filme="Senhor dos aneis",
#                    irmaos=1)
## ARGUMENTOS PRÉ-DEFINIDOS
def print_formatado(n=5.789546):#extamente 01 valor
    print(f"{n:.2f}")
#print_formatado()



###EXERCÍCIO
## adaptar a(s) nossa(s) funções para que,
# ao a pessoa alterar a condição,
# esta condição seja satisfeita
# condições possíveis: pos/neg/int/float/par/ímpar/diferentes*
def msg_erro(condicao):
    print(f"Você não digitou número {condicao}")

#função que solicita e guarda na memória um número do usuário
def solicita_numero(condicao,ordem): #posso definir na ordem que eu quiser
    #porém, na hora de utilizar, tenho que seguir a mesma ordem
    numero=float(input(f"Diga um {ordem}º número {condicao}"))  #criando o número
    return numero

def verifica_inteiro(numero,condicao,ordem):
    while numero!=int(numero):
        msg_erro(condicao)
        numero = solicita_numero(condicao, ordem)
    return int(numero) #que agora é garantidamente inteiro

def verifica_decimal(numero,condicao,ordem):
    while numero==int(numero):
        msg_erro(condicao)
        numero = solicita_numero(condicao, ordem)
    return numero #que agora é garantidamente inteiro

def verifica_par(numero,condicao,ordem):
    while numero%2!=0:
        msg_erro(condicao)
        numero = solicita_numero(condicao, ordem)
    return numero  # que agora é garantidamente inteiro


def verifica_impar(numero,condicao,ordem):
    while numero%2==0:
        msg_erro(condicao)
        numero = solicita_numero(condicao, ordem)
    return numero  # que agora é garantidamente inteiro

def verifica_positivo(numero,condicao,ordem):
    while numero<0:
        msg_erro(condicao)
        numero = solicita_numero(condicao, ordem)
    return numero  # que agora é garantidamente inteiro

def verifica_negativo(numero,condicao,ordem):
    while numero>0:
        msg_erro(condicao)
        numero = solicita_numero(condicao, ordem)
    return numero  # que agora é garantidamente inteiro

def verifica_igualdade(numero1,numero2,condicao,ordem):
    return numero1==numero2

def verifica_condicao(numero,condicao,ordem):
    if condicao=="inteiro":
        numero=verifica_inteiro(numero,condicao,ordem)
    elif condicao=="decimal":
        numero = verifica_decimal(numero,condicao,ordem)
    elif condicao=="par":
        numero = verifica_par(numero,condicao,ordem)
    elif condicao=="impar":
        numero = verifica_impar(numero,condicao,ordem)
    elif condicao=="positivo":
        numero = verifica_positivo(numero,condicao,ordem)
    elif condicao=="negativo":
        numero = verifica_negativo(numero,condicao,ordem)
    else:
        print("condição inválida!")
    return numero

def input_numero(condicao,ordem):
    if condicao!="igualdade":
        numero = solicita_numero(condicao, ordem)
        numero = verifica_condicao(numero, condicao, ordem)
        return numero
    else:
        n1=float(input ("Diga um primeiro numero para ser comparado"))
        n2 = float(input("Diga um segundo numero para ser comparado"))
        return verifica_igualdade(n1,n2,condicao,ordem)


n1=input_numero("igualdade",1)
print(n1)

# isto que vocês fizeram funciona para combinação
# de condições?
### se não, como implementamos a escolha combinada?