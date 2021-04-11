import json
from sys import path

def somenteAprovados(dates):
    aprovates = {}
    for n, i in enumerate(dates):
        if ((dates[n]["nota1"] + dates[n]["nota2"]) / 2) >= 7:
            aprovates[dates[n]["aluno"]] = (dates[n]["nota1"] + dates[n]["nota2"])/2
    
    return aprovates


students_dates = open(path[0] + "/aluno-nota.json")

extraction = somenteAprovados(json.load(students_dates))

for k, v in extraction.items():
        print(f"{k} tem média {v}")