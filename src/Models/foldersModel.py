class Folder:
    
    def __init__(self, id, name, aescipher):
        self.id = id
        self.name = name
        self.aescipher = aescipher
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name;
        
    def getId(self):
        return self.id