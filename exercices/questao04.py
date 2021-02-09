calender = {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro",
}

date = input("Data de nascimento [DD de MM de AAAA]: ").split()
date[2] = date[2].capitalize()
for k, v in calender.items():
    if date[2] == v:
        print(f"Você nasceu em {date[0]}/{k}/{date[-1]}")