## OBSERVAÇÃO:
# para fazer o case ser comparado com variáveis (ao invés de números fixos), tem que usar a condição if:
# num=10
#
# match num:
#     case 0: print("o numero é 0")
#
# num1=float(input("diga sua idade"))
# num2=float(input("diga idade de outro usuario"))
#
# match num1:
#     case _ if num1==num2:
#         print("iguais")
#     case _ if num1>num2:
#         print("num1 maior que num2")
#     case _ if num1<num2:
#         print("num2 maior que num1")


## exercício extra: repita o exercício anterior,
# desta vez começando com a comparação numero>=200

# #### exercício extra: completar a lógica que falta ( 2==1 (>3 e <3) , 3==1(>2 e <2) )
# #### ao completar, o else pode conter no máximo 1 condição

'''4)	Solicite ao usuário (separadamente) o mês do ano, e o dia atual.
 Diga em qual estação estamos
ex: 28 de março -> primeiro input = 3, segundo input = 28
Outono : De 22 de março a 21 de junho.
Inverno: De 22 de junho a 23 de setembro.
Primavera: De 24 de setembro a 21 de dezembro.
Verão: De 22 de dezembro a 21 de março.

similar ao das notas, só que agora cada mês tem mais condições

-- Temos 8 meses que a estação não muda:
---- jan,fev,abr,mai,jul,ago,out,nov
-- para cada 2 deles, temos mesma estação. Então podemos fazer:
if mes=="jan" or mes=="fev":
    print("a estação é verão")
elif [...] # teremos mais 3 elifs para os outros 6 meses
-- sobram 4 meses nos quais a estação muda
elif mes=="mar": #temos que verificar se passou do dia 21
    if dia<=21:
        print("estamos no verao")
    else: #maior ou igual a 22
        print("estamos no outono")
[...] #similar para os outros 3 meses
Caso a gente faça desta forma, nosso else ficaria "vazio".
Podemos utilizar para fazer um tratamento de erro
'''

# https://codingbat.com/python
# utilziar ao final: return resposta




# LOOP (laços - ciclo)

## for (para cada) -> loop "pré-determinado" - condição de parada pré programada
## while (enquanto) -> loop "pós-determinado" - condição de parada que pode ser desconhecida

### situação onde você quer repetição de um conjunto de comandos
### até que uma situação se satisfaça

# range (alcance)
# parâmetros: início, fim, tamanho do passo
# se você não digitar nada, o começo é sempre 0
# se você não digitar nada, o passo é sempre 1
# ele para ANTES do fim (ou seja, NÃO INCLUI O FIM)

# range(10) #lista de números começando em 0, que crescem de 1 em 1, e terminam ANTES do 10

## pass significa "passe" , ou seja, "não faça nada"



#
# for i in range(5):
#     print(i)
#     # i*=2  #é igual a i=i*2
#     # print(i)
#     #
#     # # print("---------------------------")
#     # if i%2==0:print(f"{i} é par")
#     # else:print(f"{i} é ímpar")
#     print()


#para cada numero de 0 a 4, imprima a soma dos anteriores a ele (positivos)
soma=0
for i in range(5):
    print(i)
    soma+=i  #igual a soma=soma+i


# imprima apenas o quinto elemento da sequencia fibonacci
# atual=1
# anterior=0
# for i in range(3,5):
#     soma=anterior+atual
#     anterior=atual
#     atual=soma
# print(atual)


## EXERCÍCIO:
# Faça um programa em loop que imprima esta imagem:
'''
*
**
***
****
*****
****
***
**
*
'''