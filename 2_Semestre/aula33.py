#https://home.openweathermap.org/users/sign_up

import cx_Oracle
import json
from utils_aula33 import *

#primeiros passos: conexão e cursor
login, senha = retorna_credenciais()
conn = conecta_ao_banco(login, senha)
cursor = conn.cursor()

# estrutura principal (manipulação da tabela)

#incluir um valor
#cursor.execute("INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1, :valor2)",
#               valor1=3, valor2="Paulo")

#Eu posso entregar os valores no formato de tupla:
# posso também criar uma variável contendo esta tupla
# e, por último, agrupar tudo em uma função
#insert(cursor, conn, 3, "Paulo")

#alterar
#alterar(cursor,conn,id,nome)

#remover
#remover(cursor,conn,id)

#ler
linhas = ler_tudo(cursor,conn)
verifica_conteudo(linhas)

# último passo: fechar tudo
cursor.close()
conn.close()


#EXERCÍCIO:
'''
campos da tabela:
Data (chave primária)
Temp. atual
DeltaT do dia
clima atual
clima de hoje igual ao de ontem?
média de temperatura histórica

script SQL: 
CREATE TABLE CLIMA(
DATA_DIA   VARCHAR(255)  NOT NULL PRIMARY KEY
,TEMP VARCHAR(255) NOT NULL,
DELTA_T VARCHAR(255) NOT NULL,
CLIMA_DIA VARCHAR(255) NOT NULL,
CLIMA_IGUAL VARCHAR(255) NOT NULL,
MEDIA_T VARCHAR(255) NOT NULL
)
'''
# EXERCÍCIO:
# pegar uma API_KEY
# https://home.openweathermap.org/users/sign_up

# pensar no pseudo-código (fluxograma) para este sistema que imaginamos
# pegar a previsão do tempo via API, guardar no banco, no dia seguinte comparar com o que realmente aconteceu,
# e gerar uma flag de se a previsão acertou