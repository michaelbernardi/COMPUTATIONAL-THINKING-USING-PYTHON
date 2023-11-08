### 20 de março, primeiro CP

# Correção dos exercícios da aula passada

#fluxogramas | pseudocódigo ###################################################################

#exemplos teóricos:

## calcular a autonomia do automóvel do usuário
'''
definir que a autonomia seria em km/l
solicitar ao usuário a quantidade de km percorridos
solicitar ao usuário a volume de combustível gasto (em L) para percorrer esta distância
converte (casting) e faz a conta
retorna ao usuário a autonomia de seu veículo
'''

## calcular o custo mensal com combustível do usuário
'''
--> já possuimos a autonomia do automóvel do usuário (em Km/l)
(frequencia de abastecimento   "3")
solicitar ao usuário a média de km rodados por dia útil
transformar a média diária em média mensal
calcular o consumo em L médio no mês -> 

    15km   - >    1L
    800km  - >    XL
    
    15X = 800
    X = 800/15
    x= 53.33333333333333333333L
OU solicitar ao usuário o preço que ele pagou no litro <-- (R$ 5)
OU buscar em bancos de dados/fontes externas

multiplicar o preço pela quantidade consumida
53.33333333333333 * 5 = 266,67
retornar a resposta ao usuário
'''
#primeiro input
media_km_por_dia = float(input("Diga sua média de km rodados por dia útil: "))

#dados vindos do programa anterior
autonomia_em_km_por_L = 15

#calculando dados intermediários
media_km_mensal = media_km_por_dia * 20
media_litros_por_mes = media_km_mensal/autonomia_em_km_por_L

#segundo input
preco_por_litro = float(input("Diga quanto você pagou em reais por litro de gasolina:"))

valor_gasto_mensal = media_litros_por_mes * preco_por_litro

print("Você gasta, em média, por mês {:.2f} R$ com combustível".format(valor_gasto_mensal))



## calcular o menor número de notas necessárias para pagar este custo mensal
