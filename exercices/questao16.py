def inverterOrdem(phrasex):
    word_lst = []
    string = ""
    phrasex += " "

    for letter in phrasex:
        if letter == " ":
            word_lst.insert(0, string)
            string = ""
        else:
            string += letter
    
    new_phrase = ""
    for word in word_lst:
        new_phrase += word + " "
    
    return new_phrase[:-1] 


print(inverterOrdem("Romeu e Julieta"))