import matplotlib.pyplot as plt
import json
import requests
from sys import path

def showGraphic(infected, deceased=None, state=None):
    if state:
        plt.plot(date, infected)
        plt.title(f"Dados da COVID-19 em {state}")
    else:
        plt.plot(date, infected, deceased)
        plt.title("Dados da COVID-19 no Brasil")
        plt.xlabel("Day")
        plt.ylabel("Infected and deceased")
    plt.show()


def infectedByRegion(data):
    byRegion = list()
    for i in range(5):
        byRegion.append(data[i]["infectedByRegion"])

    #state = input("Sigla do stado? ").upper()
    #counts = list()
    lst = [l for l in [byRegion[i] for i in range(5)]]
    print(lst)

    #showGraphic(counts, None, state)


def allCasesBr():
    url = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"

    response = requests.request("GET", url)
    data = json.loads(response.text)

    global date
    date = list()
    infected = list()
    deceased = list()

    for i in range(5):
        date.append(data[i]["lastUpdatedAtSource"].split("T")[0])
        infected.append(int(data[i]["infected"]))
        deceased.append(int(data[i]["deceased"]))

    showGraphic(infected, deceased)

    answer = input("Ver por estado [S/N]: ").upper()[0]
    if answer == "S":
        infectedByRegion(data)


#allCasesBr()

data = open(path[0] + "/covidData.json")
data = json.load(data)
infectedByRegion(data)
'''
if ind["state"] == state:
            counts.append(int(ind["count"]))'''