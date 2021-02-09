print("Compara duas strings")
string1 = input("String 1: ")
string2 = input("String 2: ")

print(f'Tamanho de "{string1}": {len(string1)} caracteres')
print(f'Tamanho de "{string2}": {len(string2)} caracteres')

if len(string1) == len(string2):
    print("As duas strings são de tamanhos iguais")
else:
    print("As duas strings são de tamanhos diferentes")

if string1 == string2:
    print("As duas strings possuem conteúdos iguais")
else:
    print("As duas strings possuem conteúdos diferentes")