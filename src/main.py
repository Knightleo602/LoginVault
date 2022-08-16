from tkinter import *
from Controller.database import *
from Views.confirmWindow import showConfirmWindow
from Views.masterLogin import masterLoginView
from Views.newUser import createLoginView
import pathlib
import Models.globals as globals

def exit():
    global root
    root.destroy()

root = Tk()
root.title("Login Vault")
root.minsize(width=150, height=150)
root.geometry("500x500")
globals.currentpath = str(pathlib.Path(__file__).parent.parent.resolve())
root.iconphoto(False, PhotoImage(file=globals.currentpath+"/img/vaulticon.png"))
dblocation = globals.currentpath + "/src/Models/.database.db"

root.config()

if connectDatabase(dblocation):
    masterLoginView(root)
else:
    createLoginView(root)

root.protocol('WM_DELETE_WINDOW', lambda: showConfirmWindow(root, "Are you sure you want \nto close this page?", exit))

root.mainloop()