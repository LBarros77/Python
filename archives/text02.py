from os import strerror
from sys import path

cont = contLine = 0
try:
    s = open(f"{path[0]}/text.txt", "rt")
    line = s.readline()
    while line != "":
        contLine += 1
        for ch in line:
            print(ch, end="")
            cont += 1
        line = s.readline()
    s.close()
    print("\n\nCaracteres en el archivo: ", cont)
    print("Lineas en el archivo: ", contLine)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))