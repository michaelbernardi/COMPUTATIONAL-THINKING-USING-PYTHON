
#EXERCÍCIOS:
# 1)No exemplo anterior, travar para que o número seja inteiro

n1=float(input("Diga um número inteiro"))
while n1!=int(n1):
    print("Você não digitou um número nas condições necessárias. Favor tente novamente")
    n1 = float(input("Diga um número inteiro"))

n2 = float(input("Diga um número inteiro"))
while n2 != int(n2):
    print("Você não digitou um número nas condições necessárias. Favor tente novamente")
    n2 = float(input("Diga um número inteiro"))

n1=int(n1)
n2=int(n2)
# 2)imprima a tabuada do número 5, de 0 e 10, inclusive.
# # Depois, adapte o programa para receber dois números do usuário: o de início e o de fim

# for i in range(n1,n2+1,1): #o range só aceita números inteiros
#     print(5*i)
## precebemos que n1 não pode ser maior que n2 nesta configuração
### temos 2 formas de resolver: OU travar para que n2 seja maior que n1
### OU fazer um if, e escrever o range de acordo
# EXERCÍCIO: fazer as duas opções

### opção 1:

n2 = float(input(f"Diga um número inteiro maior que {n1}"))
while n2 != int(n2) or n2<n1:
    print("Você não digitou um número nas condições necessárias. Favor tente novamente")
    n2 = float(input(f"Diga um número inteiro maior que {n1}"))


### opção 2:
if n2>=n1:
    for i in range(n1,n2+1,1): #o range só aceita números inteiros
        print(5*i)
else:
    for i in range(n2,n1+1,1):
        print(5*i)

# 3) faça um programa que imprima apenas os números pares no intervalo de n1 (inclusive) até n2 (exclusive)
# onde n1 e n2 são números dados pelo usuário, e deverão ser inteiros. Além disto, n2 deve ser maior que n1

n1=float(input("Diga um número inteiro"))
while n1!=int(n1):
    print("Você não digitou um número nas condições necessárias. Favor tente novamente")
    n1 = float(input("Diga um número inteiro"))
n2 = float(input(f"Diga um número inteiro maior que {n1}"))
while n2 != int(n2) or n2<n1:
    print("Você não digitou um número nas condições necessárias. Favor tente novamente")
    n2 = float(input(f"Diga um número inteiro maior que {n1}"))

n1=int(n1)
n2=int(n2)

soma = 0
for i in range(n1,n2):
    if i%2==0:
        soma+=i
    else:pass
print(soma)

# 4) faça um programa que , ao usuário digitar um número, obrigatoriamente inteiro, imprima os 20 números subsequentes
# Caso, após estes 20 número sejam negativos, dizer quanto falta para chegar a 0
#
n1=float(input("Diga um número inteiro"))
while n1!=int(n1):
    print("Você não digitou um número nas condições necessárias. Favor tente novamente")
    n1 = float(input("Diga um número inteiro"))
n1=int(n1)
for i in range(n1+1,n1+21):
    print (i)
#após o loop
if i<0:
    print ("Para chegar a 0 falta",i*-1)


# 5) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos

n1=float(input("Diga um número inteiro entre 1 e 20"))
while n1!=int(n1) or n1<1 or n1>20:
    print("Você não digitou um número nas condições necessárias. Favor tente novamente")
    n1 = float(input("Diga um número inteiro entre 1 e 20"))
n1=int(n1)

maior_valor=float('-inf') #menor valor possível em python
menor_valor=float("inf") #maior valor possível em python
soma=0
media=0
qt_pos=0
qt_neg=0
for i in range(n1): #não vamos usar o i para nada,apenas para contar quantas vezes estamos fazendo
    num_temp=float(input(f"diga um número quaquer (etapa {i+1} de {n1}): "))
    if num_temp>maior_valor:
        maior_valor=num_temp
    if num_temp<menor_valor:
        menor_valor=num_temp
    soma+=num_temp
    media+=num_temp/n1
    if num_temp>=0:
        qt_pos+=1
    else:
        qt_neg+=1

print(f"O maior valor é {maior_valor}")
print(f"O menor valor é {menor_valor}")
print(f"A soma dos valores é {soma}")
print(f"a médida dos valores é {media}")
print(100*qt_neg/n1,"% dos valores foram negativos")
print(100*qt_pos/n1,"% dos valores foram positivos")