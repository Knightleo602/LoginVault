class logins:
    
    def __init__(self, username, password, notes="", website=""):
        self.username = username
        self.password = self.encryptPasswd(password)
        self.notes = notes;
        self.website = website
    
    def encryptPasswd(passwd):
        # codigo para encriptar a senha vai aqui
        return passwd