import json
import requests

city = input("Digite sua localização: ")
my_key = "7ce79565160eb5e25c8c6194f99778d7"

try:
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={my_key}"
    requisition = requests.get(url)
    requisition.raise_for_status()
except EOFError as e:
    print("Requisição não encontrada. ", e)

#load archive text
dates = json.loads(requisition.text)

lst = dates["list"]

print(f"A temperatura média hoje de {city} é: ", end="")
tempCeusios = lst[0]["main"]["temp"] - 273.15
print(f"{tempCeusios:.2f}")