#construir um script que altera o valor da média na tabela
from utils_aula33 import *

#início = conectar
login, senha = retorna_credenciais()
conn = conecta_ao_banco(login, senha)
cursor = conn.cursor()

#pegar valores atuais da tabela
linhas = read_table(cursor)

#alterar todas as linhas
for linha in linhas:
    #preciso calcular a média correta

    #EXERCÍCIO1: CALCULAR A MÉDIA CORRETA
    media_t = ...
    dia = ...
    # centro = efetivamente executar o comando
    altera_linha(cursor, conn, media_t, dia)

#EXERCÍCIO 2: TRANSFORMAR A FUNÇÃO 'ALTERA LINHA' PARA QUE ACEITE A COLUNA COMO VARIÁVEL
#EXERCÍCIO 3: UTILIZAR ESTE SCRIPT PARA CORRIGIR A TABELA (testar!!!!)
#fim: encerrar
cursor.close()
conn.close()