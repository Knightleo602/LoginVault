from Crypto.Cipher import AES
from bcrypt import hashpw, gensalt

# pip install pycryptodome
# pip instll bcrypt
        
def encrypt(text, key):
    global nonce, tag
    cipher = AES.new(key, AES.MODE_EAX)
    encryptedtext = cipher.encrypt(text)
    return encryptedtext

def decrypt(encryptedtext, key, nonce):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(encryptedtext)
    try: 
        cipher.verify(tag)
        return plaintext
    except:
        return False
    
def getHash(text):
    return hashpw(text.encode('utf_8'), gensalt())