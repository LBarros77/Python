uniao = lambda a, b: a + b
def intersecao(a, b):
    x = []
    for latter in a:
        if latter in b:
            x.append(latter)
    return ", ".join(x)

def diferenca(a, b):
    lst = [letter for letter in a if letter not in b]
    for letter in b:
        if letter not in a:
            lst.append(letter)

    return ", ".join(lst)
    

a = ["a", "m", "e", "r", "i", "c", "a"]
b = ["a", "t", "a", "q", "u", "e"]
print("União: ", ", ".join(uniao(a, b)))
print("Interseção: ", intersecao(a, b))
print("Difeerença: ", diferenca(a, b))
