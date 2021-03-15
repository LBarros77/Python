import json
from tkinter import *
from tkinter.messagebox import showerror

def showList(w):
    vname.delete(0, END)
    w.delete(0, END)
    with open("names.json", "r") as fl:
        name_dic = json.load(fl)
        for name in name_dic["names"]:
            w.insert(END, name)
    return w


def includeName():
    if vname.get() == "":
        showerror(title="error", message="Digite um nome válido")

    with open("names.json") as fl:
        name_dict = json.load(fl)

    with open("names.json", "w") as fl:
        name_dict["names"].append(vname.get())
        json.dump(name_dict, fl)
    
    showList(show)


def nameRequest():
    if vname.get() == "":
        showerror(title="error", message="Digite um nome válido")

    with open("names.json", "r") as fl:
        names = json.load(fl)
        if vname.get() in names["names"]:
            show.delete(0, END)
            show.insert(END, vname.get())
        return False


def deleteName():
    if vname.get() == "":
        showerror(title="error", message="Digite um nome válido")

    with open("names.json", "r") as fl:
        name_list = json.load(fl)
    
    if vname.get() in name_list["names"]:
        name_list["names"].remove(vname.get())
        with open("names.json", "w") as fl:
            json.dump(name_list, fl)
    
    showList(show)
        
'''
Criação de arquivo:
fl = open("names.json", "w")
json.dump({"names": ["José", "Richard"]}, fl)
fl.close()
'''

app = Tk()
app.title("Lista de nomes")
app.geometry("400x300")
app.configure(background="#dde")

Label(app, text="Nome", background="#dde", foreground="#000", anchor=W).place(x=10, y=10, width=100, height=20)

vname = Entry(app)
vname.place(x=10, y=30, width=150, height=20)

Button(app, text="Incluir", command=includeName).place(x=10, y=80, width=80, height=20)
Button(app, text="Pesquisar", command=nameRequest,).place(x=10, y=110, width=80, height=20)
Button(app, text="Deletar", command=deleteName).place(x=10, y=140, width=80, height=20)

show = Listbox(app)
showList(show)
show.pack(padx=10, pady=15)

app.mainloop()