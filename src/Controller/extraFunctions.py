import re

def checkString(string): # verifica se nao tem nenhum character especial nao permitido na string
    
    return bool(re.match('^[a-zA-Z0-9]*$',string)) and not string == ""