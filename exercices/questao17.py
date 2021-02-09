def digitosExtremos(digitos):
    ind = 1
    last = []
    while True:
        if ind == 1:
            first = digitos // 1 % 10
            ind *= 10
        else:
            try:
                last.append(digitos // ind % 10)
            except:
                break
        ind *= 10
    return (first, last[-1])

print(digitosExtremos(123455))