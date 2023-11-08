'''
    TRYMF PROJEKT
Ideia principal: atualizar cadastro e reter a maior quantidade de informação para selecionar o melhor modal.

No momento de abertura do chamado, o usuário deve digitar o Placa do carro, o qual já vai puxar as informações
principais do carro ( API banco de dados com o DETRAN).

Em sequência, será o momento de descobrir possíveis alterações no veículo, através de perguntas e respostas
(c/ fotos caso exista a modificação).

Descrição do problema enfrentado pelo segurado.

Descrição do tipo de carga (ou não) transportada pelo motorista (c/ fotos em casos de carga).

Através do cruzamento de dados das informações dadas pelo usuário + fotos + localização do segurado, haverá a
escolha do melhor modal.
'''


"""
    Implementamos os dicioanrios com o intuito de gerar um banco de dados proprio para nosso sisitema enquanto não temos
o API de banco de dados com o DETRAN.
"""

veiculo = {
    'Placa ': 'AAA0000',
    'Renavam': '23458920',
    'Chassi': '7785155',
    'Especie': 'transporte de carga',
    'Fabricação': '2009',
    'Ano_do_modelo': '2008',
    'Modelo': 'Linha S - S Sleeper Perfil Alto',
    'Marca': 'Scania',
    'Cor': 'Vermelho',
    'Procedencia': 'nacional',
    'Combustivel': 'gasolina',
    'Municipio': 'São Paulo',
    'Tipo_de_carroceria': 'baú',
    'Eixos': '2',
    'Eixo_traseiro': 'sim',
    'Terceiro_eixo': 'não',
    'Tração': '200',
    'Cilindradas': '200',
    'Potencia': '100',
    'Pbt': '20',
    'Cap_passageiros': '3',
    'Tara': '200',
    'Modificacao': 'sem modificações'
}

problema = { 'Tipo': 'Veiculo sem problemas aparente'}

carga = {'Tipo' : 'Vazia' }

carga_peso = {'Peso': '0'}

#Tempo de entrega em minutos.
prestador = {
    'Nome' : 'Guincho ABC',
    'Tempo de chegada' : '30',
    'Placa' : 'SSS9999'
}

reset = {'Resetar' : 'não'}

"""
    Etapa 8: neste momento será entregue ao usuario um protocolo resumindo as informações do chamado do modal,com isso
    podendo realizar a confirmação da solcitação(seguindo para a etapa 9) ou o cancelamento do chamado por completo.
"""
def protocolo():
    global veiculo, problema, carga, peso, prestador, reset

    print("\nVeiuclo com placa ", veiculo['Placa'], ", problema de ", problema['Tipo'], ", com carga ", carga['Tipo'],
          " e pesando ", carga_peso['Peso'], " kg."
          "\nSerá socorrido pelo prestador de serviço ", prestador['Nome'], " e placa ", prestador['Nome'],
          " está com previsão de chegda de ", prestador['Tempo de chegada'])
    print("\nO(a) senhor(a) confirma a solicitação acima?"
            "\n1 - Sim, Confirmo"
            "\n2 - Não, quero cancelar")

    while True:
        confirmacao = int(input("\nEscolha uma opção: "))

        if confirmacao == 1:
            print("Solicitação finalizada com sucesso, agradecemos por utilizar de nossos serviços!")
            reset['Resetar'] = "sim"
            break

        elif confirmacao == 2:
            print("Solicitação cancelada com sucesso!")
            print("Encerrando o atendimento...")
            exit()

        else:
            print("Opção inválida! Tente novamente.")
            continue

"""
    Etapa 7:
    No projeto, a IA que será desenvolvida, avaliará a melhor opção de modal (ainda não aprendemos, por isso não temos o código aqui).
    Através da vinculação do banco de dados do detran + modificações , e escolherá o melhor prestador para atender ao chamado.
    Melhor prestador = possuir o modal correto e estiver mais próximo do segurado,para que o atendimento possa ser rápido.
    Apenas o prestador será exibido ao usuário.
    No momento não temos um banco de dados de prestadore de serviço, esparamos conseguir com a porto.
    As informações do prestador de serviço será crucial para que possamos realizar os calculos de escolha 
    de modal.
"""
def modal():

    print("\nO Prestador Escolhido é ", prestador['Nome'],
          "\nA previsão de chegada é de ", prestador['Tempo de chegada'], " minutos.")
    protocolo()

"""
    Etapa 6: Declaração do peso da carga, esta informação será usada no calculo da escolha do modal (etapa 7).
"""
def peso_carga():
    global carga_peso

    while True:
        novo_peso = (float(input('\n Qual o peso da carga (em KG)?')))

        if novo_peso >= 0:
            carga_peso['Peso'] = novo_peso
            modal()
            break

        else:
            print("\nO numero digitado é negativo, por gentileza digite o peso correto da carga")
            continue

"""
    Etapa 5: Declaração da descrição da Carga, o tipo e a quantidade da carga alteram o peso do 
    veículo, influenciando a esolha do modal.
    Caso veiculo não tenha carga o peso do veiculo será considerado apenas a tara em seguida ira 
    direcionar o usuario até a declaração do modal compativel(etapa 7).
    Caso tenha carga deve declarar o tipo e em seguida deve informar o peso (etapa 6).
       
"""

def tipo_carga():
    global carga

    print("Você está transportando Carga?"
          "\nDigite:"
          "\n1 - Sim"
          "\n2 - Não")

    carregado = (int(input("\nEscolha uma opção:")))

    if carregado == 2:
        print("\nEm breve o prestador de serviço chegará até você para resolver o problema.")
        modal()


    elif carregado == 1:
        print('\nQual o tipo de carga que você está carregando ?'
              '\n1 - Viva'
              '\n2 - Perecível'
              '\n3 - Perigosa'
              '\n4 - Seca')

        while True:
            opcoesCarga = ["Viva", "Perecivel", "Perigosa", "Seca"]

            nova_carga = (int(input('\nEscolha o múmero que corresponde ao tipo de carga: ')))

            if nova_carga >= 1 and nova_carga <= 4:
                carga['Tipo'] = opcoesCarga[nova_carga - 1]
                peso_carga()
                break

            else:
                print("Opção inválida! Tente novamente.")
                continue

    else:
        print("Opção inválida! Tente novamente.")

"""
    Etapa 4: Usuario ire informar qual problema esta enfrentando e apos isso será direcionado para a 
    declaração do tipo de carga (etapa 5).
    Este dado será salvo e direcionado ao protocolo de chamado.
    Colocamos algumas opções como exemplo, mas as possibilidades de problemas que o seguro cobre,
    esperamos conseguir com a própria Porto.
"""

def tipo_problema():
    global problema

    print('\nQual o tipo de problema você está enfrentando ?'
          '\nEscolha o número que corresponde ao problema apresentado pelo veículo:'
          '\n1 - Elétrico'
          '\n2 - Mecânico'
          '\n3 - Envolvimento em Acidente'
          '\n4 - Pneu furado')

    while True:
        opcoesProblema = ["Elétrico", "Mecânico", "Envolvimento em acidente", "Pneu furado"]

        novo_problema = (int(input('\nEscolha uma opção:')))

        if novo_problema >= 1 and novo_problema <= 4:
            problema['Tipo'] = opcoesProblema[novo_problema - 1]
            tipo_carga()
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            continue

"""
    Etapa 3: O usuario ira informar da modificação realizada no veiculo e será direcionado
    para a declaração do tipo de problema (etapa 4).
    
    As atualizações serão realizadas no cadastro, ficando salvas no perfil do cliente;
    Na próxima exibição de dados (ou acionamento do seguro), as alterações já serão exibidas;
    Algumas modificações alteram o peso do veículo, influenciando a esolha do modal;
    As possibilidades de modificações, esperamos conseguir com a própria Porto.
"""

def atualizacao():
    global veiculo

    print('\nVamos atualizar seu cadastro!\n'
          '\nEscolha o múmero que corresponde a mudança realizada no veículo:'
          '\n1 - Reforço de Eixo'
          '\n2 - Blindagem'
          '\n3 - Rebaixamento de Suspensão')

    while True:
        opcoesModificacao = ["Reforço de Eixo", "Blindagem", "Rebaixamento de Suspensão" ]

        nova_modificacao = (int(input('\nEscolha uma opção:')))

        if nova_modificacao >= 1 and nova_modificacao <= 3:
            veiculo['Modificacao'] = opcoesModificacao[nova_modificacao - 1]
            print("\nÓtimo! A modificação ", veiculo['Modificacao'], "foi adicionado com sucesso.")
            tipo_problema()
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            continue

"""
    Etapa 2:Exibição dos dados do Veículo e confirmação das informações, caso o veiculo tenha uma 
    modificação não registrada, o usuario será direcionado para a atualização do dados(etapa 3), 
    caso contraio seguira para a declaração do tipo de problema do veiculo(etapa 4).
"""

def dados_veiculo():
    global veiculo

    placa_teste = input("\nDigite a placa do seu veículo: ")

    veiculo['Placa'] = placa_teste

    print(f"\nAqui estão os dados do seu veículo:"
          f"\nPlaca: {veiculo['Placa']}"
          f"\nRenavam: {veiculo['Renavam']}"
          f"\nChassi: {veiculo['Chassi']}"
          f"\nEspecie: {veiculo['Especie']}"
          f"\nAno de Fabricação: {veiculo['Fabricação']}"
          f"\nAno do Modelo: {veiculo['Ano_do_modelo']}"
          f"\nModelo: {veiculo['Modelo']}"
          f"\nMarca: {veiculo['Marca']}"
          f"\nCor: {veiculo['Cor']}"
          f"\nProcedencia: {veiculo['Procedencia']}"
          f"\nCombustivel: {veiculo['Combustivel']}"
          f"\nMunicípio: {veiculo['Municipio']}"
          f"\nTipo de Carroceria: {veiculo['Tipo_de_carroceria']}"
          f"\nEixos: {veiculo['Eixos']}"
          f"\nEixo Traseiro: {veiculo['Eixo_traseiro']}"
          f"\nTerceiro Eixo: {veiculo['Terceiro_eixo']}"
          f"\nTração: {veiculo['Tração']}"
          f"\nCilindradas: {veiculo['Cilindradas']}"
          f"\nPotência: {veiculo['Potencia']}"
          f"\nPeso Bruto Total: {veiculo['Pbt']} toneladas"
          f"\nCapacidade de Passageiros: {veiculo['Cap_passageiros']}"
          f"\nTara: {veiculo['Tara']} kg"
          f"\nModificações: {veiculo['Modificacao']}")
    print("\nOs dados do seu veículo estão corretos?"
          "\n1 - SIM"
          "\n2 - NÃO")

    while True:

        opcao_dados = (int(input("\nEscolha uma opção:")))

        if opcao_dados == 1:
            print('\nÓtimo!Seu cadastro se mantem atualizado!.')
            tipo_problema()
            break

        elif opcao_dados == 2:
            atualizacao()
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            continue

"""
    Etapa 1: Acionamento do Seguro onde o usuario ira confirmar a solicitação do guincho, logo em seguida será
    direcionado a verificação(etapa 2) de dados do vieuclo. Caso o usuario não queira realizar a solicitação o sistema encerra.
"""

def menu():

    print("\nBem-vindo ao suporte da Porto! Está precisando de um guincho?"
            "\n1 - SIM"
            "\n2 - NÃO")

    while True:

        try:
            opcao = int(input("\nDigite a opção desejada: "))

        except ValueError:
            print("\nOpção inválida! Tente novamente.")
            continue

        if opcao == 2:
            print("\nEncerrando o atendimento...")
            exit()

        elif opcao == 1:
            dados_veiculo()
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            continue

"""
    Etapa 9: Caso o usuario queira realizar uma nova solicitação de guincho o sistema será reiniciado, caso contrario
    ele será encerrado.
"""

def resetar_sistema():

    print("\nGostaria de realizar um novo chamado?"
          "\n1 - SIM"
          "\n2 - NÃO")

    while True:
        novo_chamado = int(input("\nEscolha uma opção: "))

        if novo_chamado == 1:
            print("\nPerfeito, iremos lhe encaminhar para o inicio")
            menu()
            break

        elif novo_chamado == 2:
            print("Encerrando o atendimento...")
            exit()

        else:
            print("Opção inválida! Tente novamente.")
            continue

#inicia o sistema, assim como realiza a validação para o looping do sistema.

while True:
    menu()
    if reset['Resetar'] == "sim":
        resetar_sistema()

    else:
        break