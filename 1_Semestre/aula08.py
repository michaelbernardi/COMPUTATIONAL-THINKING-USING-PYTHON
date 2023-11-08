### comentários sobre a prova

# código solto (não deixem código solto para evitar erros)
nome1="Bruno"
nome2="Adalberto"
# nome1==nome2

# vezes e diferença

# > sem len
# print(nome1>nome2) #compara a letra, e não a quantidade de caracteres
# idade1=30
# idade2=20
# # else apenas para 1 if
# if idade1>idade2:
#     print('1')
# if idade2>idade1:
#     print('2')
# else: #vai entrar quando idade1>idade2 ou quando forem iguais
#     print('3')

# condição em uma linha
#se cada condição só tiver 1 ação, eu posso colocar na mesma linha
# if idade1>idade2: print('1')
# if idade2>idade1: print('2')
# else: print('3')

# conselho: fazer as variáveis dentro dos if/else
# dif=idade2-idade1
# dif2=idade1-idade2
#
# if idade2>idade1:
#     dif=idade2-idade1
# else:
#     dif=idade1-idade2


# testem o código!! pensem nos casos extremos






### ELIF (ou então....)


idade1=30
idade2=20

idade3=20
#
# if idade3>idade1:
#     print("idade 3 > idade 1")
# elif idade1>idade3>idade2:
# #elif idade3<idade1 and idade3>idade2: # se idade 3 está entre as outras duas
#     print("idade 3({}) está entre as 2( {} e {} )"\
#           .format(idade3,idade1,idade2))
# elif idade3==idade2:
#     print("idade 3 = idade2")
# elif idade1==idade3:
#     print("idade 1 = idade3")
# elif idade3==idade1==idade2:
#     print("todas as idades são iguais")
# else: # se a idade 3 é menor que as outras duas:
#     print ("idade 3 menor que as outras 2")
#


# if 1>0:
#     print("1")
# elif 2>0:
#     print("2")
# elif 3>0:
#     print("3")
# else:
#     print("4")

#é diferente de :
# if 1>0:
#     print("1")
# if 2>0:
#     print("2")
# if 3>0:
#     print("3")
# else:
#     print("4")

# if idade1>idade2:
#     dif=idade1-idade2
# elif idade2>idade1:
#     dif=idade2-idade1
# else:
#     print("as idades são iguais")


# 1) [0.25pt] Solicite o nome do usuário e de uma outra pessoa
# a. A partir de agora, todas as menções a cada um
# (usuário ou outra pessoa) deverão ser pelo nome
#
nome1=input("Diga o seu nome")
nome2=input("Diga o nome de uma outra pessoa")

tamanho_do_nome1 =len(nome1)
tamanho_do_nome2 =len(nome2)
# 2) [1.5pt] Caso a quantidade de caracteres seja diferente,
# diga quantas vezes o nome maior
# (em quantidade de caracteres) é maior que o menor,
# utilizando um número inteiro
# e caso sejam iguais, diga apenas que são iguais

if tamanho_do_nome1==tamanho_do_nome2:
    print(f"{nome1} e {nome2} tem tamanho igual")
elif tamanho_do_nome1>tamanho_do_nome2:
    # opção 1 (casting):
    vezes= tamanho_do_nome1/tamanho_do_nome2
    vezes=int(vezes)
    #opção 2(divisão inteira)- lembrando que nessa opção , eu não tenho acesso ao valor original
    vezes= tamanho_do_nome1//tamanho_do_nome2
    print(f"O nome {nome1} é {vezes} vezes maior que o nome {nome2}")
else: #tamanho_do_nome1<tamanho_do_nome2
    vezes = int(tamanho_do_nome2/tamanho_do_nome1)
    print(f"O nome {nome2} é {vezes} vezes maior que o nome {nome1}")


if tamanho_do_nome1>tamanho_do_nome2:
    vezes=tamanho_do_nome1//tamanho_do_nome2
    print(f"O nome {nome1} é {vezes} vezes maior que o nome {nome2}")
elif tamanho_do_nome1==tamanho_do_nome2:
    print(f"{nome1} e {nome2} tem tamanho igual")
else:#tamanho_do_nome1<tamanho_do_nome2
    vezes = int(tamanho_do_nome2/tamanho_do_nome1)
    print(f"O nome {nome2} é {vezes} vezes maior que o nome {nome1}")
