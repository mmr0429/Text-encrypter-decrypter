from cryptography.fernet import Fernet #AES
#pip install cryptography
from fileio import *

def encr(udata, k_pth, m_pth): #key path and final message path
    key = Fernet.generate_key()
    bwrite(str(k_pth),key)
    bdata=udata.encode()
    encrypter=Fernet(key)
    edata = encrypter.encrypt(bdata)
    bwrite(str(m_pth),edata)
    #print(edata)

def decr(k_path, m_path):
    key = bread(str(k_path))
    bdata=bread(str(m_path))
    decrypter=Fernet(key)
    dedata = decrypter.decrypt(bdata)
    dedata=dedata.decode('UTF-8','strict')
    return dedata
