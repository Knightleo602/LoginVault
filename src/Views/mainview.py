from tkinter import *
from .addWindow import showAddWindow

def createMainView(parent):
    frame = Frame(parent, bg='#1e8f77')
    
    frame.columnconfigure((2, 3, 4), weight=5, minsize=20) # o 6 e a quantidade de colunas
    frame.columnconfigure(1, weight=1, minsize=55)
    
    labelMain = Label(frame, text="Pasta", font=("", 15))    
    labelMain.grid(row=0, column=0, pady=(20, 18), padx=(5, 1), columnspan=3, sticky=W)
    
    adicionar = Button(frame, text="+", command=lambda: showAddWindow(frame))
    adicionar.grid(row=0, column=3, padx=(0, 20), columnspan=3, sticky=E)    
    
    labelUserN = Label(frame, text="UserName")
    labelPasswd = Label(frame, text="Senhas")
    
    # coluna 1 = usernamea
    # coluna 3 = senhas
    # todos os logins criados vao aparecer na quarta linha pra frente
    labelUserN.grid(row=2, column=1, padx=(20, 20), columnspan=2, sticky=EW)
    labelPasswd.grid(row=2, column=3, padx=(0, 20), columnspan=2, sticky=EW)
    
    # expandButton = Button(frame, text="\/", command=expandLogin)
    
    parent.add(frame, minsize=150)
    #frame.pack(side="left", fill="both", expand=True)
    
def getLogins(): # a ideia e ele pega e retorna os logins como um frame 
    ...

def expandLogin():
    ...
