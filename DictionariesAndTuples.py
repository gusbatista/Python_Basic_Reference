#
# Dicionarios - Similar ao Hash do Perl. Conjuntos de pares key-value
#
portugueseColors = ['azul','roxo','verde','rosa']
englishColors    = ['blue','purple','green','pink']

#
# Dicionario Vazio
#
transDictionary = {}
#print(transDictionary)    ### {}

#
# Prenchendo Dicionario com iteracoes
#
i = 0
for item in portugueseColors:
    transDictionary[item] = englishColors[i]
    i = i+1

#print(transDictionary)
     ### {'azul': 'blue', 'roxo': 'purple', 'verde': 'green', 'rosa': 'pink'}

#
# Tamanho do Dicionario
#
#print(len(transDictionary))  ### 4 (quantidade de pares key-value)

#
# Removendo par key-value
#
del(transDictionary['azul'])
#print(transDictionary)
     ### {'roxo': 'purple', 'verde': 'green', 'rosa': 'pink'}

#
# Inserindo par key-value
#
transDictionary['vermelho'] = "red"
#print(transDictionary)
     # {'roxo': 'purple', 'verde': 'green', 'rosa': 'pink', 'vermelho': 'red'}

#
# Verificando presenca de uma key no Dicionario
#

#if "vermelho" in transDictionary:
#    print('Ha vermelho no dicionario e sua traducao eh: ' + str(transDictionary['vermelho']))
    ### Ha vermelho no dicionario e sua traducao eh: red

colorsToCheck = ['amarelo','verde','marrom','cinza','roxo']

#for item in colorsToCheck:
#    if item in transDictionary:
#        print('Ha ' + str(item) + ' no dicionario e sua traducao eh: ' + str(transDictionary[item]))
#    else:
#        print('Nao ha ' + str(item) + ' no dicionario')

#
# Obtendo keys do dicionario numa lista
#
dictionaryKeys = sorted(transDictionary)
print(dictionaryKeys)   ### ['rosa', 'roxo', 'verde', 'vermelho']
#
# Tuplas
# --> Estrutura similar as listas, mas sao estaticas, ou seja,
#     uma vez criadas nao podem ter elementos removidos ou
#     acrescentados. As tuplas so podem ser lidas ou copiadas
#

#
# Criando Tuplas...
#
myTuple = ("aaa","bbb","ccc","ddd")
#print(myTuple)             ### ("aaa","bbb","ccc","ddd")

#
# Tupla a partir de uma String
#
anotherTuple = tuple('aabbccdd')
#print(anotherTuple)    ### ('a', 'a', 'b', 'b', 'c', 'c', 'd', 'd')

#
# Copiando Tupla ou parte da Tupla
#
copiedTuple  = myTuple
subTuple     = myTuple[:2]
tupleElement = myTuple[3]
#print(copiedTuple)         ### ("aaa","bbb","ccc","ddd")
#rint(subTuple)            ### ("aaa","bbb") - O elemento 2 eh nao incluso
#print(tupleElement)        ### ddd
#print(len(tupleElement))   ### 3

#
# Tamanho da Tupla
#
#print(len(myTuple))   ###  4

#
# Funcao Type - Identifica tipo de variavel
#
#print(type(myTuple))        ### <class 'tuple'>
#print(type(tupleElement))   ### <class 'str'>
