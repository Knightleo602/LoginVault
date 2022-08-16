from tkinter import *
from Controller.masterController import saveMasterToTable
from Views.mainview import createMainView
from Controller.extraFunctions import checkString
import Models.globals as globals

passwdState = False

def createLoginView(parent):
    global frame
    frame = Frame(parent)
    
    labelMain = Label(frame, text="Welcome!", font=("", 15))
    labelMain.pack(pady=20)
    
    labelMain = Label(frame, text="Create a new account to get started.", font=("", 15))
    labelMain.pack(pady=(20, 25))
    
    global entryUsername
    labelUsername = Label(frame, text="Username:", font=("", 10))
    labelUsername.pack()
    entryUsername = Entry(frame)
    entryUsername.pack(pady=(0, 4))
    
    global entryPassword, hiddenPwdImage, visiblePwdImage, showPasswdButton
    hiddenPwdImage = PhotoImage(file=globals.currentpath+"/img/hiddenPasswdSmall.png", width=15, height=15)
    visiblePwdImage = PhotoImage(file=globals.currentpath+"/img/visiblePasswdSmall.png", width=15, height=15)
    labelPassword = Label(frame, text="Password:", font=("", 10))
    labelPassword.pack()
    bullet = "\u2022"
    entryPassword = Entry(frame, show=bullet)
    entryPassword.pack()
    showPasswdButton = Button(frame, command=showPasswd, image=hiddenPwdImage)
    showPasswdButton.place(in_=entryPassword, relx=1.0, x=-20)

    global entryConfirmPassword
    labelConfirmPassword = Label(frame, text="Confirm Password:", font=("", 10))
    labelConfirmPassword.pack()
    entryConfirmPassword = Entry(frame, show=bullet)
    entryConfirmPassword.pack()

    add = Button(frame, text="Create", command=lambda: create(parent))
    add.pack(pady=(25, 15))
    
    global errorLabel
    errorLabel = Label(frame)
    errorLabel.pack()
    
    frame.pack()
    
def create(root):
    global errorLabel, frame
    username = entryUsername.get().strip()
    password = entryPassword.get()
    confirmpasswd = entryConfirmPassword.get()
    if checkString(username) and checkString(password):
        if password == confirmpasswd:
            if saveMasterToTable(username, password):
                errorLabel.config(text="User successfully created!")
                frame.destroy()
                createMainView(root)
            else:
                errorLabel.config(text="User already exists!")
        else:
            errorLabel.config(text="Password doesn't match!")
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
    
    