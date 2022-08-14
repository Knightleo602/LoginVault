from tkinter import *
from .confirmWindow import showConfirmWindow

def createMenuBar(parent):
    menubar = Menu(parent)

    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Export")#,command=)
    fileMenu.add_command(label="Import")#,command=)
    fileMenu.add_separator()
    fileMenu.add_command(label="Options")#,command=) # esse options vai ter opcoes pra: aparencia, lingua, creditos
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=lambda: showConfirmWindow(parent, "Tem certeza que ser sair?", exit)) # pra colocar um comando com argumento, usar lambda: 
    
    helpMenu = Menu(menubar, tearoff=0)
    helpMenu.add_command(label="Reportar Problema")#,command=)
    helpMenu.add_command(label="Guia de usuario")#,command=)
    helpMenu.add_command(label="Pagina do Github")#,command=)
    
    menubar.add_cascade(label="File", menu=fileMenu)
    menubar.add_cascade(label="Help", menu=helpMenu)
    
    parent.config(menu=menubar)