from random import randint, seed

seed()
date = [randint(-10, 10) for i in range(5)]
print(date)
print(list(filter(lambda x: x > 0 and x % 2 == 0, date)))