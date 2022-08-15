from tkinter import *

def showOptionsMenu(parent):
    frame = Toplevel(parent)
    frame.title("")
    
    accountLabel = Label(frame, text="Account:")
    languageLabel = Label(frame, text="Language:")
    appearancelabel = Label(frame, text="Appearance:")
    
    accountLabel.pack()
    languageLabel.pack()
    appearancelabel.pack()
    
    applyButton = Button(frame, text="Apply", command=apply)
    discardButton = Button(frame, text="Discard", command=discard)
    
    applyButton.pack(side=RIGHT, padx=(20, 0))
    discardButton.pack(side=LEFT, padx=(0, 20))
    
    frame.grab_set()
    frame.attributes('-topmost', True)
    
    frame.mainloop()
    
def showAccountSettings(parent):
    master = Frame(parent)

def apply():
    ...
def discard():
    ...