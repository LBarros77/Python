aluno = []
dic = {}
i = 0
print("Para parar de inserir click enter em vez de digitar o nome.")
while True:
    aluno.append(input(f"Digite o nome do {i+1}ª aluno: "))
    if aluno[i] == " " or aluno[i] == "":
            break
    nota = 0
    for e in range(2):
        nota += float(input(f"Digite a {e+1}ª nota do aluno: "))
    dic[aluno[i]] = nota / 2
    i += 1

for k, v in dic.items():
    print(f"{k} tem média {v:.2f}")
