from os import strerror
from sys import path

try:
    caracters = contLine = 0
    f = open(f"{path[0]}/text.txt", "rt", encoding="utf-8")
    lines = f.readlines(20)
    while len(lines) != 0:
        for line in lines:
            contLine += 1
            for ch in line:
                print(ch, end="")
                caracters += 1
        lines = f.readlines(10)
    f.close()
    print("\n\nCaracteres en el archivo: ", caracters)
    print("Lineas en el archivo: ", contLine)
except IOError as e:
    print("Se produjo un error de E/O: ", strerror(e.errno))