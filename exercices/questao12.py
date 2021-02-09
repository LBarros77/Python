def primo(number):
    from random import randint, choice
    string = ""
    tot = choice([False, True, False])
    if tot:
        return '"' + str(number) + '"'

    for n in range(randint(0, number)):
        if n % 2 == 1:
            string = str(n) if len(string) == 0 else string + f" {n}"
    return '"' + string + '"'


print(primo(10))