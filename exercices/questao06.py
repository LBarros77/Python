def media(x, y, z = 2):
    return (float(x) + float(y) / z)

calender = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

# temperatura max e min
print("Digite o valor das temperaturas: de cada mê.")
month_half = [media(input(f"{i}º mês\nMínima: "), input("Máxima: ")) for i in range(1, 13)]
year_half = media(min(month_half), max(month_half))

print("=" * 50)
print("Média anual: ", year_half,"\n","=" * 50)
print("Valores a cima da média anual: ")
for n, i in enumerate(month_half, start=1):
    if i > year_half:
        print(f"A temperatura media de {calender[n]} é {i:.2f}")

print("=" * 50)