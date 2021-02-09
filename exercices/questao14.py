def splitChars(chars): 
    numeric = 0
    strings = {0:"", 1:"", 2:"", 3:""}
    for letter in chars:
        if letter.isupper():
            if letter not in strings[0]:
                strings[0] += letter
        elif letter.islower():
            if letter not in strings[1]:
                strings[1] += letter
        elif letter.isdigit():
            if letter not in strings[2]:
                numeric += int(letter)
                strings[2] = f"{numeric}"
        else:
            strings[3] += letter
    
    words = []
    for n in range(len(strings)):
        if strings[n] == "":
            del strings[n]
        else:
            words.append(strings[n])
    return tuple(words)

print(splitChars("ghSPdd2-56n!*mn7jd2"))