def show(title1, lst):
    print("+", "-" * 45, "+")
    print("|\t\t" + len(title1)*" " + "\t\t|")
    print(f"|\t\t {title1} \t\t|")
    print("|\t\t" + len(title1)*" " + "\t\t|")
    print("+", "-" * 45, "+")
    for n, i in enumerate(lst, start=1):
        print(f"| {n}- {i} ", (40 - len(i)) * " ","|")
    print("+", "-" * 45, "+")

def addTask():
    task[f"Tarefa {len(task) + 1}"] = input("Tarefa: ")

def mark(tasks):
    dic = {}
    try:
        task_number = "Tarefa " + input("Número de tarefa: ")
        for k, v  in tasks.items():
            if k == task_number:
                key = "*" + k
                dic[key] = v + "*"
            else:
                dic[k] = v
        return dic
    except Exception as e:
        print(e)

def remove(x):
    x = input(x)
    try:
        del task["Tarefa " + x]
    except KeyError:
        del task["*Tarefa " + x]
    else:
        print("Tarefa não encontrada.")
    finally:
        print("Tarefa eliminada!")

def taskList():
    #keys_orde = sorted(task.keys()[0:]
    for k, v in task.items():
        print(f"{k}: {v}")

task = {}
menu_list = ["Inserir tarefa", "Marcar tarefa como concluída", "Excluir tarefa", "Listar tarefa", "Sair"]

show("LISTA DE TAREFAS", menu_list)

while True:
    option = int(input("Digite sua opção: "))
    if option == 1:
        for i in range(4):
            addTask()
    elif option == 2:
        task = mark(task)
    elif option == 3:
        remove("Nº de tarefa: ")
    elif option == 4:
        taskList()
    else:
        break

#keys_orde = sorted(task.keys()
#dic = {"taref 1": "Escovar", "tarefa 3": "Comer", "tarefa 2": "Voar"}