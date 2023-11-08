import cx_Oracle
import json
#cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient-basic-windows.x64-21.11.0.0.0dbru\instantclient_21_11")
path = r"C:\Users\paulo\Desktop\credenciais.json"

with open(path, "r") as arquivo:
    dados = json.load(arquivo)
login = dados["login"]
senha = dados["senha"]

#___________________________________________________________________________
## ESQUELETO DE CONEXÃO E CRUD

#1º passo: passar informações do banco
dsn = cx_Oracle.makedsn(host="oracle.fiap.com.br", port=1521, sid="ORCL")

#2º passo: conectar ao banco
conn = cx_Oracle.connect(user=login, password=senha, dsn=dsn)

#3º passo: criar um cursor
cursor = conn.cursor()

#passo extra: escrever a query (lembrando que é SQL) - instruções para o banco
QUERY = "SELECT * FROM TB_USUARIO"
#4º passo: preparar instrução pro banco
cursor.execute(QUERY)

#5º passo: enviar ou receber informações do banco
#5.1 Enviar: para Create, Update e Delete
#conn.commit()
#5.2 Receber: para Read
linhas_do_banco = cursor.fetchall()

#6º passo (em caso de Real - leitura): trabalhar com a informação recebida
#ex: print
for linha in linhas_do_banco:
    print(linha)

#último passo: encerrar o(s) cursor(es) e a conexão
cursor.close()
conn.close()


#EXERCÍCIO:
#pensar na estrutura de um banco de dados que guarde a previsão do tempo de um dia,
# e compare com o que realmente aconteceu

# pensar no pseudo-código (fluxograma) para este sistema que imaginamos
# pegar a previsão do tempo via API, guardar no banco, no dia seguinte comparar com o que realmente aconteceu,
# e gerar uma flag de se a previsão acertou