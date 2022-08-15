class login:
    
    def __init__(self, id, username, password, notes="", website=""):
        self.username = username
        self.password = password
        self.notes = notes
        self.website = website
        self.id = id

    def getUserName(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getNotes(self):
        return self.notes
    
    def getWebsite(self):
        return self.website