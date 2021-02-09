def montar(char, string):
    num = len(string)
    for letter in string:
        if letter in char:
            char.remove(letter)
            num -= 1
            if num == 0:
                return True
    return False

print(montar(["l", "e", "o", "n", "a", "r", "d", "o", "i", "n", "v", "e", "s", "t", "e"], "vestir"))