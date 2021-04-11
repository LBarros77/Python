import matplotlib.pyplot
import json
import requests
from sys import path

#def allCasesBr():

class Database:
    def __init__(self, my_datas, date_choice, region_choice=None):
        self.my_datas = my_datas
        self.date_choice = date_choice
        self.region_choice = region_choice
        self.months = [my_datas[i]["lastUpdatedAtSource"].split("T")[0] for i in range(4)]
        self.infecteds = [int(my_datas[i]["infected"]) for i in range(4)]
    
    #@classmethod
    def showCases(self):
        matplotlib.pyplot.plot(self.months, self.infecteds)
        matplotlib.pyplot.show()
    
    def dateChoice(self):
        months = self.months
        index_date = months.index(self.date_choice)
        return index_date

    def infectedByRegion(self):
        my_datas = self.my_datas
        by_region = [i["infectedByRegion"] for i in my_datas]
        #index_region = by_region.index("state":self.region_choice)
        #get cases infectedByRegion

#==============================================================


url = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
response = requests.request("GET", url)
data = json.load(response.text)


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)