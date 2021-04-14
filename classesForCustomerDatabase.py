class customerRegistry:
    "Classe que define template do cadastro de clientes"
    def __init__(self,name,age,address,city,state,phone):
        self.name    = name
        self.age     = age
        self.address = address
        self.city    = city
        self.state   = state
        self.phone   = phone

def Main():
    print(customerRegistry.__doc__)
    # Prints: Classe que define template do cadastro de clientes
    print("Bem vindo ao cadastro de clientes!")
    print("Digite os dados do cliente:","\n")
    customerName  = input("Nome:")
    customerAge   = int(input("Idade:"))
    customerAdd   = input("Endereco:")
    customerCity  = input("Cidade:")
    customerSt    = input("UF:")
    customerPhone = input("Telefone:")
    client1 = customerRegistry(customerName,customerAge,customerAdd,customerCity,customerSt,customerPhone)
    print("\n")
    print("Por favor confirme os dados:")
    print("Nome do Cliente : " + client1.name.upper())
    print("Idade           : " + str(client1.age))
    print("Endereco        : " + client1.address.upper())
    print("Cidade          : " + client1.city.upper())
    print("UF              : " + client1.state.upper())
    print("Telefone com DDD: " + str(client1.phone))
    option = ""
    while((option.upper() != "S") and (option.upper() != "N")):
        option = input("Confirmar? (S/N)")

Main()
