'''
BUSCA em listas ordenadas

Para encontrar um item em uma lista ordenada, podemos utilizar a
busca BINÁRIA, que consiste em sempre comparar se o item a ser encontrado
é maior que o valor correspondente ao índice do meio da lista,
o que gera uma resposta binária:
True ou False

Com isto, independente do tamanho da lista, temos uma quantidade máxima
fixade tentativas até encontrar o item ou chegar à conclusão que
ele não existe

Ex: encontrar um minuto exato 26 num relógio (0-59)
 - 1.1: comparamos com o valor do índice do meio: 29 -> False
 - 1.2: pegar a metade correspondente da lista: 0-29
 - 2.1: comparamos com o valor do índice do meio: 14 -> True
 - 2.2: pegar a metade correspondente da lista: 15-29
 - 3.1: comparamos com o valor do índice do meio: 21 -> True
 - 3.2: pegar a metade correspondente da lista: 21-29
 - 4.1: comparamos com o valor do índice do meio: 25 -> True
 - 4.2: pegar a metade correspondente da lista: 25-29
 - 5.1: comparamos com o valor do índice do meio: 27 -> False
 - 5.2: pegar a metade correpondente da lista: 25-27
 - 6.1: comparamos com o valor do índice do meio: 26 -> False
 - 6.2: pegar a metade correpondente da lista: 25-26
 - 7.1: comparamos com o valor do índice do meio: 25 -> True
 - 7.2: pegar a metade correpondente da lista: 26 <- ENTRAR COM CRITÉRIO DE PARADA

'''
#Vamos colocar isto em pyton
# (implementar uma busca binária em uma lista ORDENADA)
lista = [i for i in range(10)]
target = 7

resposta = 0
for i in range(len(lista)): #todo verificar se utilizamos o i
    indice_meio = len(lista)//2
    valor_do_meio = lista[indice_meio]
    if target > valor_do_meio:
        lista = lista[indice_meio:]
        resposta += indice_meio  # todo como utilizar esta resposta (e se ela fica aqui)
    elif target == valor_do_meio: #todo pensar quando não tem na lista
        print("encontrado no índice",indice_meio)
        break
    else:
        lista = lista[:indice_meio]

#EXERCÍCIO: resolver os todos e quaisquer outros que apareçam



# EXERCÍCIOS PARA O CHECKPOINT:

'''
1) Crie uma função que receba como parâmetros o nome e o número do mês de aniversário de uma pessoa
Essa função deverá criar um dicionário com esta pessoa, da seguinte forma:
{"Nome": nome , "Aniversario": mes} , onde o mes deverá ser escrito em forma de palavra de 3 letras (jan,fev,mar etc)
E adicione este nome a uma lista de nomes em um arquivo txt.

Antes de salvar a lista em um arquivo txt, a função deverá salvar cada dicionário individualmente em um arquivo JSON,
cujo nome deverá ser "nome_mes.json"

2) Utiliando o os.listdir() no caminho onde foram salvos os arquivos json, 
faça um loop que carregue todos (um por um) e os coloque em uma nova lista de nomes

'''