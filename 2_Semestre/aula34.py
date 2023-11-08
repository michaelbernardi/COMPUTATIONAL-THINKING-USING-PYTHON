# EXERCÍCIO:
# pegar uma API_KEY
# https://home.openweathermap.org/users/sign_up
key = 'eb77175f4214ced770e5350d142b9161'
# pensar no pseudo-código (fluxograma) para este sistema que imaginamos
# pegar o clima atual e a temperatura via API, guardar no banco,
# no dia seguinte comparar com o que realmente aconteceu,
# e gerar uma flag de se o clima mudou

from utils_aula33 import *
import requests
import json
import datetime
#pegando o dia de hoje
hoje = datetime.datetime.today()

#recebendo dados da API
lat = -23.5643758
lon = -46.6520313
unidade = 'metric'
endpoint = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unidade}&appid={key}')

#pegando a informação do clima atual
resposta = requests.request("GET",endpoint)
dados = resposta.json()
weather = dados["weather"][0] #porque esta API foi estruturada de forma que o weather é uma lista,
                            # e com os nossos parâmetros, ela só tem 1 elemento
clima_dia = weather["main"]
#print(clima_dia)

#pegando as informações de temperatura
main = dados["main"]
temp = main["temp"]
temp_min = main["temp_min"]
temp_max = main["temp_max"]
delta_t = temp_max - temp_min

#lendo a tabela
#primeiros passos: conexão e cursor
login, senha = retorna_credenciais()
conn = conecta_ao_banco(login, senha)
cursor = conn.cursor()

#pegando as informações da tabela toda
query = "SELECT * FROM CLIMA"
cursor.execute(query)
linhas = cursor.fetchall()

#pegando o clima de ontem para comparar
if len(linhas) == 0:
    clima_ontem = False
else:#para quando eu já tenho itens na tabela
    ontem = linhas[-1] #ontem será uma tupla seguindo a ordem dos campos da tabela
    clima_ontem = ontem[3] #isolei o quarto item da tabela (CLIMA_DIA)

clima_igual = clima_ontem == clima_dia # Ex: pensar em uma outra forma de criar o clima_igual

#calculando a média histórica da cidade

# soma_t = 0
# for linha in linhas:
#     temp_da_linha = linha[1]
#     soma_t += temp_da_linha
# media_t = soma_t / len(linhas)
#este script acima necessita de 2 correções. Ex: corrigir
#quando resolvermos este exercício, teremos o que precisamos para escrever uma linha no banco
media_t = 0

#vamos escrever no banco a linha de hoje
query_inserir = "INSERT INTO CLIMA (DATA_DIA, TEMP, DELTA_T, CLIMA_DIA, CLIMA_IGUAL, MEDIA_T) VALUES (:v, :v,:v, :v,:v, :v)"
valores= (hoje, temp, delta_t, clima_dia, clima_igual, media_t)
cursor.execute(query_inserir, valores)
conn.commit()

#Exercícios:
#Resolver os 2 ao longo do arquivo
#Pensar em pontos de evolução ou de possíveis problemas no nosso código






























