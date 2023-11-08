#construir um script que altera o valor da média na tabela
from utils_aula33 import *

#início = conectar
login, senha = retorna_credenciais()
conn = conecta_ao_banco(login, senha)
cursor = conn.cursor()

#pegar valores atuais da tabela
tabela = read_table(cursor)

#variável de memória para "lembrar" as linhas que já passaram
soma = 0

#loop para alterar todas as linhas
for contador in range(len(tabela)):
    #preciso calcular a média correta
    linha = tabela[contador]
    #EXERCÍCIO1: CALCULAR A MÉDIA CORRETA
    temp_atual = linha[1]
    soma += float(temp_atual)
    media_t = soma/(contador + 1)
    dia = linha[0]
    # centro = efetivamente executar o comando
    altera_linha(cursor, conn, media_t, dia, "MEDIA_T")

#fim: encerrar
cursor.close()
conn.close()