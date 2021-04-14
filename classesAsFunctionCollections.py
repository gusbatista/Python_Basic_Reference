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
    a = int(input("Digite primeiro numero:"))
    b = int(input("Digite segundo numero:"))

    print("Soma      = " + str(extremelySimpleCalc.sum(0,a,b)))
    print("Subtracao = " + str(extremelySimpleCalc.sub(0,a,b)))
    print("Divisao   = " + str(extremelySimpleCalc.div(0,a,b)))
    print("Produto   = " + str(extremelySimpleCalc.mul(0,a,b)))
    # Prints:   Soma      = 6
    #           Subtracao = 2
    #           Divisao   = 2.0
    #           Produto   = 8
    d = extremelySimpleCalc.sum(0,4,6)
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
    #Prints:  Traceback (most recent call last):
    #         f    = calc.sum(4,6)
    #         TypeError: sum() takes 2 positional arguments but 3 were given
    #
    # >>> Toda vez que um objeto (no caso "calc") chama uma de suas funcoes,
    #     ele sempre se passa como argumento. Por isso, apesar da chamado
    #     do metodo calc.sum ter passado 2 argumentos o erro fala em 3!
    #     Isso ocorreu porque a funcao "sum" na classe foi definida assim:
    #     "def sum(num1,num2)". Corrigimos o problema redefinindo-a como
    #     "def sum(self,num1,num2)"
    #

Main()
SecundaryFunction()
