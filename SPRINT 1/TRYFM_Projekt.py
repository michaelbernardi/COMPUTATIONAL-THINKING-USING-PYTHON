'''TRYMF PROJEKT
Ideia principal: atualizar cadastro e reter a maior quantidade de informação para selecionar o melhor modal.
1) No momento de abertura do chamado, o usuário deve digitar o Placa do carro, o qual já vai puxar as informações principais do carro ( API banco de dados com o DETRAN).
2)Em sequência, será o momento de descobrir possíveis alterações no veículo, através de perguntas e respostas (c/ fotos caso exista a modificação).
3)Descrição do problema enfrentado pelo segurado
4)Descrição do tipo de carga (ou não) transportada pelo motorista (c/ fotos em casos de carga).
5)Através do cruzamento de dados das informações dadas pelo usuário + fotos + localização do segurado, haverá a escolha do melhor modal.
'''

# Etapa 1:Acionamento do Seguro
print("Seja Bem-Vindo ao suporte da Porto!")
placa = input("Digite a placa do seu veículo: ")

# Etapa 2:Exibição dos dados do Veículo
# No projeto, os dados exibidos serão da API do Detran --> abaixo é apenas um exemplo para visualizar a ideia do programa no output
# Exemplo:Dados do Veículo
renavam = 23458920
chaci = 7785155
especie = "transporte de carga"
fabricação = 2009
ano_do_modelo = 2008
modelo = 'Linha S - S Sleeper Perfil Alto'
marca = 'Scania'
cor = "Vermelho"
procedencia = 'nacional'
combustivel = "gasolina"
municipio = 'São Paulo'
tipo_de_carroceria = 'baú'
eixos = 2
eixo_traseiro = 'sim'
terceiro_eixo = 'não'
tração = 200
cilindradas = 200
potencia = 100
pbt = 20
cap_passageiros = 3
cap_carga = 200

print(f'Dados do veículo: '
      f'\nPlaca: {placa.upper()}'
      f'\nRenavam: {renavam}'
      f'\nChaci: {chaci}'
      f'\nEspécie: {especie}'
      f'\nAno de Fabricação: {fabricação}'
      f'\nAno do Modelo: {ano_do_modelo}'
      f'\nModelo: {modelo}'
      f'\nMarca: {marca}'
      f'\nCor: {cor}'
      f'\nProcedência: {procedencia}'
      f'\nCombustível: {combustivel}'
      f'\nMunicípio: {municipio}'
      f'\nTipo de Carroceria: {tipo_de_carroceria}'
      f'\nEixos: {eixos}'
      f'\nEixo Traseiro: {eixo_traseiro}'
      f'\nTerceiro Eixo: {terceiro_eixo}'
      f'\nTração: {tração}'
      f'\nCilindradas: {cilindradas}'
      f'\nPotência: {potencia}'
      f'\nPeso Bruto Total: {pbt} toneladas'
      f'\nCapacidade de Passageiros: {cap_passageiros}'
      f'\nCapacidade de Cargas:{cap_carga} kg')

# Etapa 3: Confirmação de Dados
print()
print("Os dados do seu veículo estão corretos?"
      "\nDigite: 1 - Sim e 2 - Não")
opcao_dados = (int(input("\nEscolha uma opção:")))

# Etapa 3a: Atualização de Dados ou Não
# As atualizações serão realizadas no cadastro, ficando salvas no perfil do cliente;
# No próxima exibição de dados (ou acionamento do seguro), as alterações já serão exibidas;
# Algumas modificações alteram o peso do veículo, influenciando a esolha do modal;
# As possibilidades de modificações, esperamos conseguir com a própria Porto.
if opcao_dados == 1:
    print()
    print('Ótimo!Seu cadastro está atualizado.')
elif opcao_dados == 2:
    print()
    print('Vamos atualizar seu cadastro!'
          '\nEscolha o múmero que corresponde a mudança realizada no veículo:'
          '\n1 - Reforço de Eixo'
          '\n2 - Blindagem'
          '\n3 - Rebaixamento de Suspensão')

    modificacao = (int(input('\nEscolha uma opção:')))

else:
    print("Opção Inválida. Escolha novamente.")
# Loop para reiniciar o programa --> ainda não aprendemos

# Etapa 4: Descrição do Problema Enfrentado
# As possibilidades de problemas, esperamos conseguir com a própria Porto.
print()
print('Qual o tipo de problema você está enfrentando ?'
      '\nEscolha o número que corresponde ao problema apresentado pelo veículo:'
      '\n1 - Elétrico'
      '\n2 - Mecânico'
      '\n3 - Envolvimento em Acidente'
      '\n4 - Pneu furado')

problema = (int(input('\nEscolha uma opção: ')))

# Etapa 5: Descrição da Carga
# O tipo e a quantidade da carga alteram o peso do veículo, influenciando a esolha do modal.
print()
print("Você está transportando Carga?"
      "\nDigite: 1 - Sim e 2 - Não")
carga = (int(input("\nEscolha uma opção:")))

if carga == 2:
    print()
    print("Em breve o prestador de serviço chegará até você para resolver o problema.")
elif carga == 1:
    print('Qual o tipo de carga você está carregando ?'
          '\nEscolha o múmero que corresponde ao tipo de carga:'
          '\n1 - Viva'
          '\n2 - Perecível'
          '\n3 - Perigosa'
          '\n4 - Seca')
    tipo_carga = (int(input('\nEscolha uma opção: ')))
    peso_carga = (float(input('\nQual o peso da carga (em kg): ')))

else:
    print("Opção Inválida. Escolha novamente.")
# Loop para reiniciar o programa --> ainda não aprendemos

# Etapa 6: Escolha do Modal
# No projeto, a IA que será desenvolvida, avaliará a melhor opção de modal (ainda não aprendemos, por isso não temos o código aqui)
# Através da vinculação do banco de dados do detran + modificações , e escolherá o melhor prestador para atender ao chamado
# Melhor prestador = possuir o modal correto e estiver mais próximo do segurado,para que o atendimento possa ser rápido.
# Apenas o prestador será exibido ao usuário

# Etapa 7: Acionamento do Prestador
# Base de dados de Prestadores,esperamos conseguir com a própria Porto.
# Exemplo para o Programa
prestador = "Guinchos ABC"
tempo_entrega = 30
print()
print(f'O Prestador Escolhido é o {prestador}.'
      f'\nA previsão de chegada é {tempo_entrega} minutos.')

# RESUMO
print()
print('Resumo do Acionamento do Seguro:')
# etapa1
print(f"-Placa: {placa}")
# etapa2
print(f'-Modelo: {modelo}')
# etapa3
if opcao_dados == 1:
    print("-Cadastro Correto")

elif opcao_dados == 2:
    if modificacao == 1:
        modificacao = 'Reforço do Eixo'
        print(f'-Cadastro Atualizado.Modificação:{modificacao}')
    elif modificacao == 2:
        modificacao = 'Blindagem'
        print(f'-Cadastro Atualizado.Modificação:{modificacao}')
    else:
        modificacao = 'Rebaixamento de Suspensão'
        print(f'-Cadastro Atualizado.Modificação:{modificacao}')

# etapa 4
if problema == 1:
    problema = 'Elétrico'
    print(f'-Problema: {problema}')
elif problema == 2:
    problema = 'Mecânico'
    print(f'-Problema: {problema}')
elif problema == 3:
    problema = 'Envolvimento em Acidente'
    print(f'-Problema: {problema}')
else:
    problema = 'Pneu furado'
    print(f'-Problema: {problema}')

# etapa5
if carga == 1:
    if tipo_carga == 1:
        tipo_carga = 'Carga Viva'
        print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg. ")
    elif tipo_carga == 2:
        tipo_carga = 'Carga Perecível'
        print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg.")
    elif tipo_carga == 3:
        tipo_carga = 'Carga Perigosa'
        print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg. ")
    else:
        tipo_carga = 'Carga Seca'
        print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg.")

else:
    print(f'-Sem carga ')

# etapa6 = apenas com IA (ainda não aprendemos)

# etapa7
print(f'-Prestador Escolhido:{prestador} '
      f'\n-Previsão de chegada: {tempo_entrega} minutos.')

print()
print('1 - Realizar nova operação ou 2 - Encerrar atendimento')
fim = int(input('Escolha uma das opções:'))
# Precisaria fazer um loop para o programa reiniciar
# Como não aprendemos a fazer, faremos o loop de forma "manual",inserindo o código novamente.
# Loop Manual
if fim == 1:
    # Etapa 1:Acionamento do Seguro
    print("Seja Bem-Vindo ao suporte da Porto!")
    placa = input("Digite a placa do seu veículo: ")

    # Etapa 2:Exibição dos dados do Veículo
    # No projeto, os dados exibidos serão da API do Detran --> abaixo é apenas um exemplo para visualizar a ideia do programa no output
    # Exemplo:Dados do Veículo
    renavam = 23458920
    chaci = 7785155
    especie = "transporte de carga"
    fabricação = 2009
    ano_do_modelo = 2008
    modelo = 'Linha S - S Sleeper Perfil Alto'
    marca = 'Scania'
    cor = "Vermelho"
    procedencia = 'nacional'
    combustivel = "gasolina"
    municipio = 'São Paulo'
    tipo_de_carroceria = 'baú'
    eixos = 2
    eixo_traseiro = 'sim'
    terceiro_eixo = 'não'
    tração = 200
    cilindradas = 200
    potencia = 100
    pbt = 20
    cap_passageiros = 3
    cap_carga = 200

    print(f'Dados do veículo: '
          f'\nPlaca: {placa.upper()}'
          f'\nRenavam: {renavam}'
          f'\nChaci: {chaci}'
          f'\nEspécie: {especie}'
          f'\nAno de Fabricação: {fabricação}'
          f'\nAno do Modelo: {ano_do_modelo}'
          f'\nModelo: {modelo}'
          f'\nMarca: {marca}'
          f'\nCor: {cor}'
          f'\nProcedência: {procedencia}'
          f'\nCombustível: {combustivel}'
          f'\nMunicípio: {municipio}'
          f'\nTipo de Carroceria: {tipo_de_carroceria}'
          f'\nEixos: {eixos}'
          f'\nEixo Traseiro: {eixo_traseiro}'
          f'\nTerceiro Eixo: {terceiro_eixo}'
          f'\nTração: {tração}'
          f'\nCilindradas: {cilindradas}'
          f'\nPotência: {potencia}'
          f'\nPeso Bruto Total: {pbt} toneladas'
          f'\nCapacidade de Passageiros: {cap_passageiros}'
          f'\nCapacidade de Cargas:{cap_carga} kg')

    # Etapa 3: Confirmação de Dados
    print()
    print("Os dados do seu veículo estão corretos?"
          "\nDigite: 1 - Sim e 2 - Não")
    opcao_dados = (int(input("\nEscolha uma opção:")))

    # Etapa 3a: Atualização de Dados ou Não
    # As atualizações serão realizadas no cadastro, ficando salvas no perfil do cliente;
    # No próxima exibição de dados (ou acionamento do seguro), as alterações já serão exibidas;
    # Algumas modificações alteram o peso do veículo, influenciando a esolha do modal;
    # As possibilidades de modificações, esperamos conseguir com a própria Porto.
    if opcao_dados == 1:
        print()
        print('Ótimo!Seu cadastro está atualizado.')
    elif opcao_dados == 2:
        print()
        print('Vamos atualizar seu cadastro!'
              '\nEscolha o múmero que corresponde a mudança realizada no veículo:'
              '\n1 - Reforço de Eixo'
              '\n2 - Blindagem'
              '\n3 - Rebaixamento de Suspensão')

        modificacao = (int(input('\nEscolha uma opção:')))

    else:
        print("Opção Inválida. Escolha novamente.")
    # Loop para reiniciar o programa --> ainda não aprendemos

    # Etapa 4: Descrição do Problema Enfrentado
    # As possibilidades de problemas, esperamos conseguir com a própria Porto.
    print()
    print('Qual o tipo de problema você está enfrentando ?'
          '\nEscolha o número que corresponde ao problema apresentado pelo veículo:'
          '\n1 - Elétrico'
          '\n2 - Mecânico'
          '\n3 - Envolvimento em Acidente'
          '\n4 - Pneu furado')

    problema = (int(input('\nEscolha uma opção: ')))

    # Etapa 5: Descrição da Carga
    # O tipo e a quantidade da carga alteram o peso do veículo, influenciando a esolha do modal.
    print()
    print("Você está transportando Carga?"
          "\nDigite: 1 - Sim e 2 - Não")
    carga = (int(input("\nEscolha uma opção:")))

    if carga == 2:
        print()
        print("Em breve o prestador de serviço chegará até você para resolver o problema.")
    elif carga == 1:
        print('Qual o tipo de carga você está carregando ?'
              '\nEscolha o múmero que corresponde ao tipo de carga:'
              '\n1 - Viva'
              '\n2 - Perecível'
              '\n3 - Perigosa'
              '\n4 - Seca')
        tipo_carga = (int(input('\nEscolha uma opção: ')))
        peso_carga = (float(input('\nQual o peso da carga (em kg): ')))

    else:
        print("Opção Inválida. Escolha novamente.")
    # Loop para reiniciar o programa --> ainda não aprendemos

    # Etapa 6: Escolha do Modal
    # No projeto, a IA que será desenvolvida, avaliará a melhor opção de modal (ainda não aprendemos, por isso não temos o código aqui)
    # Através da vinculação do banco de dados do detran + modificações , e escolherá o melhor prestador para atender ao chamado
    # Melhor prestador = possuir o modal correto e estiver mais próximo do segurado,para que o atendimento possa ser rápido.
    # Apenas o prestador será exibido ao usuário

    # Etapa 7: Acionamento do Prestador
    # Base de dados de Prestadores,esperamos conseguir com a própria Porto.
    # Exemplo para o Programa
    prestador = "Guinchos ABC"
    tempo_entrega = 30
    print()
    print(f'O Prestador Escolhido é o {prestador}.'
          f'\nA previsão de chegada é {tempo_entrega} minutos.')

    # RESUMO
    print()
    print('Resumo do Acionamento do Seguro:')
    # etapa1
    print(f"-Placa: {placa}")
    # etapa2
    print(f'-Modelo: {modelo}')
    # etapa3
    if opcao_dados == 1:
        print("-Cadastro Correto")

    elif opcao_dados == 2:
        if modificacao == 1:
            modificacao = 'Reforço do Eixo'
            print(f'-Cadastro Atualizado.Modificação:{modificacao}')
        elif modificacao == 2:
            modificacao = 'Blindagem'
            print(f'-Cadastro Atualizado.Modificação:{modificacao}')
        else:
            modificacao = 'Rebaixamento de Suspensão'
            print(f'-Cadastro Atualizado.Modificação:{modificacao}')

    # etapa 4
    if problema == 1:
        problema = 'Elétrico'
        print(f'-Problema: {problema}')
    elif problema == 2:
        problema = 'Mecânico'
        print(f'-Problema: {problema}')
    elif problema == 3:
        problema = 'Envolvimento em Acidente'
        print(f'-Problema: {problema}')
    else:
        problema = 'Pneu furado'
        print(f'-Problema: {problema}')

    # etapa5
    if carga == 1:
        if tipo_carga == 1:
            tipo_carga = 'Carga Viva'
            print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg. ")
        elif tipo_carga == 2:
            tipo_carga = 'Carga Perecível'
            print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg.")
        elif tipo_carga == 3:
            tipo_carga = 'Carga Perigosa'
            print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg. ")
        else:
            tipo_carga = 'Carga Seca'
            print(f"-A carga é do tipo {tipo_carga} com o peso {peso_carga} kg.")
    else:
        print(f'-Sem carga ')

    # etapa6 = apenas com IA (ainda não aprendemos)

    # etapa7
    print(f'-Prestador Escolhido:{prestador} '
          f'\n-Previsão de chegada: {tempo_entrega} minutos.')

    print()
    print('1 - Realizar nova operação ou 2 - Encerrar atendimento')
    fim = int(input('Escolha uma das opções:'))
    if fim == 1:
        # Precisaria fazer um loop para o programa reiniciar
        # Como não aprendemos a fazer, fizemos o loop de forma "manual",inserindo o código novamente
        # Loop Manual foi representado nessa etapa --> não vamos fazer novamente, pois se não ficaria o ciclo ficaria "eterno"
        print('Realizar nova operação')
    else:
        print('Atendimento Encerrado')

else:
    print("Atendimento Encerrado")




