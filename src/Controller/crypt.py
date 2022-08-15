from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

class AES:
        
    def __init__(self, key):
        self.key = SHA256.new(key)
        
        
    def encrypt(self, text):
        self.cipher = AES.new(self.key, AES.MODE_EAX)
    
def getHash(text, salt):
    return SHA256.new((text + salt).encode()).digest()