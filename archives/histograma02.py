'''
Pasos:
Pida al usuario el nombre del archivo de entrada.
Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y minúsculas se tratan como iguales).
Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos distintos de cero).
En el final imprimir los valores de furma decresciente.
Questión:
Crea un archivo de prueba para tu código y verifica si tu histograma contiene resultados válidos.
'''
from sys import path

fl = path[0] + "/" + input("Nombre del archivo: ")

try:
    with open(fl, "w") as f:
        f.write("aBcacc")
except Exception as e:
    print(e)
    
dic = {}

try:
    with open(fl, "r") as f:
        data = f.read()
    for k in data:
        if k not in dic.keys():
            dic[k] = 1
        else:
            dic[k] += 1
    for k, v in sorted(dic.items(), key=lambda items: items[1], reverse=True):
        print(f"{k} -> {v}")
except Exception as e:
    print(e)