from passlib.hash import bcrypt
from Controller.crypt import AESCipher, getHash
import Controller.database as db
from .foldersController import createDefaultFolders
from Models.masterModel import Master

def saveMasterToTable(name, password):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Masters WHERE name =?", (name,))
    if cursor.fetchone() is None:
        hashedpasswd = getHash(password)
        
        cursor.execute('INSERT INTO Masters(name, password) VALUES (?, ?)', (name,hashedpasswd))
        db.connection.commit()
        global loggedMaster, aesCipher
        loggedMaster = Master(cursor.lastrowid, name)
        createDefaultFolders()
        return True
    else:
        return False

def masterLogin(name, password):
    global loggedMaster, aesCipher
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Masters WHERE name=?", (name,))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        if bcrypt.verify(password, result[2]):
            loggedMaster = Master(result[0], result[1])
            return True
        return False