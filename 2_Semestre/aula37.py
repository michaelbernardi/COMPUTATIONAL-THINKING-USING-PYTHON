# Vamos criar uma tabela nova que contenha o campo cidade;
# Depois, vamos importar os dados da tabela atual para a nova,
# preenchendo o valor da localidade

'''
CREATE TABLE CLIMA_W_CIDADE(
DATA_DIA   VARCHAR(255)  NOT NULL PRIMARY KEY
,TEMP VARCHAR(255) ,
DELTA_T VARCHAR(255) ,
CLIMA_DIA VARCHAR(255) ,
CLIMA_IGUAL VARCHAR(255) ,
MEDIA_T VARCHAR(255) ,
LOCALIDADE VARCHAR(255)
)
'''

#etapas:
from utils_aula33 import *
# 0) concetar ao banco (a mesma conexão vai ser utilizada para as duas tabelas)

login, senha = retorna_credenciais()
conn = conecta_ao_banco(login, senha)
cursor = conn.cursor()

# 1) ler a tabela antiga

tabela = read_table(cursor)
# print(tabela) é importante conferir o conteúdo e os dados recebidos,
# principalmente quando estamos mexendo com 2 tabelas diferentes

# 2) adicionar o valor da cidade

# 2.1) pegar o valor da cidade:
#recebendo dados da API
lat = -23.5643758
lon = -46.6520313
unidade = 'metric'
endpoint = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unidade}&appid={key}')

resposta,status = get_resposta(endpoint)
localidade = resposta.json()["name"]
print(localidade)
# 2.2) loop para acessar todas as linhas e adicionar a cidade
#for contador in range(len(tabela)):
#    linha = tabela[contador]

# 3) escrever na nova tabela

# 4) ENCERRAR AS CONEXÕES!
cursor.close()
conn.close()

##EXERCÍCIO: Completar o script