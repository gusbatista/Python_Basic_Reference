#
# Shalow Copy Vs Deep Copy
#
# No Python, por default, quando uma variavel faz referencia a outra ela passa
# a apontar para a mesma area de memoria que a variavel original. Com isso,
# uma mudanca na variavel original acarreta mudanca na variavel de referencia.
#
# Exemplo:
#
carros     = ["Uno","Fusca","Corolla"]
automoveis = carros

print(carros)          #  ['Uno', 'Fusca', 'Corolla']
print(automoveis)      #  ['Uno', 'Fusca', 'Corolla']

carros[0] = "Corsa"

print(automoveis)   # ['Corsa', 'Fusca', 'Corolla']

#
# Para evitar isso pode-se usar a copia com a referencia ":" ...
#
carros = ["Uno","Fusca","Corolla"]

automoveis = carros[0:]

carros[0] = "Corsa"

print(carros)      # ['Corsa', 'Fusca', 'Corolla']
print(automoveis)  # ['Uno', 'Fusca', 'Corolla']

#
# ... ou ainda usar a funcao deepcopy (copia "profunda"). Essa funcao aloca
# um novo espaco em memoria com uma copia efetiva do valor da variavel original
#

from copy import deepcopy

carros     = ["Uno","Fusca","Corolla"]
automoveis = deepcopy(carros)

carros[0] = "Corsa"

print(carros)      # ['Corsa', 'Fusca', 'Corolla']
print(automoveis)  # ['Uno', 'Fusca', 'Corolla']
