from tkinter import *

from .loginsView import createLoginsView

from .menubar import createMenuBar

from .folderview import createFolderView

def createMainView(parent):
    
    paned = PanedWindow(parent, sashwidth=3, bg="#5D5D5D")
    paned.pack(fill=BOTH, expand=True)
    
    createMenuBar(parent)
    createFolderView(paned)
    createLoginsView(paned)
    
    #frame.pack(side="left", fill="both", expand=True)
    return paned
    
def getLogins(): # a ideia e ele pega e retorna os logins como um frame 
    ...

def expandLogin():
    ...
