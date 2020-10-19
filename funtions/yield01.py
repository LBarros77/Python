def fun(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

print(list(fun(5)))