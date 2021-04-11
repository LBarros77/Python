from sys import path

with open(path[0] + "/lista-de-compras.txt", "r") as f:
    informations = f.readlines()

lst = [i[:-1].split(":") for i in informations]
print(sum([float(ind[1]) for ind in [i[1].split(" ") for i in lst]]))