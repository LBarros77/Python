from datetime import datetime
from beepy import beep
from time import sleep

seletioned_hour = input("Horário de alarme: ")

for i in range(5):
    time_now = f"{datetime.now().time()}".split(":")[:-1]
    time_now = f"{time_now[0]}:{time_now[1]}"
    if seletioned_hour == time_now:
        beep(sound=6)
        sleep(1)