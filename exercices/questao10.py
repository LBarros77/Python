def menorVolta(dictionary):
    for k, v in dictionary.items():
        if v == min(dictionary.values()):
            return f"{k} com {v}"

def ordemChegada(dictionary):
    dictionary = sorted(dictionary.items(), key = lambda value: value[1])
    return dict(dictionary)

hall = []
three_laps = []
single_return = 0
smaller = {}
averages_corridors = {}

for h in range(6):
    hall.append(input(f"Digite o nome do {h+1}ª corredor: "))
    three_laps.clear() 
    for t in range(3):
        n2 = int(input(f"Digite a {t+1}ª volta: "))
        three_laps.append(float(n2) / 100)
        if n2 <= min(three_laps):
            single_return = t

    smaller[hall[h]] = min(three_laps)#menores voltas
    averages_corridors[hall[h]] = sum(three_laps) / len(three_laps)#média dos corredores

ranking = ordemChegada(averages_corridors)
print("\nNa {}ª houve a menor volta de {}".format(single_return + 1, menorVolta(smaller)))
print("\nClassificação")
for k, v in ranking.items():
    print(f"{k}: {v:.3f}")
