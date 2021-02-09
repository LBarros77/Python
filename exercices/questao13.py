def reverteRetira(lst, repeat):
    if repeat in lst:
        lst.remove(repeat)

    lst2 = []
    n = len(lst)#Pode-se fazer um contador com for no lugar de len!
    while n > 0:
        n -= 1
        lst2.append(lst[n].swapcase())
    
    return lst2


print(reverteRetira(["oi", "pEdRo", "cAMa"], "oi"))