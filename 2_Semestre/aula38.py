## VAMOS CRIAR UMA NOVA TABELA QUE CONTENHA O CAMPO 'LOCALIDADE'
## E VAMOS IMPORTAR OS DADOS DA TABELA CLIMA_X PARA ELA, INCLUINDO O NOME DA CIDADE

'''
CREATE TABLE CLIMA_X_CIDADE(
DATA_DIA   VARCHAR(255)  NOT NULL PRIMARY KEY
,TEMP VARCHAR(255) ,
DELTA_T VARCHAR(255) ,
CLIMA_DIA VARCHAR(255) ,
CLIMA_IGUAL VARCHAR(255) ,
MEDIA_T VARCHAR(255) ,
LOCALIDADE VARCHAR(255)
)
'''

from utils_aula32 import *
# etapas do processo:

# 0 concetar ao banco
# vamos manipular duas tabelas do mesmo banco
# por isso, a conexão é a mesma!
print("Conctando ao banco...")
dsn = cria_dsn(host="oracle.fiap.com.br", port=1521, sid="ORCL")
login, senha = carrega_credenciais(path=r"C:\Users\paulo\Desktop\credenciais.json")
conn = conecta_banco(login, senha, dsn)
cursor = conn.cursor()
print()

# 1 guardar as informações da tabela antiga
# 1.1 ler a tabela antiga
nome_tabela = input("Diga o nome da tabela que deseja importar: ")

while True:  #validando se a tabela existe no banco
    try:
        QUERY = f"SELECT * FROM {nome_tabela} ORDER BY DATA_DIA"
        cursor.execute(QUERY)
        # 1.2 armazenar em uma variável de memória
        tabela = cursor.fetchall()
        break #caso exista, sair do loop
    except cx_Oracle.DatabaseError:
        print("nome da tabela inválido!")
        nome_tabela = input("Diga o nome da tabela que deseja importar: ")
        #enquando o usuário digiar um nome que não existe, ele vai pedir um nome novo

## EXERCÍCO: escrever a etapa 2
# 2 escrever na nova tabela
# 2.1 adicionar o valor requerido (a localidade)
# -> como saber qual a localidade?
# ---> extraindo da resposta da API a localidade correspondendo à latitude e longitude
#recebendo os dados da api novamente, para poder salvar a localidade
resposta = recebe_api(endpoint) #para generalizar, precisamos solicitar ao usuário ou a lat/lon diretamente; ou um arquivo que contenha a localização
resposta_dict = resposta.json()
localidade = resposta_dict["name"] #assim que eu recupero o valor de uma chave
print(localidade)
# -> onde e como eu adiciono este valor na minha tabela?
# ---> eu dou um append ao final da lista com o valor da localidade

#EXERCÍCO: verificar o que precisa ser feito nesta etapa para generalizar
for linha in tabela:
    linha_lista = list(linha) #lembrando que os itens da minha lista (as linhas da tabela) são retornadas como tupla
    linha_lista.append(localidade)
    print(linha_lista)
    # 2.2 colocar cada linha na tabela (escrevemos linha a linha)
    # -> podemos utilizar a função "escreve_na_tabela"?
    # ---> posso juntar as 2 etapas num mesmo loop, para não ter re-processamento
    escreve_na_tabela_localidade(cursor, conn, linha_lista)



# 3 ENCERRAR AS CONEXÕES!!!
cursor.close()
conn.close()
