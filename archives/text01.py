from os import strerror
from sys import path

with open(f"{path[0]}/text.txt", "w") as file:
    file.write("""
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.""")

for line in open(f"{path[0]}/text.txt"):
    print(line, end="")
print()