from tkinter import *

class Kanvas:
    def __init__(self,root):

        # self.canvas1 = Canvas(raiz, width=200, height=200, cursor='X_cursor', bd=5, bg='dodgerblue')
        # self.canvas1.pack(side=LEFT)
        #
        # self.canvas2 = Canvas(raiz, width=200, height=200, cursor='dot', bd=5, bg='purple')
        # self.canvas2.pack(side=LEFT)
        # #self.canvas2["text"] = "Autenticado"
        w = Label(root, text="red", bg="red", fg="white")
        w.pack(padx=5, pady=10, side=LEFT)
        w = Label(root, text="green", bg="green", fg="black")
        w.pack(padx=5, pady=20, side=LEFT)
        w = Label(root, text="blue", bg="blue", fg="white")
        w.pack(padx=5, pady=20, side=LEFT)

        self.juca = Label(root, text="", bg="blue", fg="white", width=50)
        self.juca.pack(padx=5, pady=30, side=LEFT)

        self.juca['text'] = "Aleluia, consegui fazer o quero!!!!\n juca"

instancia=Tk()
Kanvas(instancia)
instancia.mainloop()
