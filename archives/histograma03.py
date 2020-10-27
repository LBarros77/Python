from os import strerror

caracters = 0
dic = {"a":0, "B":0, "c":0}
try:
    ar = input("Archive Name: ")
    with open(ar, "r") as fl:
        fil = fl.read(20)
    for c in fil:
        if c in dic.keys():
            dic[c] += 1
        caracters += 1
except IOError as e:
    print("E/S error: ", strerror(e.errno))

for k, v in sorted(dic.items(), key=lambda items: items[1], reverse=True):
    print(k, "-->", v)
print("\nCaracters total: ", caracters)