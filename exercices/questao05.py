from random import shuffle, randint

compare = ["França", "Inglaterra", "Brasil", "China", "Irlanda", "Espanha"]
compare = compare[randint(0, len(compare))]
word = list(compare)
shuffle(word)
print("Frase: ", "".join(word))

n = 0
while n < 3:
    answer = input("Digite a frase organizada: ")
    if answer == compare:
        print("Parabéns você acertou!")
        break
    n += 1