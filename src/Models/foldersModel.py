class Folder:
    
    def __init__(self, name, logins=[]):
        self.name = name
        self.logins = logins
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name;
        
    def addLogin(self, login):
        self.logins.append(login)