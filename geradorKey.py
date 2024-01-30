from random import choice
import string

def sessionKey():    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    key = ''
    for i in range(40):
        key += choice(caracteres)
    return key