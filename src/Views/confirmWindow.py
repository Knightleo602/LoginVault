from tkinter import *

def showConfirmWindow(parent, msg, function):
    global confirmmenu
    confirmmenu = Toplevel(parent)
    confirmmenu.resizable(0,0)
    confirmmenu.title("")
    
    msg = Label(confirmmenu, text=msg)
    
    yesButton = Button(confirmmenu, text="Yes", command=function)
    noButton = Button(confirmmenu, text="No", command=leaveConfirm)
    
    msg.pack(expand=True, pady=(20, 0), padx=20)
    noButton.pack(expand=True, side=LEFT, pady=(20, 20))
    yesButton.pack(expand=True, side=LEFT, pady=(20, 20))
    confirmmenu.grab_set()
    confirmmenu.attributes('-topmost', True)
    confirmmenu.mainloop()
    
    
# https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method

def leaveConfirm():
    global confirmmenu
    confirmmenu.destroy()
    
