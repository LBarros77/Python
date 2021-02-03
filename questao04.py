calender = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junior",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

date = input("Data de nascimento [DD de MM de AAAA]: ").split()
date[2] = date[2].capitalize()
for k, v in calender.items():
    if date[2] == v:
        print(f"Você nasceu em {date[0]}/{k}/{date[-1]}")