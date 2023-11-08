
# EXERCÍCIOS PARA O CHECKPOINT:

'''
1) Crie uma função que receba como parâmetros o nome e 
o número do mês de aniversário de uma pessoa.
Esta função deverá criar um dicionário com esta pessoa, 
da seguinte forma:
{"Nome": nome , "Aniversario": mes} , 
onde o mes deverá ser escrito em forma de palavra de 3 letras 
(jan,fev,mar,...,dez etc) E adicione esta pessoa (dicionário) 
a um arquivo txt, cada um em uma linha. 
Este arquivo deve conter, ao final, todos os dicionários
criados (ou seja, sem perder informação)

Antes de salvar o dicionário em um arquivo txt,
a função deverá salvar cada dicionário individualmente em um 
arquivo JSON, cujo nome deverá ser "nome_mes.json"
Ex: "paulo_jun.json"
'''
def exercicio1(nome, num_mes):
    import json
    dicio_mes = {1:"jan", 2:"fev", 3:"mar", 4:"abr", 5:"mai", 6:"jun",
                7:"jul", 8:"ago", 9:"set", 10:"out", 11:"nov", 12:"dez"}
    mes_palavra = dicio_mes[num_mes]#estou entregando a chave para receber
                                    #o valor daquela chave
    #crio o dicionário
    dicio_pessoa = {"Nome": nome, "Aniversario": mes_palavra}

    #salvando em um arquivo json

    #opcao 1:
    # nome_do_json = nome+"_"+mes_palavra+".json"
    # with open(nome_do_json,"w") as arquivo_json:

    #opcao 2:
    #vamos abrir com o W, pois foi solicitado que seja 1 pessoa por arquivo
    with open(f"{nome}_{mes_palavra}.json","w") as arquivo_json:
        #a função dump necessita de 2 argumentos:
        #o item a ser salvo (dicionário)
        #o arquivo que vai receber o item (neste exemplo, arquivo_json)
        json.dump(dicio_pessoa, arquivo_json)

    #para escrever, eu abro o arquivo
    #neste caso, TEM que ser com o 'a', pois senão se eu abrir com o 'w',
    #vou estar apagando tudo o que tinha antes no arquivo
    with open("exercicio1.txt", "a") as arquivo_txt:
        arquivo_txt.write(str(dicio_pessoa)) #lembrando que só escrevo strings
        #como o enunciado pediu explicitamente um em cada linha,
        #temos que pular linha
        arquivo_txt.write("\n")


# exercicio1("Paulo", 6)
# exercicio1("Paula", 7)
# exercicio1("João", 7)
# exercicio1("Maria", 1)
# exercicio1("José", 11)
'''
2) Utilizando o os.listdir() no caminho onde foram salvos os arquivos json, 
faça um loop que carregue todos os arquivos json (um por um) 
e os coloque em uma nova lista de nomes
'''
import os
import json
caminho = os.getcwd() #função que retorna o CWD = current work directory
# (diretório atual de trabalho)
#print(caminho)
lista_arquivos = os.listdir(caminho)
#o listdir retorna uma lista com os nomes dos
#arquivos neste diretório

lista_nova = []
for i in lista_arquivos:
    nome_dividido = i.split(".") #quebrando a palavra onde aparecem '.' e retornando uma lista
    ext = nome_dividido[-1]  #isolando a extensão do arquivo (pegando a último item da lista para garantir caso o nome contenha outros '.'
    if ext == "json": #caso seja um arquivo json
        #'i' é apenas uma string com o nome do arquivo
        # eu tenho que abrir o arquivo, para poder ler
        with open(i, 'r') as arquivo:
            conteudo = json.load(arquivo) #salvei na memória o conteúdo do arquivo json
            # print(conteudo)
            # print(type(conteudo))
            # print()
            lista_nova.append(conteudo) #adicionei à minha lista o dicionário
print(lista_nova)