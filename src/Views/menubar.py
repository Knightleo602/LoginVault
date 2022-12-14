from tkinter import *

from .options import showOptionsMenu
from .confirmWindow import showConfirmWindow
import webbrowser

def createMenuBar(parent):
    menubar = Menu(parent)
    """
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Export")#,command=)
    fileMenu.add_command(label="Import")#,command=)
    fileMenu.add_separator()
    fileMenu.add_command(label="Options", command=lambda: showOptionsMenu(parent)) # esse options vai ter opcoes pra: aparencia, lingua, creditos
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=lambda: showConfirmWindow(parent, "Tem certeza que ser sair?", exit)) # pra colocar um comando com argumento, usar lambda: 
    """
    
    helpMenu = Menu(menubar, tearoff=0)
    helpMenu.add_command(label="Github Page",command=lambda: openBrowser("https://github.com/Knightleo602/LoginVault"))
    
    #menubar.add_cascade(label="File", menu=fileMenu)
    menubar.add_cascade(label="Help", menu=helpMenu)
    
    parent.config(menu=menubar)
    
def openBrowser(link):
    webbrowser.open(link)