from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os,sys
from os import listdir
from os.path import isfile, join
import time
import psutil
import bz2
    
# Decrypt message with password
def decrypt(ciphertext, key):
    #get Iv from encrypted data file
    iv = ciphertext[:AES.block_size]
    #initial new AES with key, Mode, iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    #decrypt Data file.
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")
        
# Decrypt file
def decrypt_file(file_name, key):
    #read file to get encrypted data
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    # decrypt file with password has been hash by SHA256    
    dec = decrypt(ciphertext, key)
    #save decrypted file
    with open("2018-09-19-11_55_21_VN100_compressed_encypted_decrypted.bz2", 'wb') as fo:
        fo.write(dec)
# hash pasword to get 16 bytes key.

def getKey(password):
    # Use SHA256 to hash password for encrypting AES 
    hasher = SHA256.new(password.encode())
    return hasher.digest()

def main():    
    filename = "2018-09-19-11_55_21_VN100_compressed_encypted.bz2"
    password = input("Password: ")
    decrypt_file(filename, getKey(password))
    
    os.system("bzip2 -dk 2018-09-19-11_55_21_VN100_compressed_encypted_decrypted.bz2")
 
if __name__ == "__main__":
    main()