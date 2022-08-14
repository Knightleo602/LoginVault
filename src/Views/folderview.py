from tkinter import *
from turtle import width

row = -1
resizeState = False
cursor = ''

def createFolderView(parent):
    global frame
    frame = PanedWindow(parent, sashwidth=4, sashrelief=SUNKEN, bg='#404040')
    labelMain = Label(frame, text="Vault", fg='#212121')
    labelPastas = Label(frame, text="Pastas: ")
    
    # aqui vai ser dai pra mostrar todas as pastas criadas
    # A unica pasta que vai ter de inicio e o Created
    
    newFolder = Button(frame, text="Nova Pasta", command=criarNovaPasta)
    
    labelMain.pack(anchor=NW, pady=(10, 30), padx=10)
    labelPastas.pack(anchor=NW, pady=(10, 15), padx=20)
    newFolder.pack(side=BOTTOM, pady=(50, 10))

    parent.add(frame, minsize=50, width=150)
    #frame.pack(side="left", fill="y", ipadx=20)
    
def rowCount(add = 1): # pra fazer certinho as linhas
    global row
    row += add
    return row

def criarNovaPasta():
    ...
            
