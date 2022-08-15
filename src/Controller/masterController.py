from Controller.crypt import getHash
import Controller.database as db
from Models.masterModel import Master

def saveMasterToTable(name, password):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Masters WHERE name =?", (name,))
    if cursor.fetchone() is None:
        hashedpasswd = getHash(password, name)
        cursor.execute('INSERT INTO Masters(name, password) VALUES (?, ?)', (name,hashedpasswd))
        db.connection.commit()
        return True
    else:
        return False

def masterLogin(name, password):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Masters WHERE name=? AND password=?", (name, getHash(password, name)))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        global loggedMaster
        loggedMaster = Master(result[0], result[1])
        return True