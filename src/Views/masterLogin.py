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
    labelMain.pack(pady=20)
    
    labelMain = Label(frame, text="Please login to your account", font=("", 15))
    labelMain.pack(pady=(20, 25))
    
    global entryUsername
    labelUsername = Label(frame, text="Username:", font=("", 10))
    labelUsername.pack()
    entryUsername = Entry(frame)
    entryUsername.pack(pady=(0, 4))
    
    global entryPassword, hiddenPwdImage, visiblePwdImage, showPasswdButton
    hiddenPwdImage = PhotoImage(file="./img/hiddenPasswdSmall.png", width=15, height=15)
    visiblePwdImage = PhotoImage(file="./img/visiblePasswdSmall.png", width=15, height=15)
    labelPassword = Label(frame, text="Password:", font=("", 10))
    labelPassword.pack()
    bullet = "\u2022"
    entryPassword = Entry(frame, show=bullet)
    entryPassword.pack()
    showPasswdButton = Button(frame, command=showPasswd, image=hiddenPwdImage)
    showPasswdButton.place(in_=entryPassword, relx=1.0, x=-20)

    loginButton = Button(frame, text="Login", command=lambda: login(parent))
    loginButton.pack(pady=(25, 15))
    
    createNewButton = Button(frame, text="Create new Account", command=lambda: moveToCreateAccount(parent))
    createNewButton.pack()
    
    global errorLabel
    errorLabel = Label(frame)
    errorLabel.pack(pady=15)
    
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
            errorLabel.config(text="Name or password Incorrect!")
            entryUsername.config(textvariable="")
    else:
        errorLabel.config(text="Invalid name or password!")
    
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