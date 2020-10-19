lst2 = list(map(lambda x: 2 ** x, range(5)))

print(lst2)

for i in list(map(lambda x: x ** 2, lst2)):
    print(i, end=" ")
print()

print(list(map(lambda x: 1 if x % 2 == 0 else 0, lst2)))
