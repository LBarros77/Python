def includeContact(name, x):
    x[name] = input("Digite o número: ")
    return x

def includePhone(name, x):
    if name in x:
        num = input("Digite o número: ")
        x[name] = [x[name], num]
        return x
    else:
        question = input("O nome digitado não está na agenda, você deseja adiciona-lo?(y/n) ")
        if question == "y":
            x[name] = input("Digite o número: ")
            return x
        else:
            return x

def deletPhone(name, x):
    x[name] = ""
    return x

def deletName(name, x):
    del x[name]
    return x

def getContact(name, x):
    if name in x:
        print(x.get(name))
    else:
        print("Este contato não existe")
    
def enunciado():
    comand = {"a": "Incluir novo nome",
              "b": "Incluir telefone",
              "c": "Excluir telefone",
              "d": "Excluir nome",
              "e": "Consutar telefone",
              "f": "Sair"}

    for k, v in comand.items():
        print(k,":", v)

    print("-"*55, "\n")

schedule = {"Gaby":99235711, "Brenda": [96340221, 92667190]}
enunciado()

while True:
    option = input("Escolha um comando: ")
    name = input("Nome do contato: ")
    if option == "a":
        includeContact(name, schedule)
    elif option == "b":
        includePhone(name, schedule)
    elif option == "c":
        deletPhone(name, schedule)
    elif option == "d":
        deletName(name, schedule)
    elif option == "e":
        getContact(name, schedule)
    else:
        break
    print()

