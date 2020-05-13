##################################################
# Strings Operation
#

#
# Merge de Strings
#
myQuestion = "Ola, como vai? Tudo bem?"
myAnswear  = "Comigo tudo ok!"

mergedString = myQuestion + " " + myAnswear
#print(mergedString)

#
# Obter Caracter de Strings
#
characterOfMyQuestion        =  myQuestion[0]
anotherCharacterOfMyQuestion =  myQuestion[7]
#print(characterOfMyQuestion)
#print(anotherCharacterOfMyQuestion)

#
# Obter tamanho de Strings
#
myAnswearSize = len(myAnswear)
#print(myAnswearSize)

#
# Converter variavel Nao String em String
#

x = 8
brandNewString = "Carol tem" + " x " + "anos" # Carol tem x anos
#print(brandNewString)

brandNewString = "Carol tem " + str(x) + " anos" # Carol tem 8 anos
#print(brandNewString)

#
# Metodos Up and Lowercase
# Obs: metodos sao funcoes built in especificas para Strings
#

anotherString = "Eita Lele, sai pra la!"
#print(anotherString.lower())
#print(anotherString.upper())

#
# Metodo para busca de string dentro de string
#
anotherString  = "Eita Lele, sai pra la!"
lelePosition   = anotherString.find("Lele")
blablaPosition = anotherString.find("Blabla")
#print(lelePosition)      # Resultado: 5
#print(blablaPosition)    # Resultado: -1 (String nao encontrada)
