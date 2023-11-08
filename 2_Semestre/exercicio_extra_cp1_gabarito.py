'''
1)
Crie uma função que receba uma string como parâmetro
esta função deverá criar e reotrnar um dicionário novo onde as chaves
deste dicionário são as diferentes letras desta string; e os valores,
suas quantidades
'''
def cria_dicio(s):#recebe apenas um parâmetro (string)
    dicio = {}
    #lembrando que a string comporta-se como lista,
    #então podemos interar por ela como uma lista:
    for i in s: #para cada letra na palavra
        if i not in dicio.keys(): #caso ainda não seja uma chave
            dicio[i] = 1 # criamos a chave com valor 1
        else: #caso exista
            dicio[i] += 1 #somamos 1 ao valor
    return dicio #esta função tem que ter retorno pois, além de pedido no enunciado,
                 # caso não tivesse, nunca teríamos acesso a este dicionário fora da função

novo_dicio = cria_dicio("exemplo")
print(novo_dicio)

'''
2) utilize a função acima para criar pelo menos 3 dicionários, e
adicioná-los a uma lista
'''
lista = []
#basta darmos append no retorno da função
lista.append(cria_dicio("exemplo"))
lista.append(cria_dicio("palavra"))
lista.append(cria_dicio("teclado"))

# obs: podemos criar variáveis de memória para salvar o retorno da
# função antes do append. porém, teriam que ser 3 variáveis diferentes
dicio1 = cria_dicio("mouse")
dicio2 = cria_dicio("monitor")
dicio3 = cria_dicio("python")
#agora, podemos utilizar o extend, para adicionar mais de um item de um vez
#lembrando que para utilizar o extend, temos que entregar os itens via lista
lista.extend( [dicio1, dicio2, dicio3] )
print(lista)
'''
3) crie uma função que receba uma lista de dicionários como parâmetro,
e salve cada dicionário em um arquivo json único, cujo nome deverá ser
um contador criado por você que garanta que ele é único por lista
'''
def salva_lista(lista):
    import json
    id = 0 #vou utilizar este id como modificador único
    #vou incrementar 1 a cada lista que eu salvar
    nome_base = "dicio" #vou colocar este nome apenas para ter algo além do id
                        #obs: esta parte é opcional. poderia ser apenas o id

    for dicio in lista: #para cada item da lista (que é o dicionário)
        nome_arquivo = nome_base + str(id) + ".json" #lembrando que temos que transformar o id em string

        #salvando o json
        with open(nome_arquivo,"w") as arquivo: #lembrando que o 'w' cria, porém apaga tudo que tinha antes, caso o arquivo exista
            json.dump(dicio,arquivo) #lembrando que o dump recebe 2 argumentos:
                                     #o dicionário a ser salvo;
                                     #e o arquivo onde salvar

        #após salvar, temos que incrementar o contador:
        id += 1

    #lembrando que esta função não precisa de retorno, pois é
    #apenas para percorrer a lista e salvar os json


#para utilizar a função:
salva_lista(lista)