from tkinter import *
from Controller.masterController import masterLogin
from Views.mainview import createMainView
from Controller.extraFunctions import checkString
from Views.newUser import createLoginView

passwdState = False

def masterLoginView(parent):
    global frame
    frame = Frame(parent)
    
    labelMain = Label(frame, text="Welcome!", font=("", 15))
    labelMain.grid(row=0, column=0, columnspan=3, pady=17)
    
    labelMain = Label(frame, text="Please login to your account", font=("", 15))
    labelMain.grid(row=1, column=0, columnspan=3, pady=17)
    
    global entryUsername
    labelUsername = Label(frame, text="Username:", font=("", 10))
    labelUsername.grid(row=2, column=0, pady=(0, 10), padx=(6, 0))
    entryUsername = Entry(frame)
    entryUsername.grid(row=2, column=1, sticky=EW, padx=(0, 9), pady=(0, 10))
    
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

    loginButton = Button(frame, text="Login", command=lambda: login(parent))
    loginButton.grid(row=4, column=0, sticky=EW, columnspan=2, pady=(10, 5))
    
    createNewButton = Button(frame, text="Create new Account", command=lambda: moveToCreateAccount(parent))
    createNewButton.grid(row=5, column=0, columnspan=2, pady=15)
    
    global errorLabel
    errorLabel = Label(frame)
    errorLabel.grid(row=6, column=0, sticky=EW, columnspan=2)
    
    frame.pack()

def moveToCreateAccount(parent):
    frame.destroy()
    createLoginView(parent)

def login(root):
    global errorLabel, frame
    username = entryUsername.get()
    password = entryPassword.get()
    if checkString(username) and checkString(password):
        if masterLogin(username, password):
            frame.destroy()
            createMainView(root)
        else:
            errorLabel.config(text="Usuario ou senha incorretos!")
            entryUsername.config(textvariable="")
    else:
        errorLabel.config(text="Uso de characteres não permitidos!")
    
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