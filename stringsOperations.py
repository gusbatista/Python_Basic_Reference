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
# Metodos Uppercase and Lowercase
# Obs: metodos sao funcoes built in especificas para Strings
#
anotherString = "Eita Lele, sai pra la!"
#print(anotherString.lower())
#print(anotherString.upper())

#
# Metodo para busca da posicao de uma string dentro de string
#
anotherString  = "Eita Lele, sai pra la!"
lelePosition   = anotherString.find("Lele")
blablaPosition = anotherString.find("Blabla")
#print(lelePosition)      # Resultado: 5
#print(blablaPosition)    # Resultado: -1 (String nao encontrada)

#
# Metodo para encontrar e substituir substring da String
#
randomString = "Hoje eh dia de Folia!!!"
newString    = randomString.replace("dia","noite")
#print(newString)   ### Hoje eh noite de Folia

#
# Metodo para quebrar String baseado num delimitador
#
moreAndMoreString = "All we need is love!"
splitedString     = moreAndMoreString.split("need")
#print(splitedString)    # ['All we ',' is love!']
#print(splitedString[0]) # All we

#
# Obter substring de uma String pela posicao
#
fatherString   = "O dia estava muito ensolarado hoje"
sonString      = fatherString[6:11]
sonString2     = fatherString[6:]
daughterString = fatherString[-6:]
daughterString2= fatherString[:-8]
#print(sonString)       # estav   (Obtem string da posicao 6 ate 11 nao inclusa)
#print(sonString2)      # estava muito ensolarado hoje (da posicao 6 ate o fim)
#print(daughterString)  # o hoje (da posicao 6 de tras pra frente ate o fim)
#print(daughterString2) # O dia estava muito ensolar (do inicio ate pos 8 de tras pra frente)
