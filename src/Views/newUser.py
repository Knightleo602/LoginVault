from tkinter import *
from Controller.masterController import saveMasterToTable
from Views.mainview import createMainView
from Controller.extraFunctions import checkString

passwdState = False

def createLoginView(parent):
    global frame
    frame = Frame(parent)
    
    labelMain = Label(frame, text="Welcome!", font=("", 15))
    labelMain.grid(row=0, column=0, columnspan=3, pady=17)
    
    labelMain = Label(frame, text="Create a new account to get started.", font=("", 15))
    labelMain.grid(row=1, column=0, columnspan=3, pady=17)
    
    global entryUsername
    labelUsername = Label(frame, text="Username:", font=("", 10))
    labelUsername.grid(row=2, column=0, pady=(10, 10), padx=(6, 0))
    entryUsername = Entry(frame)
    entryUsername.grid(row=2, column=1, sticky=EW, padx=(0, 9), pady=(10, 10))
    
    global entryPassword, hiddenPwdImage, visiblePwdImage, showPasswdButton
    hiddenPwdImage = PhotoImage(file="./img/hiddenPasswdSmall.png", width=15, height=15)
    visiblePwdImage = PhotoImage(file="./img/visiblePasswdSmall.png", width=15, height=15)
    labelPassword = Label(frame, text="Password:", font=("", 10))
    labelPassword.grid(row=3, column=0, pady=(0, 10), padx=(6, 0))
    bullet = "\u2022"
    entryPassword = Entry(frame, show=bullet)
    entryPassword.grid(row=3, column=1, sticky=EW, padx=(0, 9), pady=(0, 10))
    showPasswdButton = Button(frame, command=showPasswd, image=hiddenPwdImage)
    showPasswdButton.grid(row=3, column=1, pady=(0, 10), sticky=E, padx=(0, 9))

    add = Button(frame, text="Create", command=lambda: create(parent))
    add.grid(row=4, column=0, columnspan=3, pady=10, ipadx=25)
    
    global errorLabel
    errorLabel = Label(frame)
    errorLabel.grid(row=5, column=0, sticky=EW, columnspan=2)
    
    frame.pack()
    
def create(root):
    global errorLabel, frame
    username = entryUsername.get().strip()
    password = entryPassword.get()
    if checkString(username) and checkString(password):
        if saveMasterToTable(username, password):
            errorLabel.config(text="Usuario criado com sucesso!")
            frame.destroy()
            createMainView(root)
        else:
            errorLabel.config(text="Usuario ja existe!")
    else:
        errorLabel.config(text="Nome ou senha Invalido!")

def showPasswd():
    global passwdState, showPasswdButton, visiblePwdImage, hiddenPwdImage
    if passwdState:
        passwdState = False
        bullet = "\u2022"
        entryPassword.config(show=bullet)
        showPasswdButton.config(image=hiddenPwdImage)
    else:
        passwdState = True
        bullet = "\u2022"
        entryPassword.config(show="")
        showPasswdButton.config(image=visiblePwdImage)
    
    