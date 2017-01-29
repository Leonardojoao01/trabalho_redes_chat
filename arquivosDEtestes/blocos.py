from tkinter import *

class Application:
    def __init__(self, master=None):

        self.juca = Label(master, width=30, text="").grid(row=0, sticky=W)
        self.afonso = Label(master, text="Second").grid(row=1, sticky=W)

        e1 = Entry(master)
        e2 = Entry(master)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        #self.mensagem =  Label(row=0, text="")
        #self.mensagem.pack()

        self.juca["text"] = "Autenticado"

root = Tk()
Application(root)
root.mainloop()
