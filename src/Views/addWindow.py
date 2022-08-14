from tkinter import *

passwdState = False

def showAddWindow(parent):
    rowAmount = 7
    global add
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
    
    global entryPassword, hiddenPwdImage, visiblePwdImage, showPasswdButton
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
    
    availableFolders = ["No Folder"]
    clicked = StringVar(add)
    clicked.set(availableFolders[0])
    
    labelFolder = Label(add, text="Folder:", font=("", 10))
    labelFolder.grid(row=4, column=0, pady=(0, 10), padx=(6, 0))
    entryFolder = OptionMenu(add, clicked, availableFolders)
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
    ...

def cancel():
    global add
    add.destroy()
    
def showPasswd():
    global passwdState, showPasswdButton, visiblePwdImage, hiddenPwdImage
    if passwdState:
        passwdState = False
        entryPassword.config(show="")
        showPasswdButton.config(image=hiddenPwdImage)
    else:
        passwdState = True
        bullet = "\u2022"
        entryPassword.config(show=bullet)
        showPasswdButton.config(image=visiblePwdImage)
    