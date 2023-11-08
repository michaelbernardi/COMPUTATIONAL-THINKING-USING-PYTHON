# Partes de uma URL (Uniform Resource Locator):
#

# Esquema, Domínio, Porta, Caminho e Query string.

# 1. **Esquema (Scheme)**: Indica o protocolo de comunicação.

#   Os esquemas mais comuns em sistemas web são o "http" e o "https".

# O HTTP (Hypertext Transfer Protocol) é para transferir informações entre um cliente e um servidor.

# Ele permite que os clientes solicitem recursos (páginas da web, imagens, JSON, dados, etc)
# e os servidores respondam fornecendo esses recursos.

# Opera no modelo de solicitação-resposta (request-response),
# onde o **cliente faz requests** para URLs e o **servidor responde (responses)** com os dados solicitados.

# As mensagens HTTP incluem métodos, como GET para buscar recursos e POST para enviar dados,
# além de códigos de status, como 200 para indicar sucesso ou 404 para indicar que o recurso não foi encontrado.

# O HTTPS é a versão "segura" do HTTP, pois utiliza criptografia para que as informações sejam acessíveis
# apenas para o cliente e o servidor.


# 2. **Domínio (Host)**: Indica o endereço do servidor onde o recurso está localizado.
# Pode ser um domínio como https://www.google.com ou um endereço de IP https://142.250.219.4:443 (Google)


# 3. **Porta (Port)**: é opcional e indica o número da porta de um servidor a ser usado para acessá-lo.
# Se não for especificada, utiliza-se a porta padrão para o esquema
# como por exemplo, 80 para HTTP e 443 para HTTPS.

# No exemplo anterior: https://www.google.com:443 ou https://142.250.219.4:443
# (note o :443 no final)


# 4. **Caminho (Path)**: (opcional) Especifica o caminho para o recurso no servidor.
# Pode incluir diretórios e subdiretórios.
# Exemplos:
# https://www.google.com/imghp  => Google imagens
# https://www.google.com/search  => Google search


# 5. **Query String**: (opcional) Contém os parâmetros de consulta para o servidor.
# É precedida por um ponto de interrogação "?" e pode conter múltiplos pares chave-valor separados por "&".

#    Exemplo: https://www.google.com/search?q=fiap


# Exemplo com a PokéAPI
# Site com documentação: https://pokeapi.co/docs/v2
# Acessando uma informações de uma berry:  https://pokeapi.co/api/v2/berry/{id or name}/
# Exemplo: https://pokeapi.co/api/v2/berry/1/ ou https://pokeapi.co/api/v2/berry/cheri/


# Acessando uma API com Python requests:

# primeiramente, temos que instalar o pacote requests
# Digite em seu terminal (fora do python): pip install requests

# em seguida, em um arquivo .py:
# importe o pacote
import requests
import pprint  # uma forma de imprimir "bonito" (pretty)

# print(4 * "\n")
# print(50 * "=")
# print(10 * " ", "Trabalhando com a pokéAPI")
# print(50 * "=")
# print()
# # envie uma request
# url = "https://pokeapi.co/api/v2/berry/1/"
# response = requests.get(url)
# # trate a resposta de sua requisição:
# if response.status_code == 200:
#     # lista de códigos de estado: https://pt.wikipedia.org/wiki/Lista_de_c%C3%B3digos_de_estado_HTTP
#     data = response.json()  # Converte a resposta JSON em um dicionário Python
#     # Faça algo com os dados, como exibir, processar ou armazenar
#     pprint.pprint(data)
# else:
#     print("Falha na solicitação. Código de status:", response.status_code)
#
#
#
# # Métodos GET, POST, PATCH e DELETE

# POST -> CREATE
# GET - > READ
# PATCH / PUT -> UPDATE
# DELETE -> DELETE
#
# nestes exemplos, utilizaremos a API jsonplaceholder

# print(4 * "\n")
# print(50 * "=")
# print(10 * " ", "Trabalhando com a API jsonplaceholder")
# print(50 * "=")
# print()

# # GET:
# #    - É uma operação de leitura, solicitando dados de um recurso específico do servidor.
# #    - Os parâmetros são anexados à URL e **são visíveis**, transmitidos de forma legível na URL.
# #    - Não modifica os dados no servidor.
# #    - Corresponde a operação READ do CRUD.
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)
#
# print()
# print(50 * "=")
# print(10 * " ", "Trabalhando com GET na API jsonplaceholder")
# print(50 * "=")
#
# if response.status_code == 200:
#     data = response.json()
#     pprint.pprint(data)
# else:
#     print("Falha na solicitação. Código de status:", response.status_code)

# POST:
#    - É uma operação de envio de dados dados ao servidor e por isso utilizada para criar novos recurso.
#          Exemplos: envios de formulários web, envios de dados para APIs, etc.
#    - Os dados são enviados no corpo (body) da solicitação e não na URL, o que os torna menos visíveis.
#    - Corresponde a operação CREATE do CRUD.
# print()
# print(50 * "=")
# print(10 * " ", "Trabalhando com POST na API jsonplaceholder")
# print(50 * "=")
#
# dados_post = {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1,
# }
# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.post(url=url, data=dados_post)
#
# if response.status_code == 201:
#     data = response.json()
#     pprint.pprint(data)
# else:
#     print("Falha na solicitação. Código de status:", response.status_code)

# PATCH:
#    - É usado para atualizar um recurso JÁ existente no servidor.
#          Exemplos: alteração de informações cadastrais, configurações, etc.
#    - Assim como no POST, Os dados também são enviados no body da requisição, neste caso apenas com os campos a serem alterados.
#    - Corresponde a operação UPDATE do CRUD.
# print()
# print(50 * "=")
# print(10 * " ", "Trabalhando com PATCH na API jsonplaceholder")
# print(50 * "=")
#
# dados_patch = {
#     "id": 1,
#     "title": "bar",  # era "foo"
#     "body": "foo",  # era "bar"
#     "userId": 1,
# }
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.patch(url, dados_patch)
# if response.status_code == 200:
#     data = response.json()
#     pprint.pprint(data)
# else:
#     print("Falha na solicitação. Código de status:", response.status_code)
#
# DELETE:
#    - Solicita a remoção de um recurso JÁ existente no servidor.
#          Exemplos: remoção de um item do catálogo, remoção de um cadastro, etc.
#    - Geralmente não requer dados na solicitação, pois a identificação do recurso pode ser feita pela URL.
#    - Corresponde a operação DELETE do CRUD.
#    Curiosidade: muitas aplicações implementam o soft-delete, que trata-se de não apagar um registro,
#                 mas marcá-lo como "inativo" no banco de dados.

print()
print(50 * "=")
print(10 * " ", "Trabalhando com DELETE na API jsonplaceholder")
print(50 * "=")

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url=url)
if response.status_code == 200:
    print("Deletado com sucesso")
else:
    print("Falha na solicitação. Código de status:", response.status_code)

# # As tratativas de dados e conexões utilizam cláusulas try/except para aumentar a "resiliência" do código.
# # Exercício: reescrever o código acima utilizando try/except
# # referência: https://requests.readthedocs.io/en/latest/_modules/requests/exceptions/


#
# # Exercício 1: filtrar posts dado um userId na API jsonplaceholder
# #        Referência: https://jsonplaceholder.typicode.com/guide/
#
#
# # Exercício 2: Criar módulos e/ou funções para lidar com as requisições para a API jsonplaceholder
# #            Deverá utilizar a biblioteca python requests, tratativas de exceções e
# #            validações de códigos de retorno.
