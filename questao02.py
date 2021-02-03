name = input("Digite seu nome: ")
for letter in range(len(name)):
    print(" " * len(name[:letter]) + name[letter:])