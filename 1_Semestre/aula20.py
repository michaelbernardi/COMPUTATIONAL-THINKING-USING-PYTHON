## COMENTÁRIOS SOBRE A PROVA

#diferença entre print e return
def imprime(n):
    print(f"{n:.3f}º")
#resposta=imprime(5.8523654)  #None

#é diferente de:
def imprime2(n):
    print(f"{n:.3f}º")
    return f"{n:.3f}º"
#resposta2=imprime2(5.8523654)  #5.852º

#imprime(9.84569)

# resultado=imprime2(7.8455)
# print(resultado)

#argumentos
def imprime3(n):
    n=100 #neste caso, está sobrescrevendo o que o usuário colocar ao chamar a função

##se você for utilizar input, crie uma função sem argumentos


##if com várias condições
#tem que colocar manualmente a variável todas as vezes
# while True:
#     palavra=input("Diga uma operação")
#     if palavra=="soma" or palavra=="subtracao" or palavra=="divisao":
#         break
#     print("escolha uma função válida")
# print(palavra)


#LISTAS
#criando uma lista vazia:
lista1=[]
#criando uma lista com itens:
lista2=[1,5,9]

#adicionando um elemento à lista: (ao final da lista)
# append
#print(lista1)
lista1.append(1)
#print(lista1)
lista1.append(5)
lista1.append("string")
lista1.append(lista2)
#print(lista1)
#print("---")
#acesso itens da minha lista através do índice
# lembrando que o índice começa do 0
#print(lista1[1])

#alterando itens da lista:
#localizar pelo índice e alterar
lista1[1]=9
#print("Lista 1 após alteração:",lista1)

#tamanho da lista = len(lista)
#print("a lista 1 tem {} itens".format(len(lista1)))

#pegando o último item utilizando o len
#tenho que descontar
tamanho_da_lista=len(lista1)
indice_do_ultimo_item=tamanho_da_lista-1
#print(lista1[indice_do_ultimo_item])

#acessando diretamente o último
#print(lista1[-1])


#acessar partes de lista(slices)
#print(lista1[0:2])  #eu escolho o ponto de partida e parada, lembrando que é igual ao range: para 1 antes do último


#se eu tiver apenas valores numéricos,
# posso utilizar o sum(lista) para somar todos os valores
lista_numeros=[5,7,94,5,.85,7956]
#print(sum(lista_numeros))

#se eu quiser a média dos números da lista:
media_da_lista=sum(lista_numeros)/len(lista_numeros)
#print(media_da_lista)

## retirando itens da lista: temos 2 opções
# lista=[1,4,9,7,9]
# print("lista original",lista)
# ### .pop() , onde escolhemos o ÍNDICE
# ### o .pop() RETORNA o valor retirado
# print(lista.pop(1))
# print("Lista após pop(1):,",lista)
# print("-"*20)
# ### .remove(), onde escolhemos o VALOR
# # (a primeira ocorrência)
# ###o .remove() NÃO retorna o valor
# print(lista.remove(9))
# print("lista após remove(9):",lista)

# removendo todas as ocorrências de um valor na lista
lista=[1,5,7,5,5,9,6,87,4,5]

lista_reserva=lista.copy() #cria uma cópia inteira da lista
# se você fizer apenas lista_reserva=lista ; ao alterar a lista, você altera a lista_reserva também


#vamos remover todos os '5'
# for i in range(len(lista)):
#     print("interação:",i)
#     print("avalição atual", lista[i])
#     if lista[i]==5:
#         lista_reserva.remove(5)
#     print("lista original após remoção:",lista)
#     print("lista reserva após remoção:", lista_reserva)
#     print()

#--------------
## EXERCÍCIO:FAZER COM O WHILE
#--------------
lista_intermediaria=lista1[3]
print(lista_intermediaria[1])
#é o mesmo que :
print(lista1[3][1])

#alterando o item da lista dentro da lista
lista1[3][1]="5"
print(lista1)
print(lista1[3])








