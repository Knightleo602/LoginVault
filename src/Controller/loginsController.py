import Controller.database as db
from Models.loginsModel import login
import Controller.foldersController as fdr

def saveLoginToTable(name, password, website, notes, folderId):
    cursor = db.connection.cursor()
    encryptedpasswd = fdr.getSelectedFolder().aescipher.encrypt(password)
    cursor.execute('INSERT INTO Logins(name, password, website, notes, id_folder) VALUES (?, ?, ?, ?, ?)', (name, encryptedpasswd, website, notes, folderId))
    db.connection.commit()

def loadLogins():
    global logins, aesCipher
    logins = []
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Logins WHERE id_folder =?", (fdr.selectedFolder,))
    for row in cursor.fetchall():
        decryptedpasswd = fdr.getSelectedFolder().aescipher.decrypt(row[2])
        logins.append(login(row[0], row[1], decryptedpasswd, website=row[3], notes=row[4]))
    return logins