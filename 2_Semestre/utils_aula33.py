import json
import cx_Oracle

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
    query = "SELECT * FROM TB_USUARIO"
    cursor.execute(query)
    linhas = cursor.fetchall()
    return linhas

def verifica_conteudo(linhas):
    print(f"Esta tabela possui {len(linhas)} linhas!\nSão elas:")
    for linha in linhas:
        print(linha)