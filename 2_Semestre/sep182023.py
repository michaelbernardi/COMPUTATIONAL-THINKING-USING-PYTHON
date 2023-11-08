# Exercício Try/except com strftime

# 1 - Calculadora de Idade com Tratamento de Data de Nascimento:
# Peça ao usuário para inserir sua data de nascimento no formato "dd/mm/aaaa".
# Utilize try, except para capturar erros de entrada e calcular a idade da pessoa.
# Em seguida, use um bloco else para exibir a idade calculada e um bloco finally
# para agradecer ao usuário por usar a calculadora.

# datetime.strptime('18/09/2023', '%d/%m/%Y')
# Ref: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes




# while True:
#

from datetime import datetime



# 18/09/2023 18-09-2023
# 31/09/2023

class DataInvalidaError(ValueError):
    ...

now = datetime.now()
while True:
    try:
        data_nascimento = input("Digite a data de nascimento no formato dd/mm/yyyy: ")
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        if data_nascimento > now:
            raise DataInvalidaError("A data inserida é maior que a data de hoje.")
    except DataInvalidaError as die:
        print(die)
    except ValueError:
        print("Data inválida. Atente-se ao formato dd/mm/yyyy.")
        print("Tente novamente")
        print()
    except KeyboardInterrupt:
        print("\nNão to afim!")
    else:
        idade = (now - data_nascimento).days
        idade_anos = idade // 365
        idade_meses = idade % 365 // 30
        idade_dias = idade % 365 % 30
        print(f"Sua idade é {idade_anos} anos, {idade_meses} meses e {idade_dias} dias")
        break
    # finally:

print("Obrigado por utilizar a calculadora")





















# API Intro
# Exemplo https://www.google.com.br/search?q=
#
#
#
# registro = [{....}]
#
# def search(q):
#     for registro in registros:
#         if q in registro.keys():
#             return registo





