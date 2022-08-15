from os import path
import sqlite3

def createTables():
    global connection
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE Masters(id_master INTEGER PRIMARY KEY, name TEXT, password BLOB)''')
    cursor.execute('''CREATE TABLE Folders(id_folder INTEGER PRIMARY KEY, name TEXT, id_master INTEGER, FOREIGN KEY (id_master) REFERENCES Masters(id_master))''')
    cursor.execute('''CREATE TABLE Logins(id_logins INTEGER PRIMARY KEY, name TEXT, password TEXT, website TEXT, notes TEXT, id_folder INTEGER, FOREIGN KEY (id_folder) REFERENCES Folders(id_folder))''')
    connection.commit()
    
def saveFolderToTable(name):
    global connection
    cursor = connection.cursor()
    data = [(name)]
    cursor.execute('INSERT INTO Folders(name) VALUES (?)', data)

def saveLoginToTable(name, password, website, notes, folderId):
    global connection
    cursor = connection.cursor()
    data = [(name, password, website, notes, folderId)]
    cursor.execute('INSERT INTO Logins(name, password, website, notes, id_folder) VALUES (?, ?, ?, ?, ?)', data)

def connectDatabase(location):
    global connection
    if not path.isfile(location):
        connection = sqlite3.connect(location)
        createTables()
        return False
    else:
        connection = sqlite3.connect(location)
        return True

def closeDatabase():
    global connection
    connection.close()
    
    