def crearCierre(par):
    loc = par
    def potencia(p):
        return p ** loc
    return potencia

fsqr = crearCierre(2)
fcub = crearCierre(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))