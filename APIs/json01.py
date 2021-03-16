import json
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

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

    else:
        with open("names.json") as fl:
            name_dict = json.load(fl)

        with open("names.json", "w") as fl:
            name_dict["names"].append(vname.get())
            json.dump(name_dict, fl)
    
    showList(show)


def nameRequest():
    if vname.get() != "":
        with open("names.json", "r") as fl:
            names = json.load(fl)
        
        if vname.get() in names["names"]:
            show.delete(0, END)
            show.insert(END, vname.get())
        else:
            showwarning(title="Pesquisa", message=f"{vname.get()} não foi encontrado")
    else:
        showerror(title="error", message="Digite um nome válido")


def deleteName():
    if vname.get() == "":
        showerror(title="error", message="Digite um nome válido")

    with open("names.json", "r") as fl:
        name_list = json.load(fl)
    
    if vname.get() in name_list["names"]:
        name_list["names"].remove(vname.get())
        with open("names.json", "w") as fl:
            json.dump(name_list, fl)
    else:
        showinfo(title="Informação", message="Para que um nome seja deletado ele precisa estar na lista")
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

Label(app, text="Nome", background="#dde", foreground="#000", anchor=W).grid(column=1, row=1, sticky="w", padx=(10, 0), pady=(15, 0))

Label(app, text="Lista de nomes", background="#dde", foreground="#000", anchor=W).grid(column=2, row=1, padx=50, pady=(15, 0))

vname = Entry(app)
vname.grid(column=1, row=2, padx=(10, 0), pady=(5, 3))

Button(app, text="Incluir", command=includeName).place(x=10, y=80, width=80, height=20)
Button(app, text="Pesquisar", command=nameRequest,).place(x=10, y=110, width=80, height=20)
Button(app, text="Deletar", command=deleteName).place(x=10, y=140, width=80, height=20)

show = Listbox(app)
showList(show)
show.place(x=200, y=40, width=150, height=150)

app.mainloop()