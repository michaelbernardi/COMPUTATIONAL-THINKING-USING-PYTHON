#CHECKPOINT 1 : 04/SET
'''
lista_de_alunos = []
lista_de_turmas = []

def adiciona_aluno(nome, curso, lista_de_alunos):

    dicio_aluno = {
        "Nome": nome,
        "Curso": curso,
        "RM": len(lista_de_alunos)+1
    }
    lista_de_alunos.append(dicio_aluno)

def adiciona_turma(lista_de_alunos):
    for aluno in lista_de_alunos:
        # {"Nome": "Fulano", "Curso": "TDS", "RM":123}
        curso = aluno["Curso"]
        nome = aluno["Nome"]
        rm = aluno["RM"]
        if rm % 2 == 0: #turma W
            turma = "1"+curso+"W"
        else: #turma X
            turma = "1"+curso+"X"

        dicio_turma = {
            "Nome": nome,
            "RM": rm,
            "Turma": turma
        }
        lista_de_turmas.append(dicio_turma)

#EXERCÍCICIO
# utilizando as funções acima, crie uma lista de alunos com 5 alunos
# e os salve em um arquivo txt , um aluno por linha
# após isto, crie uma rotina que leia os alunos deste aquivo, passe pela função
# adiciona turma, e salve, um aluno por linha, em um outro arquivo txt

# criar os alunos (5)
adiciona_aluno("Fulano", "TDS", lista_de_alunos)
adiciona_aluno("Ciclano", "ADM", lista_de_alunos)
adiciona_aluno("Beltrano", "BDO", lista_de_alunos)
adiciona_aluno("Paulo", "ESO", lista_de_alunos)
adiciona_aluno("Fualo", "TDS", lista_de_alunos)
#print(lista_de_alunos)

# salvar a lista (um por linha)
with open("lista_do_exercicio.txt","w") as arquivo:
    for i in lista_de_alunos:
        arquivo.write(str(i))
        arquivo.write("\n")

# ler este aqrquivo
with open("lista_do_exercicio.txt","r") as arquivo:
    lista_lida = arquivo.readlines()
#print(lista_lida)

#converter
import ast
lista_convertida = []
for i in lista_lida:
    dicionario_convertido = ast.literal_eval(i)
    lista_convertida.append(dicionario_convertido)
#print(lista_convertida)

# utilizar a função "adiciona_turma"
adiciona_turma(lista_convertida)
#print(lista_de_turmas)

# salvar a lista das turmas (em um arquivo novo)
with open("lista_de_turmas.txt","w") as arquivo:
    for i in lista_de_turmas:
        arquivo.write(str(i))
        arquivo.write("\n")
'''

# JSON = JavaScript Object Notation
#é um formato universal, e é muito utilizado para trocar informações através de plataformas
#ex: API
# no python, funciona como um dicionário, através da sua biblioteca própria
import json
dicio = {
    "user": "Paulo",
    "password": 123
}

#para escrever o json EM UM ARQUIVO, utilizamos o DUMP
with open("exemplo.json","w") as arquivo:
    json.dump(dicio,arquivo)

#para ler o json DE UM ARQUIVO, utilizamos o LOAD
with open("exemplo.json","r") as arquivo:
    dicio_lido = json.load(arquivo)
print(dicio_lido.keys())

# para converter para o formato string de JSON, utilizamos o DUMPS (s=string)
#ou seja, cria uma string (<class 'str'>) sem perder as propriedades,
#como acontece quando eu uso str(dicio)

#apenas dentro do python!
ex_dumps = json.dumps(dicio)
print(ex_dumps)
print(type(ex_dumps))
print()
# para converter do formato string de JSON para dicio, utilizamos o LOADS (s=string)
#apenas dentro do python!
ex_loads = json.loads(ex_dumps)
print(ex_loads)
print(type(ex_loads))

'''
ORDENAÇÃO de listas
 - processo intuitivo:
    * percorrer a lista
    * comparo len(lista)-1 vezes -> descubro o maior OU o menor
    * trago o menor para a primeira posição OU o maior para a última posição
    * comparo len(lista)-2 vezes -> descubro o segundo maior OU segundo menor
    * trago o 2º menor para a 2º posição OU o 2º maior para a penúltima posição

este raciocínio intuitivo é chamado de SELECTION SORT
[1,0,5,3,9,8] -> [0,1,5,3,9,8] -> [0,1,3,5,9,8] -> [0,1,3,5,8,9]

 - uma segunda forma de pensar 
    * percorrer a lista
    * selecionar um item e comparar com seu vizinho
    * caso seja maior, trocar. caso não seja, andar para o lado
    * ao chegar ao final, voltar ao começo da lista
    * caso eu não efetue nenhuma troca, a lista está ordenada
[1,0,5,3,9,8] -> [0,1,5,3,9,8] -> [0,1,3,5,9,8] -> [0,1,3,5,8,9]
'''
lista1 = [1,0,5,3,9,8]
lista2 = [1,0,5,3,9,8]

#EXERCÍCIOS:
#1) vamos programar o selection sort


#2) vamos programar o bubble sort

# BUSCA em listas