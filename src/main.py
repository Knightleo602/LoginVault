from glob import glob
from tkinter import *
from Views.folderview import createFolderView
from Views.menubar import createMenuBar
from Views.mainview import createMainView

def exit():
    global root
    root.destroy

root = Tk()
root.title("Login Vault")
root.minsize(width=150, height=150)
root.geometry("500x500")
paned = PanedWindow(root, sashwidth=3, bg="#5D5D5D", handlepad=100)

paned.pack(fill=BOTH, expand=True)

createFolderView(paned)
createMainView(paned)
createMenuBar(root)

root.mainloop()