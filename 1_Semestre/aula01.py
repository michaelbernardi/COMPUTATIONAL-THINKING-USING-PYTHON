'''
Isto é um comentário em bloco
Pode fazer várias linhas
Sem colocar # na frente
'''

"""
Pode ser com qualquer aspas
"""


# Isto é um comentário # vai continuar sendo um comentário
#
# #este numero TEM QUE SER inteiro
# numero_qualquer = 2  #comentários na mesma
#
# float_qualquer = 2.0
#
# string_qualquer= " 'dois' "
# dois_em_string="2"
#
#
# variavel_logica= True
# outra_logica= False

#idade em anos inteiros
Minha_idade = 30

Idade_alvo=65

Idade_ate_aposentadoria=Idade_alvo-Minha_idade

#print("Olá Mundo!")

#print("Anos até a aposentadoria: {}. \n Isto porque você tem {} anos".format(Idade_ate_aposentadoria,Minha_idade))

#print("Anos até a aposentadoria: {}".format((Idade_ate_aposentadoria)))
#print("Isto porque você tem {} anos hoje".format(Minha_idade))

Idade_do_usuario_string=input("Digite a sua idade")

Idade_do_usuario_em_inteiro=int(Idade_do_usuario_string)

print("O tipo da variavel de entrada é:{}".format(type(Idade_do_usuario_string)))

print("O tipo da variavel convertida é:{}".format(type(Idade_do_usuario_em_inteiro)))

print()
tempo_para_aposentadoria = Idade_do_usuario_em_inteiro - Idade_alvo
print("Faltam {} anos para o usuário se aposentar".format(tempo_para_aposentadoria))