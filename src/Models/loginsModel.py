class login:
    
    def __init__(self, id, username, password, passwdTag, notes="", website=""):
        self.username = username
        self.password = self.encryptPasswd(password)
        self.notes = notes
        self.website = website
        self.id = id
    
    def encryptPasswd(self, passwd):
        # codigo para encriptar a senha vai aqui
        return passwd

    def getUserName(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getNotes(self):
        return self.notes
    
    def getWebsite(self):
        return self.website