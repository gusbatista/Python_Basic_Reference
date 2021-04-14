###################################
# Lists
#

#
# Acessando conteudo da lista
#
carros = ['Uno','Palio','Bravo','Punto']
#print(carros[1])   # Palio

#
# Copiando lista
#
pesDeBoi  = carros
#print(pesDeBoi[2])  #Bravo

#
# Juntando duas listas
#
onibus = ['Ciferal','Mercedes']
automoveis = onibus + carros
#print(automoveis)   # ['Ciferal','Mercedes','Uno','Palio','Bravo','Punto']

#
# Loop baseado em lista com construcao "in" e "for"
#
carros = ['Uno','Palio','Bravo','Punto']
#for auto in carros:
 #print(auto + " nao eh la muito bom") # Uno nao eh la muito bom
                                      # Palio nao eh la muito bom
                                      # Bravo nao eh la muito bom
                                      # Punto nao eh la muito bom

#
# Checando se ha elemento na lista com "in"
#
carros     = ['Uno','Palio','Bravo','Punto']

if "Uno" in carros:
    print("Uno is on the list =-)")
else:
    print("Uno nao esta la =-()")
if "Peugeot" in carros:
    print("Peugeot is on the list")
else:
    print("Peugeot nao esta la =-()")  # Uno is on the list =-)
                                       # Peugeot nao esta la =-(

#
# Invertendo lista
#
carros     = ['Uno','Palio','Bravo','Punto']
carros.reverse()
print(carros)
# Prints: ['Punto', 'Bravo', 'Palio', 'Uno']
