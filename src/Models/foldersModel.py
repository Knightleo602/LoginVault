class Folder:
    
    def __init__(self, id, name, logins=[]):
        self.id = id
        self.name = name
        self.logins = logins
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name;
        
    def getId(self):
        return self.id
    
    def addLogin(self, login):
        self.logins.append(login)