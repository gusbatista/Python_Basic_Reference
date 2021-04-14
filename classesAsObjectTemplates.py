#
# Classes: template de uma estrutura de dados que abriga variaveis e
#          funcoes. Esse template pode dar origem a objetos.
#
# As classes, ao serem criadas, ja definem algumas funcoes intrinsecas. Por
# exemplo: __init__(), __doc__(), etc.

class extremelySimpleCalc:
    "Classe que contem Operacoes Basicas de Calculadora"
#
#   Funcao soma
#
    def sum(self,num1,num2):
        result = num1 + num2
        return result
#
#   Funcao subtracao
#
    def sub(self,num1,num2):
        result = num1 - num2
        return result
#
#   Funcao Divisao
#
    def div(self,num1,num2):
        result = num1/num2
        return result
#
#   Funcao Multiplicacao
#
    def mul(self,num1,num2):
        result = num1*num2
        return result

def Main():
    print(extremelySimpleCalc.__doc__)
    # Prints "Classe que contem Operacoes Basicas de Calculadora"

    #
    # Criando o objeto calc com o template extremelySimpleCalc
    #
    calc = extremelySimpleCalc()
    a = int(input("Digite primeiro numero:"))
    b = int(input("Digite segundo numero:"))

    print("Soma      = " + str(calc.sum(a,b)))
    print("Subtracao = " + str(calc.sub(a,b)))
    print("Divisao   = " + str(calc.div(a,b)))
    print("Produto   = " + str(calc.mul(a,b)))
    # Prints:   Soma      = 6
    #           Subtracao = 2
    #           Divisao   = 2.0
    #           Produto   = 8
    d = calc.sum(4,6)
    print(d)
    # Prints 10

def SecundaryFunction():
    #
    #Criando objeto calc a partir da Classe...
    #
    calc = extremelySimpleCalc()
    f    = calc.sum(4,6)
    print(f)
    #
    #Prints:  10
    #

Main()
SecundaryFunction()
