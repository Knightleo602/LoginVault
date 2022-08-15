from Models.foldersModel import Folder
import Controller.masterController as master
import Controller.database as db

selectedFolder = 0
amount = 0

def saveFolderToTable(name):
    global folders, amount
    if amount >= 10:
        return False
    cursor = db.connection.cursor()
    cursor.execute('INSERT INTO Folders(name, id_master) VALUES (?, ?)', (name,master.loggedMaster.id))
    db.connection.commit()
    return cursor.lastrowid

def loadFolders():
    global folders, selectedFolder, amount
    folders = []
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Folders WHERE id_master =?", (master.loggedMaster.id,))
    amount = 0
    for row in cursor.fetchall():
        amount += 1
        folders.append(Folder(row[0], row[1]))
    selectedFolder = folders[0].getId()
    return folders

def createDefaultFolders():
    saveFolderToTable("Favorites")
    saveFolderToTable("Default")

def getSelectedFolder():
    global folders, selectedFolder
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Folders WHERE id_folder =?", (selectedFolder,))
    result = cursor.fetchone()
    return Folder(result[0], result[1])

def getFolderId(name):
    global folders
    for i in folders:
        if i.getName() == name:
            return i.getId()
    
    
    
    