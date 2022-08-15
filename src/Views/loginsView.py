from tkinter import *

from Controller.loginsController import loadLogins, saveLoginToTable
import Controller.foldersController as fdr
from functools import partial

def createLoginsView(parent):
    global frame
    frame = Frame(parent, bg='#666666')
    
    buildLoginsView()
    
    parent.add(frame, minsize=150)

def updateLoginsView():
    global frame
    for i in frame.winfo_children():
        i.destroy()
    buildLoginsView()

def buildLoginsView():
    global frame
    frame.columnconfigure((2, 3, 4), weight=5, minsize=20)
    frame.columnconfigure(1, weight=1, minsize=55)
    
    labelMain = Label(frame, text=fdr.getSelectedFolder().getName(), font=("", 15), highlightthickness=1, highlightbackground='black')    
    labelMain.grid(row=0, column=0, pady=(20, 18), padx=(5, 1), columnspan=3, sticky=EW)
    
    adicionar = Button(frame, text="+", command=lambda: showAddWindow(frame), highlightthickness=1, highlightbackground='black')
    adicionar.grid(row=0, column=3, padx=(0, 20), columnspan=3, sticky=E)    
    
    labelUserN = Label(frame, text="UserNames", highlightthickness=1, highlightbackground='black')
    labelPasswd = Label(frame, text="Passwords", highlightthickness=1, highlightbackground='black')
    
    labelUserN.grid(row=2, column=1, padx=(20, 20), pady=(0, 10), columnspan=2, sticky=EW)
    labelPasswd.grid(row=2, column=3, padx=(0, 20), pady=(0, 10), columnspan=2, sticky=EW)
    
    rowCount = 3
    for i in loadLogins():
        name = Label(frame, text=i.getUserName(), highlightthickness=2, highlightbackground='black', bg="#ADADAD", foreground='black')
        name.grid(row=rowCount, column=1, padx=(20, 20), pady=(10, 0), columnspan=2, sticky=EW)
        
        name.bind("<Button-1>", partial(copyToClipboard, i.getUserName(), name))
        name.bind("<Enter>", partial(changeNameBg, name, True))
        name.bind("<Leave>", partial(changeNameBg, name, False))
        
        
        passLabel = Label(frame, text=i.getPassword(), bg='#212121', foreground='#212121', highlightthickness=3, highlightbackground='black')
        passLabel.grid(row=rowCount, column=3, padx=(0, 20), pady=(10, 0), columnspan=2, sticky=EW)
        
        passLabel.bind("<Button-1>", partial(copyToClipboard, i.getPassword(), passLabel))
        passLabel.bind("<Enter>", partial(changePasswordBg, passLabel, True))
        passLabel.bind("<Leave>", partial(changePasswordBg, passLabel, False))
        rowCount += 1
    
    global message
    message = Label(frame, bg="#666666", fg="white")
    message.grid(row=rowCount, column=1, columnspan=4, pady=(100, 0), sticky=S)
        
def copyToClipboard(text, label, event):
    frame.clipboard_clear()
    frame.clipboard_append(text)
    fg = label["foreground"]
    bg = label["bg"]
    message.config(text="Copied to Clipboard", bg="#59B663")
    label.config(bg='#BFBFBF', foreground='black')
    frame.after(100, lambda: label.config(bg=bg, foreground=fg))
    frame.after(5000, lambda: message.config(text="", bg="#666666"))
    
def changeNameBg(label, state, event):
    if state:
        label.config(bg="white", foreground='#212121', highlightthickness=3)
    else:
        label.config(bg='#ADADAD', foreground='black', highlightthickness=2)
def changePasswordBg(label, state, event):
    if state:
        label.config(bg="#666666", foreground='white')
    else:
        label.config(bg='#212121', foreground='#212121')

passwdState = False

def showAddWindow(parent):
    rowAmount = 7
    global add, entryUsername, entryPassword, entryWebsite, clickedFolder, entryNotes, hiddenPwdImage, visiblePwdImage, showPasswdButton
    add = Toplevel(parent)
    add.title("")
    add.columnconfigure((0, 1), weight=1)
    add.resizable(0,0)
    
    labelMain = Label(add, text="Add new login information", font=("", 15))
    labelMain.grid(row=0, column=0, columnspan=3, pady=17)
    
    labelUsername = Label(add, text="Username:", font=("", 10))
    labelUsername.grid(row=1, column=0, pady=(0, 10), padx=(6, 0))
    entryUsername = Entry(add)
    entryUsername.grid(row=1, column=1, sticky=EW, padx=(0, 9), pady=(0, 10))
    
    hiddenPwdImage = PhotoImage(file="./img/hiddenPasswdSmall.png", width=15, height=15)
    visiblePwdImage = PhotoImage(file="./img/visiblePasswdSmall.png", width=15, height=15)
    labelPassword = Label(add, text="Password:", font=("", 10))
    labelPassword.grid(row=2, column=0, pady=(0, 10), padx=(6, 0))
    bullet = "\u2022"
    entryPassword = Entry(add, show=bullet)
    entryPassword.grid(row=2, column=1, sticky=EW, padx=(0, 9), pady=(0, 10))
    showPasswdButton = Button(add, command=showPasswd, image=hiddenPwdImage)
    showPasswdButton.grid(row=2, column=1, pady=(0, 10), sticky=E, padx=(0, 9))

    labelWebsite = Label(add, text="Website:", font=("", 10))
    labelWebsite.grid(row=3, column=0, pady=(0, 10), padx=(6, 0))
    entryWebsite = Entry(add)
    entryWebsite.grid(row=3, column=1, sticky=EW, padx=(0, 9), pady=(0, 10))
    
    availableFolders = []
    selectedFolderIndex = 0
    cont = 0
    for i in fdr.folders:
        availableFolders.append((i.getName()))
        if i.getName() == fdr.getSelectedFolder().getName():
            selectedFolderIndex = cont
        cont += 1
    clickedFolder = StringVar(add)
    clickedFolder.set(availableFolders[selectedFolderIndex])
    
    labelFolder = Label(add, text="Folder:", font=("", 10))
    labelFolder.grid(row=4, column=0, pady=(0, 10), padx=(6, 0))
    entryFolder = OptionMenu(add, clickedFolder, *availableFolders)
    entryFolder.grid(row=4, column=1, sticky=EW, padx=(0, 9), pady=(0, 10))
    
    labelNotes = Label(add, text="Notes:", font=("", 10))
    labelNotes.grid(row=5, column=0, sticky=N, pady=(0, 10), padx=(6, 0))
    entryNotes = Text(add, height=5, width=40)
    entryNotes.grid(row=5, column=1, sticky=EW, padx=(0, 9))
    
    buttonsFrame = Frame(add)
    
    addButton = Button(buttonsFrame, text="Add", command=create)
    cancelButton = Button(buttonsFrame, text="Cancel", command=cancel)
    addButton.pack(side=RIGHT, padx=(0, 50))
    cancelButton.pack(side=LEFT, padx=(50, 0))
    buttonsFrame.grid(row=rowAmount, column=0, sticky=EW, columnspan=3, pady=10)
    
    add.grab_set()
    add.attributes('-topmost', True)
    
    add.mainloop()

def create():
    global entryUsername, entryPassword, entryWebsite, clickedFolder, entryNotes
    username = entryUsername.get().strip()
    password = entryPassword.get()
    website = entryWebsite.get().strip()
    folderId = fdr.getFolderId(clickedFolder.get())
    notes = entryNotes.get("1.0",'end-1c')
    saveLoginToTable(username, password, website, notes, folderId)
    updateLoginsView()
        
def cancel():
    global add
    add.destroy()
    
def showPasswd():
    global passwdState, showPasswdButton, visiblePwdImage, hiddenPwdImage
    if passwdState:
        passwdState = False
        bullet = "\u2022"
        entryPassword.config(show=bullet)
        showPasswdButton.config(image=visiblePwdImage)
    else:
        passwdState = True        
        entryPassword.config(show="")
        showPasswdButton.config(image=hiddenPwdImage)
    

