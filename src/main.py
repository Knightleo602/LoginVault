from tkinter import *
from Controller.database import *
from Views.confirmWindow import showConfirmWindow
from Views.masterLogin import masterLoginView
from Views.newUser import createLoginView

def exit():
    global root
    closeDatabase()
    root.destroy()

root = Tk()
root.title("Login Vault")
root.minsize(width=150, height=150)
root.geometry("500x500")

dblocation = "./src/Models/database.db"

if connectDatabase(dblocation):
    masterLoginView(root)
else:
    createLoginView(root)

root.protocol('WM_DELETE_WINDOW', lambda: showConfirmWindow(root, "Tem certeza que ser sair?", exit))

root.mainloop()