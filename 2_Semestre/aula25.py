#EXERCÍCIOS:

#1) Crie uma função que receba um número inteiro positivo N como parâmetro
# (e que por padrão seja =1) e retorne um dicionário cujas chaves
# são os números de 0 até N, e os valores, seus quadrados
# ex: N=3, dict={0:0,1:1,2:4,3:9}

#dict={n:n**2}.

def n_quadrado(N=1):
    #dicio = {}
    #for n in range(N+1):
    #    dicio[n] = n**2

    dicio = {n:n**2 for n in range(N+1)} #a mesma coisa o loop de cima

    return dicio
dicio_ex_1 = n_quadrado()
#print(dicio_ex_1)

#2) Crie uma função que receba um dicionário e some e retorne
# seus valores numéricos
# Caso não exista nenhum, deverá imprimir uma mensagem de erro
def soma_numeros(dicio):
    resposta = 0
    validador = True
    for valor in dicio.values():

        if type(valor) == int or type(valor) == float:
            resposta += valor
            validador = False
    if validador:
        return "Erro! Não possui valores numéricos"
    else:
        return resposta

# print(soma_numeros(dicio_ex_1))
# print(soma_numeros({0:"0"}))
#3) Transforme duas listas de tamanhos iguais e um dicionário
# ex: ["cor","tampa"] e ["preta","branca"] viram {1:"um",2:"dois"}
lista1=["cor","tampa"]
lista2=["preta","branca"]
dicio = {}
for i in range(len(lista1)):
    chave = lista1[i]
    valor = lista2[i]
    dicio[chave] = valor

dicio2 = dict(zip(lista1, lista2)) #equivalente ao for acima
#
# print(dicio)
# print(dicio2)

#4) faça uma função que recebe um dicionário e
# qualquer número de chaves, e retorne um novo dicionário contendo
# apenas estas chaves (ou seja, que filtre um dicionário)
# ex:
dict1={"nome": "Fulano","idade": 25,"cidade": "Rio de Janeiro"}
#     chave = "nome"
#    retorno = {"nome":Fulano}
def filtra_dict(dicio,*args):
    dicio_resposta = {chave:valor for chave,valor in dicio.items() if chave in args}
    return dicio_resposta
print(filtra_dict(dict1,"nome","idade"))


#EXERCÍCIO:
# vamos criar uma função que adiciona um dicionário
# contendo o cadastro do aluno à lista de alunos
# porém, de forma que o RM seja único por aluno
#{"Nome": "Fulano", "Curso": "TDS", "RM":123}