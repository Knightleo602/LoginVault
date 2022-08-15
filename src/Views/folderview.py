from tkinter import *
from tkinter import messagebox
from Controller.extraFunctions import checkString
import Controller.foldersController as fdr
import Controller.masterController as master
from .loginsView import updateLoginsView
from functools import partial

row = -1
resizeState = False
cursor = ''

def createFolderView(parent):
    global frame
    frame = PanedWindow(parent, sashwidth=4, sashrelief=SUNKEN, bg='#404040')

    buildFolderView()
    
    parent.add(frame, minsize=50, width=150)
    
def updateFolderView():
    global frame
    for i in frame.winfo_children():
        i.destroy()
    buildFolderView()
    
def buildFolderView():
    global frame
    labelMain = Label(frame, text=master.loggedMaster.name + "'s vault", fg='#212121')
    labelPastas = Label(frame, text="Pastas: ")
    
    newFolder = Button(frame, text="Nova Pasta", command=criarNovaPasta)
    
    labelMain.pack(anchor=NW, pady=(10, 30), padx=10)
    labelPastas.pack(anchor=NW, pady=(10, 20), padx=20)
    
    userFolders = Frame(frame, bg="#404040")

    for i in fdr.loadFolders():
        button = Button(userFolders, text=i.getName(), command=partial(setSelectedFolder, i.getId()), bg='#404040', borderwidth=0, activebackground='#666666', foreground='white')
        button.pack(pady=(0, 10))
        
    userFolders.pack()
    
    newFolder.pack(side=BOTTOM, pady=(50, 10))

def setSelectedFolder(folderId):
    fdr.selectedFolder = folderId
    updateLoginsView()
    
def rowCount(add = 1): # pra fazer certinho as linhas
    global row
    row += add
    return row

def criarNovaPasta():
    global frame, add
    add = Toplevel(frame)
    add.title("")
    
    name = Label(add, text="Name")
    name.pack()
    
    global entry
    entry = Entry(add)
    entry.pack()
    
    button = Button(add, text="Create", command=addCommand)
    button.pack()
    
    global errorLabel
    errorLabel = Label(add)
    errorLabel.pack()
    
    add.grab_set()
    add.attributes('-topmost', True)
    
    add.mainloop()

def addCommand():
    global entry, add
    name = entry.get()
    if checkString(name):
        if fdr.saveFolderToTable(name):
            add.destroy()
            updateFolderView()
        else:
            messagebox.showinfo("", "Numero Maximo de pastas atingido!", parent=frame)
    else:
        errorLabel.config(text="Invalid Name")
