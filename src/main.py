from tkinter import *
from Views.folderview import createFolderView
from Views.menubar import createMenuBar
from Views.mainview import createMainView
from Views.confirmWindow import showConfirmWindow
from os import path

def exit():
    global root
    root.destroy()

root = Tk()
root.title("Login Vault")
root.minsize(width=150, height=150)
root.geometry("500x500")

if not path.isfile("Models/settings.json"):
    ...

paned = PanedWindow(root, sashwidth=3, bg="#5D5D5D")

paned.pack(fill=BOTH, expand=True)

createFolderView(paned)
createMainView(paned)
createMenuBar(root)

root.protocol('WM_DELETE_WINDOW', lambda: showConfirmWindow(root, "Tem certeza que ser sair?", exit))

root.mainloop()