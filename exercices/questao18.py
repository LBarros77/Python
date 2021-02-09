def busca(x, lst):
    lst2 = []
    for i in lst:
        if x in i:
            lst2.append(i)
    return lst2

print(busca("Maracatu", ["Samba", "Maracatu Rural", "Frevo",
"Maraca", "Maracatu Nação", "Maravilha", "Cavalo Marinho",
"Maracatus"]))