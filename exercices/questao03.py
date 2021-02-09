matrix = [[int(input(f"Número de [{n}x{num}]: ")) for num in range(3)] for n in range(3)]
ind = len(matrix)
for line in matrix:
    ind -= 1
    for n, col in enumerate(line):
        if n >= ind:
            print(col, end=" ")
        else:
            print(" ", end=" ")
    print("")
