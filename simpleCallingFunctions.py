#
# Funcao Simples que eleva um numero ao cubo
#
def calculateCube(number):
    result = number*number*number
    return result;

#
# Funcao Simples que eleva dois numeros ao cubo e retorna ambos resultados
#
def calculateTwoCubes(number1,number2):
    result1 = number1*number1*number1
    result2 = number2*number2*number2
    return result1,result2

#
# Funcao que pode receber um ou dois numeros, eleva ambos ao cubo
# e retorna os dois resultados. Se for passado apenas um numero, o
# segundo por default eh 2
#
def calculateOneOrTwoCubes(number1,number2 = 2):
    result1 = number1*number1*number1
    result2 = number2*number2*number2
    return result1,result2

#
# Funcao que pode receber qualquer quantidade de numeros, calcula o cubo
# de todos e retorna todos os resultados. Essa funcao engloba a funcionalidade
# de todas acima
#
def calculateAnyNumberOfCubes(*numberList):
    resultArray = []
    for number in numberList:
        resultArray.append(number*number*number)
    return resultArray

#
#
# Main Code
#

x = calculateCube(8)
#print(x)   ### 512

[y,z] = calculateTwoCubes(9,10)
#print(y)
#print(z)
            ### 729
            ### 1000

[a,b] = calculateOneOrTwoCubes(5,4)
[c,d] = calculateOneOrTwoCubes(6)

#print(a)  ### 125
#print(b)  ### 64
#print(c)  ### 216
#print(d)  ### 8

[f,g,h,i,j] = calculateAnyNumberOfCubes(7,5,4,3,6)
print(f)  ### 343
print(g)  ### 125
print(h)  ### 64
print(i)  ### 27
print(j)  ### 216
