from os import strerror

date = bytearray(10)
for i in range(len(date)):
    date[i] = 10 - i

try:
    with open("file.bin", "wb") as fl:
        fl.write(date)
except IOError as e:
    print("Have a error of E/S; ", strerror(e.errno))

try:
    with open("file.bin", "rb") as fl:
        date = bytearray(fl.read(20))
    for b in date:
        print(hex(b), end=" ")
    print()
except IOError as e:
    print("Error of E/S: ", strerror(e.errno))