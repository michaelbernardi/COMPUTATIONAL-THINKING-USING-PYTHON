import cx_Oracle
import json
import requests

key = 'eb77175f4214ced770e5350d142b9161'

lat = -23.563886
lon = -46.6529712
units = "metric"
endpoint = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={key}'


DICIO_ERROS={
    400: "Error 400 - Bad Request. \nYou can get 400 error if either some mandatory parameters in the request are missing or some of request parameters have incorrect format or values out of allowed range. \nList of all parameters names that are missing or incorrect will be returned in `parameters`attribute of the `ErrorResponse` object.",
    401: "Error 401 - Unauthorized. ",
    404: "Error 404 - Not Found. ",
    429: "Error 429 - Too Many Requests"
}#lista de erros desta api: https://openweathermap.org/api/one-call-3#popularerrors

def conecta_banco(login,senha,dsn):
    try:
        conn = cx_Oracle.connect(user=login, password=senha, dsn=dsn)
        print("conectado na primeira tentativa")

    except Exception as ex:
        print(f"Erro ({ex}) da primeira tentativa...tentano segunda forma")
        cx_Oracle.init_oracle_client(lib_dir=r"P:\instantclient-basic-windows.x64-21.11.0.0.0dbru\instantclient_21_11")
        conn = cx_Oracle.connect(user=login, password=senha, dsn=dsn)
    finally:
        print("Conectado!")
    
    return conn
#-----------------------------------------------------

def cria_dsn(host,port,sid):
    dsn = cx_Oracle.makedsn(host=host, port=port, sid=sid)
    return dsn

def carrega_credenciais(path = "senha_fake.json"):
    with open(path,"r") as arquivo:
        dados = json.load(arquivo)
    login = dados["login"]
    senha = dados["senha"]

    return login,senha

#limpar a tabela (CUIDADO, ISTO SEMPRE LIMPA TODA A TABELA!)
def limpa_tabela_toda(cursor,conn,tabela = "TB_USUARIO"): #o ideal é usar o WHERE e passar valores
    cursor.execute(f"DELETE FROM {tabela}")
    conn.commit()

def create(cursor,conn,id, nome):
    while True:
        try:
            valores = (id, nome)
            query = "INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1, :valor2)"
            cursor.execute(query, valores)
            conn.commit()
            break
        except cx_Oracle.IntegrityError as ex:
            print("XXXX - Não foi possível inserir neste ID. ID já existente na tabela!")
            id = int(input("--> Escolha um novo valor para ID: "))
            #print("XXXX - Código = ",ex)

def update(cursor,conn,id, nome):
    valores = (nome,id)
    query = "UPDATE TB_USUARIO SET NOME=:valor1 WHERE ID=:valor2"
    cursor.execute(query, valores)
    conn.commit()

def delete(cursor,conn,id):
    valores = (id,) #tupla de tamanho 1
    query = "DELETE FROM TB_USUARIO WHERE ID=:valor1"
    cursor.execute(query, valores)
    conn.commit()

#função mais genérica, que requer a query como parâmetro
def cud(cursor,conn,query, valores):
    cursor.execute(query, valores)
    conn.commit()

def ler_tabela_toda(cursor):
    query = "SELECT * FROM CLIMA_X ORDER BY DATA_DIA"
    cursor.execute(query)
    linhas = cursor.fetchall()
    return linhas


def recebe_api(endpoint):
    resposta = requests.request("GET", endpoint)
    if resposta.status_code==200:
        print("Dados recebidos da API!")
    return resposta  # precisamos que seja 200

def manipula_resposta(resposta):
    print("processando dados da API...")
    resposta_json = resposta.json()
    # pegando os dados da chave "main"
    main = resposta_json["main"]
    temp = main["temp"]
    temp_min = main["temp_min"]
    temp_max = main["temp_max"]

    delta_t = temp_max - temp_min
    # pegando os dados da chave "weather"
    # lembrando que, pela documentação, vimos que é uma lista

    weather = resposta_json["weather"][0]
    clima = weather["main"]
    print(f"...finalizado!\n---- Dados colhidos: Temp = {temp}ºC; Delta T = {delta_t}ºC; clima = {clima}")
    return temp,delta_t,clima

def verifica_clima(quantidade_de_linhas, linhas_da_tabela, clima):
    if quantidade_de_linhas == 0:
        clima_igual = False
    else:
        ultima_linha = linhas_da_tabela[-1]
        print("ultima data no banco",ultima_linha[0])
        clima_ontem = ultima_linha[3] #posição 4 da nossa tabela
        clima_igual = clima_ontem == clima
    print("---> O clima de hoje é igual ao de ontem?", clima_igual)
    return clima_igual

def calcula_media_t(quantidade_de_linhas,linhas_da_tabela,temp):
    if quantidade_de_linhas == 0:
        media_t = temp
    else:
        #neste caso, é mais fácil fazer uma query específica para retornar apenas a temp
        #como temos uma query genérica, temos que interar pela resposta
        soma_temp = temp #para corrigir o fato de que a linha sempre é adicionada toda de uma vez
        for linha in linhas_da_tabela:
            temp_da_linha = linha[1]  #pensar em como tratar para caso tenhamos valores nulos
            soma_temp += float(temp_da_linha)
        media_t = soma_temp/(quantidade_de_linhas+1)
    print(f"---> Média de temperatura histórica para esta cidade:{media_t}ºC")

    return media_t

def escreve_na_tabela(cursor, conn, hoje, temp, delta_t, clima, clima_igual, media_t):
    print("Escrevendo os valores na tabela...")
    try:
        query = "INSERT INTO CLIMA_X (DATA_DIA, TEMP, DELTA_T, CLIMA_DIA, CLIMA_IGUAL, MEDIA_T) VALUES (:v,:v,:v,:v,:v,:v)"
        valores = (hoje, temp, delta_t, clima, clima_igual, media_t)
        cursor.execute(query, valores)
        conn.commit()
        print("...sucesso!")
    except cx_Oracle.IntegrityError:
        print(f"---> Informações do dia de hoje ({hoje}), já inseridas no banco!\nTente novamente amanhã!")

def escreve_na_tabela_localidade(cursor, conn,lista_com_valores):
    #alteramos a estrutura da tabela para receber a lista, e a trasformamos em tupla
    #caso não fosse desta forma, teríamos que quebrar manualmente a lista em variáveis,
    #para depois juntar novamente em uma tupla
    print("Escrevendo os valores na tabela...")
    try:
        query = "INSERT INTO CLIMA_X_CIDADE (DATA_DIA, TEMP, DELTA_T, CLIMA_DIA, CLIMA_IGUAL, MEDIA_T, LOCALIDADE) VALUES (:v,:v,:v,:v,:v,:v,:v)"
        valores = tuple(lista_com_valores) #transformando a lista em tupla para entregar os valores para a query
        cursor.execute(query, valores)
        conn.commit()
        print("...sucesso!")
    except cx_Oracle.IntegrityError:
        print(f"---> Informações do dia ({lista_com_valores[0]}), já inseridas no banco!\nTente novamente amanhã!")


def altera_media(cursor, conn, nova_media, data_a_mudar):
    query = "UPDATE CLIMA_X SET MEDIA_T=:v WHERE DATA_DIA=:v"
    #query = f"UPDATE CLIMA_X SET MEDIA_T={nova_media} WHERE DATA_DIA={data_a_mudar}"
    valores = (nova_media,data_a_mudar)
    cursor.execute(query,valores)
    conn.commit()

def altera_campo(cursor, conn, campo, novo_valor, data_a_mudar):
    query = f'UPDATE CLIMA_X SET {campo}=:v WHERE DATA_DIA=:v'
    valores = (novo_valor, data_a_mudar)
    cursor.execute(query, valores)
    conn.commit()

def corrige_medias(cursor, conn, linhas_da_tabela):
    try:
        qt_linhas = 0
        soma_t = 0
        campo = "MEDIA_T"
        for linha in linhas_da_tabela:
            qt_linhas += 1
            soma_t += float(linha[1]) #temperatura da linha. lembrando que vem como string
            data_a_mudar = linha[0] #é necessariamente o primeiro campo
            nova_media = soma_t/qt_linhas
            altera_campo(cursor, conn, campo, nova_media, data_a_mudar)
        print("Alterações efetuadas!\nTotal de linhas afetadas:",len(linhas_da_tabela))
    except Exception as ex:
        print("Erro ao alterar\n", ex)