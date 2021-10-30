# note this decryption code was adapted for use from the code on the website: https://kentjuno.com/learning/python/encrypt-file-with-aes-in-python/?__cf_chl_managed_tk__=pmd_hlkUY4MSLokfXLP0W7X5pldoV.w7AWDdhgcb_gkkEJM-1633346584-0-gqNtZGzNAuWjcnBszROl
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os
import time
import psutil
import bz2
import sys

# decrypt file
def decrypt(fileName, key):
    f = open(fileName,'r+b')
    fileData = f.read()
    f.close()
    
    iv = fileData[:AES.block_size] # retrieve the IV used for encyption
    cipher = AES.new(key, AES.MODE_CBC, iv) # create the cipher using the AES library
    decyptedText = cipher.decrypt(fileData[AES.block_size:]) # decrypt the section of the file
    dec = decyptedText.rstrip(b"\0")
    
    w = open(fileName.replace(".bz2", "_decrypted.bz2"),'w+b')
    w.write(dec)
    w.close()

# using the password to make a key for the encyption
def getKey(password):
    return (SHA256.new(password.encode())).digest()

def main():    
    filename = str(sys.argv[1])
    password = input("Password: ")
    decrypt(filename, getKey(password))
    inputParameter = "bzip2 -dk "+ filename.replace(".bz2", "_decrypted.bz2")
    os.system(inputParameter)
 
if __name__ == "__main__":
    main()