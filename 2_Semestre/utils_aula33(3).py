import json
import cx_Oracle
import requests

DICT_ERROS = {
    400: "Error 400 - Bad Request. ",
    401: "Error 401 - Unauthorized",
    404: "Error 404 - Not Found. ",
    429: "Error 429 - Too Many Requests"
}

key = 'eb77175f4214ced770e5350d142b9161'

def retorna_credenciais(path = r"C:\Users\paulo\Desktop\credenciais.json"):
    with open(path, "r") as arquivo:
        dados = json.load(arquivo)
    login = dados["login"]
    senha = dados["senha"]

    return login, senha

def conecta_ao_banco(login,senha, host="oracle.fiap.com.br", port=1521, sid="ORCL"):
    dsn = cx_Oracle.makedsn(host=host, port=port, sid=sid)
    conn = cx_Oracle.connect(user=login, password=senha, dsn=dsn)
    return conn

def insert(cursor,conn,id,nome):
    while True:
        try:
            valores = (id,nome)
            cursor.execute("INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1, :valor2)",
                           valores)
            conn.commit()
            break
        except cx_Oracle.IntegrityError:
            print("ERRO! Você está tentando criar um ID já existente!")
            id = int(input("Escolha um novo valor de ID: "))

def remover(cursor,conn,id):
    query = "DELETE FROM TB_USUARIO WHERE ID=:valor1"
    valor = (id,) #obs: a função execute requer um interavel
    #então temos que criar uma tupla de tamanho 1
    cursor.execute(query, valor)
    conn.commit()

def alterar(cursor,conn,id,nome):
    query = "UPDATE TB_USUARIO SET NOME=:valor1 WHERE ID=:valor2"
    valor = (nome,id)
    cursor.execute(query, valor)
    conn.commit()

def ler_tudo(cursor,conn):
    query = "SELECT * FROM CLIMA"
    cursor.execute(query)
    linhas = cursor.fetchall()
    return linhas

def verifica_conteudo(linhas):
    print(f"Esta tabela possui {len(linhas)} linhas!\nSão elas:")
    for linha in linhas:
        print(linha)

def get_resposta(endpoint):
    print("Tentando receber informações...")
    try:
        #pegando a informação do clima atual
        resposta = requests.request("GET",endpoint)
        status = resposta.status_code
        print("...sucesso!")
    except:
        resposta = False
        status = 1000
    return resposta, status

def get_valores(resposta):
    print("Processando dados recebidos...")
    dados = resposta.json()
    weather = dados["weather"][0]  # porque esta API foi estruturada de forma que o weather é uma lista,
    # e com os nossos parâmetros, ela só tem 1 elemento
    clima_dia = weather["main"]
    # print(clima_dia)

    # pegando as informações de temperatura
    main = dados["main"]
    temp = main["temp"]
    temp_min = main["temp_min"]
    temp_max = main["temp_max"]
    delta_t = temp_max - temp_min
    print("...fim!")
    return temp, delta_t, clima_dia

def read_table(cursor):
    query = "SELECT * FROM CLIMA ORDER BY DATA_DIA" #TEMOS QUE ORDENAR!!!!
    cursor.execute(query)
    linhas = cursor.fetchall()
    return linhas

def compara_clima(linhas,clima_dia):
    if len(linhas) == 0:
        clima_ontem = False
    else:#para quando eu já tenho itens na tabela
        ontem = linhas[-1] #ontem será uma tupla seguindo a ordem dos campos da tabela
        clima_ontem = ontem[3] #isolei o quarto item da tabela (CLIMA_DIA)
    print(clima_ontem)
    clima_igual = clima_ontem == clima_dia # Ex: pensar em uma outra forma de criar o clima_igual
    return clima_igual

def get_media_t(linhas, temp):
    print("Calculando a média histórica...")
    #este script abaixo necessita de 2 correções.
    #segundo ponto: o loop só funciona quando já temos dados na tabela.
    # temos que colocar em um if para quando não há dias na tabela
    if len(linhas) == 0:
        media_t = temp
    else:
        soma_t = temp #primeiro ponto; inicializar a soma com o dia de hoje
                        # para compensar o fato de ainda nao estar na tabela
        for linha in linhas:
            temp_da_linha = linha[1]
            soma_t += float(temp_da_linha)
        media_t = soma_t / (len(linhas)+1)  #verificamos que esta média não está certa
    print("...feito!")
    return media_t

def escreve_linha_hoja(hoje, temp, delta_t, clima_dia, clima_igual, media_t,cursor,conn,dia_formatado):
    ##vamos escrever no banco a linha de hoje
    print("Inserindo valores no banco...")
    try:
        query_inserir = "INSERT INTO CLIMA (DATA_DIA, TEMP, DELTA_T, CLIMA_DIA, CLIMA_IGUAL, MEDIA_T) VALUES (:v, :v,:v, :v,:v, :v)"
        valores = (hoje, temp, delta_t, clima_dia, clima_igual, media_t)
        cursor.execute(query_inserir, valores)
        conn.commit()
        print("...sucesso!")
    except cx_Oracle.IntegrityError:
        print(f"---> As informações do dia de hoje ({dia_formatado}) já foram processadas!\nTente novamente amanhã!")


def altera_linha(cursor, conn, media_t, dia,coluna):
    query = f"UPDATE CLIMA SET {coluna}=:v WHERE DATA_DIA=:v"
    valores = (media_t, dia)
    cursor.execute(query, valores)
    conn.commit()