'''#EXERCÍCIO:
# como vocês manipulariam uma string contendo um dicionário para formar um dicionário?

ex = "{'Nome': 'Fulano', 'Curso': 'TDS', 'RM': 1}"
quebra = ex.split(",")
dicionario_linha = {}
for i in quebra:
    if i == quebra[0]: #isolei a abertura da chave
        #opção 1:
        #print(i.split("{")[-1]) #quebrando a string na abertua de chave '{' e pegando o segundo item
        #opção 2:
        #criando uma string nova sem o primeiro item da string
        i_temp = i[1:]

        #quebrando esta string nos ':'
        quebra_temp = i_temp.split(":")
        #print(quebra_temp)

        #com esta quebra, temos uma lista com 2 itens
        #o primeiro é a chave (ex: 'Nome')
        #o segundo é o valor (ex: "Fulano")
        chave = quebra_temp[0]
        valor = quebra_temp[1]

        #incluindo no dicionário
        dicionario_linha[chave] = valor
    elif i == quebra[-1]: #isolei o fechamento da chave
        #opção 1:
        #print(i.split("}")[0].split(":"))
        i_temp = i.split("}")[0]
        quebra_temp = i_temp.split(":")
        chave = quebra_temp[0]
        valor = quebra_temp[1]
        dicionario_linha[chave] = valor
        #opção 2:
        #print(i[:-1])criando uma string nova sem o último item da string
    else:
        quebra_temp = i.split(":")
        chave = quebra_temp[0]
        valor = quebra_temp[1]
        dicionario_linha[chave] = valor

print(dicionario_linha)
print(dicionario_linha.keys())

import ast
dicio = ast.literal_eval(ex)
print(dicio)

'''

# Lembrando da MANIPULAÇÃO DE TEXTOS:
#utilizamos a função open (abrir)
#temos 3 modos principais de abrir um arquivo:
## r = read (ler) -> apenas para arquivos existentes
## w = write (escrever) -> sempre ESVAZIA o arquivo ao abrir ; consigo CRIAR arquivos
## a = append (adicionar) -> adiciona ao FINAL do arquivo ; também cria arquivos

#temos também modificadores para estes modos: +
# lembrando que este modificador não altera a característica principal de cada modo
# ex: r+ não cria arquivos e tem o ponteiro no começo do arquivo
#       (ou seja, substitui os caracteres escritos, caso o seek não seja utilizado)
# w+ apaga todo o arquivo
with open("lista_de_alunos.txt",'a+') as arquivo:
    arquivo.write("teste")
    arquivo.write("\n")
    arquivo.write("teste")
    arquivo.write("\n")
    arquivo.write("teste")
    arquivo.write("\n")
    arquivo.write("teste")
    arquivo.write("\n")
    #arquivo.seek(0)
    #arquivo.write("ex")
    arquivo.seek(0)
    print(arquivo.readlines())

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