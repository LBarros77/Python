import json
from sys import path


with open(f"{path[0]}/aluno-nota.json") as f:
    dates = json.load(f)

aprovate = {}
reprovate = {}

for n, i in enumerate(dates):
    if ((dates[n]["nota1"] + dates[n]["nota2"]) / 2) >= 7:
        aprovate[dates[n]["aluno"]] = (dates[n]["nota1"] + dates[n]["nota2"])/2
    else:
        reprovate[dates[n]["aluno"]] = (dates[n]["nota1"] + dates[n]["nota2"])/2

try:
    print("Aprovados!")
    for k, v in aprovate.items():
        print(f"{k} tem média {v}")
except:
    print("Ninguém foi aprovado.")

print()
try:
    print("Reprovados!")
    for k, v in reprovate.items():
        print(f"{k} tem média {v}")
except:
    print("Ninguém foi reprovado.")