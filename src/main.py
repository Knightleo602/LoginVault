from tkinter import *
from Controller.database import *
from Views.confirmWindow import showConfirmWindow
from Views.masterLogin import masterLoginView
from Views.newUser import createLoginView

def exit():
    global root
    root.destroy()

root = Tk()
root.title("Login Vault")
root.minsize(width=150, height=150)
root.geometry("500x500")

root.iconphoto(False, PhotoImage(file="./img/vaulticon.png"))

dblocation = "./src/Models/.database.db"

root.config()

if connectDatabase(dblocation):
    masterLoginView(root)
else:
    createLoginView(root)

root.protocol('WM_DELETE_WINDOW', lambda: showConfirmWindow(root, "Are you sure you want \nto close this page?", exit))

root.mainloop()