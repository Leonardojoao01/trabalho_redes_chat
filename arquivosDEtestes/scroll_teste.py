from tkinter import *

master = Tk()

scrollbar = Scrollbar(master)
#scrollbar.pack(side=RIGHT, fill=Y)         # Mostra a barra de rolagem

#-------------------------------------------------------------------------------

primeiroContainer = Frame(master)
primeiroContainer["pady"] = 10
primeiroContainer["padx"] = 150
primeiroContainer.pack()

segContainer = Frame(master)
segContainer["pady"] = 15
segContainer.pack()

segundoContainer = Frame(master)
segundoContainer["pady"] = 20
segundoContainer.pack()



subject_label = Label(segundoContainer, text="Conversa", width=90)
subject_label.pack(padx=0, side=LEFT)

#-------------------------------------------------------------------------------

listbox = Listbox(segundoContainer, yscrollcommand=scrollbar.set, width=50)
for i in range(1000):
    listbox.insert(0, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

for i in range(2000):
    listbox.insert(0, str(i))

mainloop()
