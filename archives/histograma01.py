'''
Pasos:
Pida al usuario el nombre del archivo de entrada.
Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y minúsculas se tratan como iguales).
Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos distintos de cero).
Questión:
Crea un archivo de prueba para tu código y verifica si tu histograma contiene resultados válidos.
'''
from sys import path

try:
    fl = f"{path[0]}/" + input("Escribe el nobre del archvo: ")
    with open(fl, "w") as f:
        f.write("aBca")
except Exception as e:
    print(e)
    
dic = {}

try:
    f = open(fl, "r")
    data = f.read()
    f.close()
    for k in data:
        if k not in dic.keys():
            dic[k] = 1
        else:
            dic[k] += 1
    for k, v in dic.items():
        print(f"{k} -> {v}")
except Exception as e:
    print(e)