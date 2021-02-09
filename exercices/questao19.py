def eliminarRepetidos(lst):
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return lst2

print(eliminarRepetidos([1, 2, 4, 4, 3, 8, 5, 2]))