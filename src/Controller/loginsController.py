import Controller.database as db
from Models.loginsModel import login
import Controller.foldersController as fdr

def saveLoginToTable(name, password, website, notes, folderId):
    cursor = db.connection.cursor()
    cursor.execute('INSERT INTO Logins(name, password, website, notes, id_folder) VALUES (?, ?, ?, ?, ?)', (name, password, website, notes, folderId))
    db.connection.commit()

def loadLogins():
    global logins
    logins = []
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Logins WHERE id_folder =?", (fdr.selectedFolder,))
    for row in cursor.fetchall():
        logins.append(login(row[1], row[2], row[3], row[4]))
    return logins