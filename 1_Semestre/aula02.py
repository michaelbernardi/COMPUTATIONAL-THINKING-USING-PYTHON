import math

# outros tipos de formatação #####################################################################################
Idade_Alvo = 65
Minha_idade=30
# print("Normal",Idade_Alvo)
#
# print("Formatando {}".format(Idade_Alvo))
#
# ## Outras formas
#
# print (f"Segunda forma {Idade_Alvo}")
#
# print("Terceira forma {i}, outro exemplo {n}"\
#       .format(i=Idade_Alvo, \
#               n=Minha_idade))
#apenas uma formatação do print
## nenhuma informação é perdida
#print("A raiz quadrada de 2 é: {:.1f}".format(math.sqrt(2)))




# outros tipos de casting #####################################################################################

## conversão de string para int
### apenas funcionará caso a string seja apenas um número
string_original = "30"
convertido_em_int= int(string_original)
convertido_em_float = float(string_original)
# obs: caso a string seja em formato de float ex: "25.5", você NÃO vai conseguir converter para inteiro
## primeiro terá que converter para float; e depois para inteiro

#print(convertido_em_float)
### o inverso também existe

idade_convertida_em_string = str(Minha_idade)
#print(type(idade_convertida_em_string))


### existe a conversão de int para float e vice versa
ex_float_1=30.0
ex_float_2=30.1
ex_float_3=30.9

# print(int(ex_float_1))
# print(int(ex_float_2))
# print(int(ex_float_3))



# operadores aritméticos #####################################################################################
# + - * /
# % // **
## o resultado de uma divisão em python vai ser sempre float
## o mesmo não acontece com a multiplicação

##Lembrando que o python respeita a ordem matemática de execução de operações
### Ou seja, ** vem antes de / e *
### * e / vem antes de + e -
### caso queira dar prioridade a uma operação, utilizar ()
###Ex:
media= (Minha_idade + Idade_Alvo)/2
'''
Atenção!:

# DIVISÃO INTEIRA -> //
# resto (módulo) -> %

módulo é apenas uma outra forma de se referir ao resto da divisão!
'''
#divisao normal:
# print ("divisão normal",13/5)
# #divisão inteira
# print("divisão inteira",13//5)
# #resto (ou módulo)
# print("resto",13%5)
# #potência
# print(5**2)
#
# #raiz quadrada (square root) -> sqrt
# ## nome_da_biblioteca.funcao
# ### retorna um float
# print("raiz quadrada",math.sqrt(25))




# comparadores #####################################################################################
## não compara o tipo, e sim o valor
#  = é definição
#  == é comparação
# > < == !=
# >= <=
# print(5>2)
# print(type(5>2))
# print()
# print(5>=6)
# print()
# print(5==5.0)
# print()
# print(type(5)==type(5.0))
# print()
# print(5=="5")




#exercícios #####################################################################################

# faça um programa que:
## peça a idade do usuario E de uma outra pessoa
## peça o nome do usuario E da outra pessoa

## calcule a diferença de idade
## calcule a média de idade entre as 2 pessoas
##  faça a comparação se a primeira pessoa é mais velha que a segunda

### imprima na tela os nomes com as idades e os resultados das operações acima

Primeiro_nome = input("Digite o nome do usuario 1 ")
Segundo_nome = input("Digite o nome do usuario 2 ")
#
# #o input e conversão podem ser feitas de duas formas:
# # opção 1
# #Idade_usuario_1 = input("Digite a idade do usuario 1")
# #Idade_usuario_1_convertida=int(Idade_usuario_1)
# #opção 2:
Idade_usuario_1_convertida=int(input("Digite a idade do usuario {} ".format(Primeiro_nome)))
Idade_usuario_2_convertida=int(input("Digite a idade do usuario {} ".format((Segundo_nome))))

# print(Idade_usuario_1_convertida)
# print(type(Idade_usuario_1_convertida))

print("A diferença de idade entre {} e {} é de {} anos"\
      .format(Primeiro_nome,\
              Segundo_nome,\
              Idade_usuario_1_convertida-Idade_usuario_2_convertida))

soma_das_idades = Idade_usuario_1_convertida+Idade_usuario_2_convertida
media_de_idade = soma_das_idades /2

print("A media de idade entre {} e {} é de {:.1f} anos"\
      .format(Primeiro_nome,\
              Segundo_nome,\
              media_de_idade))

print("{} é mais velho que {}?{}".format(Primeiro_nome,Segundo_nome,\
                                         Idade_usuario_1_convertida>Idade_usuario_2_convertida))
