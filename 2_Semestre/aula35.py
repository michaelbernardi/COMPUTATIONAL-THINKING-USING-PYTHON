# EXERCÍCIO:
# pegar uma API_KEY
# https://home.openweathermap.org/users/sign_up
key = 'eb77175f4214ced770e5350d142b9161'
#key=""
# pensar no pseudo-código (fluxograma) para este sistema que imaginamos
# pegar o clima atual e a temperatura via API, guardar no banco,
# no dia seguinte comparar com o que realmente aconteceu,
# e gerar uma flag de se o clima mudou

from utils_aula33 import *
import requests
import json
import datetime
DICT_ERROS={
    400:"Error 400 - Bad Request. ",
    401:"Error 401 - Unauthorized",
    404:"Error 404 - Not Found. ",
    429:"Error 429 - Too Many Requests"
}

#pegando o dia de hoje
hoje = datetime.datetime.today()
dia_formatado = hoje.strftime("%d/%m/%Y")

#recebendo dados da API
lat = -23.5643758
lon = -46.6520313
unidade = 'metric'
endpoint = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unidade}&appid={key}')

resposta,status = get_resposta(endpoint)


#para efeito de testes, eu posso sobrescrever o restulado original por um que eu queira
#status = 429 #criando um erro para testar meu tratamento

if status == 200:
    temp, delta_t, clima_dia = get_valores(resposta)

    #lendo a tabela
    #primeiros passos: conexão e cursor
    print("Conctando ao banco...")
    login, senha = retorna_credenciais()
    conn = conecta_ao_banco(login, senha)
    cursor = conn.cursor()
    print("...conectado!")

    #pegando as informações da tabela toda
    linhas = read_table(cursor)

    #pegando o clima de ontem para comparar
    clima_igual = compara_clima(linhas,clima_dia)

    #calculando a média histórica da cidade
    media_t = get_media_t(linhas, temp)

    #confirmando os valores
    print("DATA_DIA, TEMP, DELTA_T, CLIMA_DIA, CLIMA_IGUAL, MEDIA_T")
    print(dia_formatado, "|", temp, "|", delta_t, "|", clima_dia, "|", clima_igual, "|", media_t)

    escreve_linha_hoja(hoje, temp, delta_t, clima_dia, clima_igual, media_t, cursor, conn, dia_formatado)

    #encerrando as conexões
    cursor.close()
    conn.close()

else:
    if status in DICT_ERROS.keys():
        print("Erro na API:",DICT_ERROS[status])
    else:
        print("Erro desconhecido. Consulte a documentação:\n https://openweathermap.org/api/one-call-3#popularerrors")
#Exercícios:
#Pensar em pontos de evolução ou de possíveis problemas no nosso código






























