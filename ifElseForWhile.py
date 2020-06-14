#
# Condicoes - if / else
#
# Em Python, 0 e Null sao False e qualquer outra coisa eh True
#
var = 5
if var:
    print ("Var tem um valor valido")
else:
    print("Var tem um valor False")
    ### Var tem um valor valido

var = 0
if var:
    print ("Var tem um valor True")
else:
    print("Var tem um valor Vazio")
    ### Var tem um valor Vazio

var = ""
if var:
    print ("Var tem um valor True")
else:
    print("Var tem um valor Vazio")
    ### Var tem um valor Vazio

#
# Comparadores:     Igual                   ==
#                   Diferente               != ou <>
#                   Menor/Maior             </>
#                   Menor/Maior ou Igual    <=/>=
#

#
# Loop com while (uso identico as outras linguagens)
# porem adicionando o operadora ":" tipico do Python
#
# Obs: para fazer a negacao no while (equivalente ao "!"
# do Perl) use "not".
#
# Exemplo: while not(idade <= 18): ...
#
#idade = 3
#while(idade <= 18):
#    print("Feliz aniversario de " + str(idade) + "!!!")
#    idade = idade + 1

    ### Feliz aniversario de 3!!!
    ### Feliz aniversario de 4!!!
    ### (...)
    ### Feliz aniversario de 18!!!

#
# Loop com for (como ocorre em outras linguagens, mais
# economico que o while)
#
for idade in range(3,18):
    print("Feliz aniversario de " + str(idade) + "!!!")
