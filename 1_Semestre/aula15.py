## COMENTÁRIO SOBRE A PROVA

# n1=float(input("Diga um número positivo e inteiro"))
#
# #inteiro e positivo
#
# ## lógica "invertida" (escrevemos o que não queremos)
# while n1//1!=n1 or n1<0:  #eu escrevo o que eu não quero
#     print("Este número nao atende às caraterísticas")
#     n1=float(input("Diga um número positivo e inteiro"))
#
# ## para usar a lógica direta, começamos com o while True
# while True: #loop infinito
#     if n1//1==n1 and n1>0: break  #escrevo o que eu quero
#     else:
#         print("Este número nao atende às caraterísticas")
#         n1=float(input("Diga um número positivo e inteiro"))
#
#
#
# #########################################################
# while n1//1!=n1:
#     print("Este número nao é inteiro")
#     n1=float(input("Diga um número positivo e inteiro"))
#
# #SAIU DO LOOP  DA LINHA 22 (verificação de inteiro)
# #então, ao fazer o loop abaixo, ele não vai mais verificar se é inteiro
# while n1<0:
#     print("Este número nao é positivo")
#     n1=float(input("Diga um número positivo e inteiro"))
#
# print(n1)
#
# # para saber exatamente qual a característica que não foi atendida,
# # temos que usar estruturas de decisão condicionais (if/else)
#
# while n1//1!=n1 or n1<0:  #quando não temos situações mutualmente excludentes, temos que começar com a mais restritiva
# #pois na estrutura if/elif/else, apenas 1 condição vai ser executada
#     if n1//1!=n1 and n1<0: #o número é decimal E negativo
#         print("Você digitou um número decimal E negativo")
#         n1 = float(input("Diga um número positivo e inteiro"))
#     elif n1<0:#o número é negativo ( e inteiro)
#         print("Você digitou um número negativo")
#         n1 = float(input("Diga um número positivo e inteiro"))
#     else:#o número é decimal (e positivo)
#         print("Você digitou um número decimal")
#         n1 = float(input("Diga um número positivo e inteiro"))
#
#
# ## loop "dentro de loop" (nested)
#
# #tabuada de 0 a n2, de todos os números de 1 a n1
# n1=int(input("Diga um número inteiro e positivo: "))
# n2=int(input("Diga outro número inteiro e positivo: "))
# for i in range(0,n2+1):# cria uma lista [0,1,2,...n2], e o 'i' vai assumir cada um desses valores, nesta ordem
#     for j in range(1,n1+1): #eu tenho que trocar o contador
#         print(i*j)
#
# #fazendo com while:
#
# # transformando 'for i in range(0,n2+1):' em while:
# i=0
# while i<=n2:
#     [...]
#     i+=1
#
# # transformando 'for j in range(1,n1+1)' em while:
# j=1
# while j<=n1:
#     [...]
#     j+=1
#
# #juntando os 2
# i=0
#
# #só while me da a liberdade de controlar (repetir ou avançar) o andamento do meu loop
# while i<=n2:
#     j = 1 #o contador do segundo loop tem que ficar dentro do primeiro para ser resetado
#     while j <= n1:
#         if "condição que eu quero que aconteça de novo":
#             continue #volta para o começo deste loop (linha 78)
#         elif "condição que eu quero pular o próximo":
#             j+=2
#         else: #condição que eu não quero que repita
#             j += 1
#     #o contador do primeiro loop tem que ser FORA do segundo
#     i+=1


## FUNÇÕES E PROCEDIMENTOS: conjunto de instruções
# uma função RETORNA alguma coisa; um procedimento, não

#criando uma função (básica): def (definição)
'''sintaxe:
- função:
def nome_da_função(argumentos):
    instruções #quantas quiser
    [...]
    return variável(eis)

-procedimento:
def nome_da_função(argumentos):
    instruções #quantas quiser. Ex: print, salvar um arquivo, escrever no banco de dados, enviar uma chamada de api,chamar uma função, etc
    [...]

obs: o nome da função não pode ter espaços nem caracteres especiais (além do _ )
são as mesmas condições para nome de variável

obs2: um dos objetivos de agrupar suas linhas de código em funções é para
organizar seu código. Por isto, é uma boa prática adotada amplamente,
definir todas as funções no começo do código, e ir chamando conforme o necessário
Além disto, é bom dar nomes intuitivos para as funções

LEMBRANDO QUE: a definição TEM QUE VIR ANTES do chamado
(o python, por ser um linguagem interpretada, não possui void nem ponteiro)
'''

# criando procedimento que imprime a soma de dois valores:
def imprime_soma_dos_valores(a,b):  #estou apenas definindo a função/procedimento. Não estou criando variáveis
    print(f"A soma dos valores digitados ({a} e {b}) é: ",a+b)

# utilizando o procedimento criado: #aqui eu preciso passar valores e/ou variáveis
# n1=float(input("Diga o primeiro numero"))
# n2=float(input("Diga o segundo numero"))
# imprime_soma_dos_valores(n1,n2)
# print()
#criando procedimento que imprime a soma de dois valores dados pelo usuário:
# def print_valores_do_usuario(): #eu posso ter função/procedimento sem argumentos
#     n1 = float(input("Diga o primeiro numero"))
#     n2 = float(input("Diga o segundo numero"))
#     print("A soma dos valores digitados é: ",n1+n2)
#
# print_valores_do_usuario()

#eu posso ter uma função chamando outra função


def print_valores_do_usuario_2(): #eu posso ter função/procedimento sem argumentos
    n1 = float(input("Diga o primeiro numero"))
    n2 = float(input("Diga o segundo numero"))
    imprime_soma_dos_valores(n1, n2)
