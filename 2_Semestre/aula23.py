# Exercício da aula passada

# Crie uma função que encontre e retorne o menor e o maior valor da lista, e seus índices
## SEM utilizar a função nativa do python (min e max)
lista=[1,5,7,5,5,9,6,87,4,5]

def encontra_extremos(lista):
    maior = float("-inf")
    menor = float('inf')
    for i in lista:
        if i > maior:
            maior = i

        if i < menor:
            menor = i
    indice_maior = lista.index(maior)
    indice_menor = lista.index(menor)
    return maior, menor, indice_maior, indice_menor

# maior, menor, indice_maior, indice_menor = encontra_extremos(lista)
#
# print(f"O maior número é {maior}")
# print(f"O menor número é {menor}")
# print("o maior número da lista está na posição {}".format(indice_maior))
# print("o menor número da lista está na posição {}".format(indice_menor))


# TUPLAS

#são inalteráveis

lista=[1,5,7,5,5,9,6,87,4,5]
tupla=(1,5,7,5,5,9,6,87,4,5)

lista[0]=0
#print(lista)
#tupla[0]=0   #dá erro pois tupla não pode ser alterada

#a tupla possui as mesmas funções de lista que não a alterem
# print(len(tupla))
# print(tupla[0])

#posso transformar uma lista em tupla
tupla2=tuple(lista)
#tupla2[0]=7 #retorna erro pois foi transformada em tupla

#para criar uma tupla,eu preciso de uma vírgula
tupla_1 = (5) #não é tupla
tupla_2 = (5,)
tupla_3 = 5,2
tupla_4 = tupla_2 + tupla_3
# print(type(tupla_1))
# print(type(tupla_2))
# print(type(tupla_3))
# print()
# print(tupla_4)



# STRING

silaba1="le"
silaba2="tra"
#print(silaba1+silaba2)

string= "palavra"
# print(len(string))
# print(string[0])
# print(sorted(string))
# print(string)
#
sorted_string=sorted(string)

string_final="" #equivalente a lista_final = []

for i in sorted_string:
    string_final += i

palavra_sem_a_1 = "123".join(i for i in sorted_string if i != "a")

palavra_sem_a_2 = ""
for i in sorted_string:
    if i != "a":
        palavra_sem_a_2 += "123"+i
# print(palavra_sem_a_1)
# print(palavra_sem_a_2)


#exemplo em aberto:
# criar uma rotina que encontre arquivo da última aula, pegue seu número, adicione 1 e crie um arquivo python com esse novo nome

import os
lista_arquivos=os.listdir(r"C:\Users\paulo\PycharmProjects\ComputationalThinking\1TDSPW\1SEM")
print(lista_arquivos)

for i in lista_arquivos:
    lista_split = i.split(".")
    if lista_split[-1].lower() == "py":
        lista_split[0].__contains__("aula")

# EXERCÍCIO PARA A PRÓXIMA AULA
# Crie uma função que encontre e retorne o menor e o maior valor da lista, e seus índices
## SEM utilizar a função nativa do python (min e max);
## mas agora utilizando a função sort() de listas







