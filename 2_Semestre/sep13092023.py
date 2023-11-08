# class DivisaoPorZero(ZeroDivisionError):
#     pass
#
# def calcula_divisao():
#     while True:
#         message = ""
#         try:
#             num_1 = int(input("Digite o numerador: "))
#             num_2 = int(input("Digite o denominador: "))
#             div = num_1 / num_2
#         except ValueError:
#             message = "Os valores inputados não são numéricos"
#         except ZeroDivisionError:
#             raise DivisaoPorZero("Impossível dividir por zero.")
#         else:
#             message = f"Divisão realizada com sucesso, valor {div}"
#             return div
#         finally:
#             print(message)
#             print()
#
#
# # print(calcula_divisao())
#
#
# with open('arquivo.txt', 'w') as arquivo:
#     arquivo.write('abacate')
#
#
# try:
#     arquivo = open('arquivo.txt', 'w')
#     arquivo.write('abacate')
# except Exception:
#     pass
# else:
#     pass
# finally:
#     arquivo.close()


# 2 - Erro de Divisão por Zero:
# Peça ao usuário para inserir dois números e realize uma divisão.
# Use try e except para lidar com a exceção de divisão por zero e imprima uma mensagem apropriada.

# while True:
#     try:
#         num_1 = int(input("Digite o numero 1: "))
#         num_2 = int(input("Digite o numero 2: "))
#         div = num_1/num_2
#     except ZeroDivisionError:
#         print("Impossível dividir por zero.")
#     except ValueError:
#         print("Digite apenas carectes numéricos.")
#     else:
#         print(f"O valor da divisão de {num_1} por {num_2} é {div}")
#     finally:
#         print()
#
#
# def captura_numero(idx):
#     while True:
#         try:
#             num = int(input(f"Digite o numero {idx}: "))
#         except ValueError:
#             print("Digite apenas carectes numéricos.")
#         else:
#             return num
#         finally:
#             print()
#
# n = 2
# while True:
#     nums = []
#     for i in range(n):
#         nums.append(captura_numero(i))
#     try:
#         div = nums[0] / nums[1]
#     except ZeroDivisionError:
#         print("Impossível dividir por zero")
#     else:
#         print(f"A divisão de {nums[0]} por {nums[1]} é {div}")
#         break
#     finally:
#         print()


# 1 - Calculadora de Idade com Tratamento de Data de Nascimento:
# Peça ao usuário para inserir sua data de nascimento no formato "dd/mm/aaaa".
# Utilize try, except para capturar erros de entrada e calcular a idade da pessoa.
# Em seguida, use um bloco else para exibir a idade calculada e um bloco finally
# para agradecer ao usuário por usar a calculadora.

from datetime import datetime

while True:
    try:
        nasc = datetime.fromisoformat(input("Digite sua data de nascimento no formato aaaa-mm-dd: "))  # aaaa-mm-dd
    except ValueError:
        print("Digite uma data válida, de acordo com o padrão aaaa-mm-dd")
    else:
        today = datetime.today()
        idade_anos = int((today - nasc).days/365)
        print(f"Você possui {idade_anos} anos")
        break
    finally:
        print()
