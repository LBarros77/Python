with open("text.txt", "r") as f:
    dates = f.read()


with open("text2.txt", "w") as f:
    f.write(dates.lower())