lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
    print(x, end=" ")
print()