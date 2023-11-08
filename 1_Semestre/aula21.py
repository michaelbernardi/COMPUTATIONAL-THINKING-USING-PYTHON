### ORDENANDO A LISTA

#lista=[5,1,3,7,4,9]
## temos duas opções: lista.sort() e sorted(lista)
# a primeira, reorganiza a lista inteira (ou seja, perdemos a configuração inicial da lista)
# por isto, ela não retorna nada
# não existe uma forma de eu voltar à configuração original
## Obs: a função sort tem um argumento "reverse" (que é pré-definido como False), para caso eu queira a função ordenada de forma decrescente
# print(lista.sort(reverse=True))  #None
# print(lista)

# na segunda, é RETORNADA uma lista nova, ordenada
# então, para utilizarmos esta lista nova, temos que salvar em uma varíavel de memória
#lista=[5,1,3,7,4,9]
# print(sorted(lista))  #lista ordenada
# lista_ordenada = sorted(lista)
# print(lista)
# print(lista_ordenada)

#---------------------
### REVERSE
#literalmente reverte a lista (SEM ORDENAR)
# lembrando que faz em cima da lista original

#lista=[5,1,3,7,4,9]
#lista.reverse()
#print(lista)

#-------------------------
### para não perder a informação original, podemos criar uma cópia da lista:
### lista_backup = lista.copy()


#-------------------------
### EXTEND E +
## para adicionar mais de 1 item à lista, podemos utilizar o extend e a soma de listas

## para utilizar o extend, eu passo uma lista, que será interpretada como itens individuais
# lista=[]
# lista.append([5,5]) #estou adicionando apenas 1 elemento, e este elemento é uma lista com 2 itens
# print(lista)
# lista.extend([5,5,6,7,8,9]) #estou adicionando 2 elementos separados
# print(lista)
# print("O primeiro item da lista é ",lista[0])
# print("O segundo item da lista é ",lista[1])
# print('-'*30)
# ## podemos também concatenar listas utilizando o símbolo +
# lista1=[1,2,3]
# lista2=[4,5,6]
# print(lista1+lista2)
# print(lista1)
# #para salvar a concatenação, eu tenho que colocar numa variável de memória
# lista1+=lista2
# #ou
# lista3=lista1+lista2

#----------------------------------
### INSERT
#adiciona um item à lista, no ANTES do índice especificado
# lista=[1,2,3,4,5]
# lista.append(6)
# print(lista)
# lista.insert(2,6) #o número 6 vai passar a ser o índice 2
# print(lista)
# lista.insert(40,9)  #como a lista não tem 40 elementos, ele vai colocar ao final da lista; e não vai criar a quantiadade de elementos necessária para chegar a 40 elementos
# print(lista)
# print("-"*30)
#obs: o insert adiciona um número à lista, e não modifica o valor que estava naquele índice


### INDEX
#localizar o índice da PRIMEIRA ocorrência de um determinado valor
#esta função não inclui um pré-tratamento de existência do valor
#print("O índice em que o valor 6 ocorre pela primeira vez é:",lista.index(6))
## print("O índice em que o valor 10 ocorre pela primeira vez é:",lista.index(10)) #ERRO

### VERIFICANDO SE UM ITEM EXISTE NA LISTA: in (dentro)
# print(10 in lista)
# print(6 in lista)
# print("-"*30)
# if 10 in lista:
#     print("O índice em que o valor 6 ocorre pela primeira vez é:",lista.index(10))
# else:
#     print("Não há 10 na lista")
#
# if 6 in lista:
#     print("O índice em que o valor 6 ocorre pela primeira vez é:",lista.index(6))
# else:
#     print("Não há 6 na lista")
#
# ### COUNT
# print("-" * 30)
# #literalmente conta quantas vezes o item ocorre na lista
# print("O numero 6 aparece", lista.count(6), "vezes na lista")
# print("O numero 10 aparece", lista.count(10), "vezes na lista")
# print("O numero 1 aparece", lista.count(1), "vezes na lista")


## EXERCÍCIOS:

# 1) vamos remover todos os '5', utilizando o while
lista=[1,5,7,5,5,9,6,87,4,5] # len(lista)=10. Último índice = 9
# i=0
# while i<len(lista): #todas as vezes que o loop chegar ao final e retornar para cá, ele vai calcular o len ATUAL da lista
#     item_atual=lista[i] #não posso cravar um índice
#     if item_atual==5:
#         lista.remove(5)
#         i-=1
#     i+=1
print("Lista antes da função:",lista)

# 2)transforme esta rotina em uma função que receba como argumentos a lista
# e o número a ser removido
# E, antes de executar o loop, verifique se o número existe na lista

def remove_numero(lista,num):
    if num in lista:
        i = 0
        while i < len(lista):  # todas as vezes que o loop chegar ao final e retornar para cá, ele vai calcular o len ATUAL da lista
            item_atual = lista[i]  # não posso cravar um índice
            if item_atual == num:
                lista.remove(num)
                i -= 1
            i += 1
    else:
        print("o número não está na lista")

# remove_numero(lista,5)
# print("Lista após a função:",lista)
#apesar de não ter retorno na função, pelo fato do remove alterar a lista original,
# este processo de remoção já fica automaticamente salvo na lista


# 3) trocar o último elemento com o primeiro de uma lista
lista=[1,5,7,5,5,9,6,87,4,5]

lista[0] #primeiro item
lista[-1] #último item
#
#preciso salvar o primeiro item antes de alterar
# lembrando que copy é apenas para listas
# primeiro_item=lista[0]
# lista[0]=lista[-1] #substituo o valor do primeiro pelo do último
# print("lista após a primeira troca:",lista)
# lista[-1]=primeiro_item
# print("lista ao final das mudanças",lista)

# 4) Crie uma função que encontre e retorne o menor e o maior valor da lista, e seus índices
lista=[1,5,7,5,5,9,6,87,4,5]

def encontra_maior_menor_valor(lista):
    menor_valor_da_lista = float("inf")  #maior valor possível em python
    maior_valor_da_lista = float("-inf") #menor valor possível em python
    for i in lista: #percorre os valores da lista, e não os índices
        if i<menor_valor_da_lista:
            menor_valor_da_lista=i
        if i>maior_valor_da_lista:
            maior_valor_da_lista=i
    #como eu não alterei a lista, mas sim criei valores novos, eu preciso do return
    return menor_valor_da_lista,maior_valor_da_lista,\
        lista.index(menor_valor_da_lista),lista.index(maior_valor_da_lista)

menor_valor,maior_valor,indice_menor_valor,indice_maior_valor=encontra_maior_menor_valor(lista)
print(menor_valor,maior_valor,indice_menor_valor,indice_maior_valor)
