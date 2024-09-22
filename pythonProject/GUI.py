from tkinter import *

root = Tk()

# Ajustar tamanho
root.geometry("200x200")

def registrar():
    label.config(text='Cliente "' + entradaNome.get() + '" registrado!')
    f = open("registros.txt", "a")
    f.write("\n" + entradaNome.get() + " " + selecaoDia.get() + " " + selecaoHorario.get() + " " + entradaDia.get() + " " + entradaMes.get() + " " + entradaAno.get())
    f.close()


# Menus dropdown
diasDaSemana = [
    "Segunda",
    "Terca",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sabado",
    "Domingo"
]

horarios = [
    "Manha",
    "Tarde",
    "Noite",
]

# tipo de dados dos menus dropdown
selecaoDia = StringVar()
selecaoHorario = StringVar()

# texto inicial
selecaoDia.set("Dia da Semana...")
selecaoHorario.set("Horario...")

# criar menu Dropdown
entradaNome = Entry(root)
entradaNome.insert(END, "Nome...")
entradaNome.pack()
entradaDiaDaSemana = OptionMenu(root, selecaoDia, *diasDaSemana)
entradaDiaDaSemana.pack()
entradaHorario = OptionMenu(root, selecaoHorario, *horarios)
entradaHorario.pack()
entradaDia = Entry(root)
entradaMes = Entry(root)
entradaAno = Entry(root)
entradaDia.insert(END, "Dia...")
entradaMes.insert(END, "Mes... (por extenso)")
entradaAno.insert(END, "Ano...")
entradaDia.pack()
entradaMes.pack()
entradaAno.pack()

button = Button(root, text="Registrar Cliente", command=registrar).pack()

label = Label(root, text=" ")
label.pack()

# Executar tkinter
root.mainloop()