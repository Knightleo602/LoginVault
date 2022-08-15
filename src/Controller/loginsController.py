from .crypt import encrypt
import Controller.database as db
from Models.loginsModel import login
import Controller.foldersController as fdr
import Controller.masterController as mr

def saveLoginToTable(name, password, website, notes, folderId):
    cursor = db.connection.cursor()
    encryptedpasswd = encrypt(password, mr.loggedMaster.hashedPassword)
    cursor.execute('INSERT INTO Logins(name, password, website, notes, id_folder) VALUES (?, ?, ?, ?, ?)', (name, encryptedpasswd, website, notes, folderId))
    db.connection.commit()

def loadLogins():
    global logins
    logins = []
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Logins WHERE id_folder =?", (fdr.selectedFolder,))
    for row in cursor.fetchall():
        encryptedPasswd, nonce, tag = encrypt(row[2])
        logins.append(login(row[1], encryptedPasswd, website=row[3], notes=row[4]))
    return logins