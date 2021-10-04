# note this code was adapted for use from the code on the website: https://kentjuno.com/learning/python/encrypt-file-with-aes-in-python/?__cf_chl_managed_tk__=pmd_hlkUY4MSLokfXLP0W7X5pldoV.w7AWDdhgcb_gkkEJM-1633346584-0-gqNtZGzNAuWjcnBszROl
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os,sys
from os import listdir
from os.path import isfile, join
import time
import psutil

def pad(s):
    # Data will be padded to 16 byte boundary in CBC mode
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

# Encrypt message with password
def encrypt(message, key, key_size=256):
    global usageRAM
    #Message is file data, this Pad will change data file to 16 Byte boundary to use in CBC mode of AES
    message = pad(message)
    # Generata iv with random of AES block_size : IV (byte string) - The initialization vector to use for encryption or decryption.
    iv = Random.new().read(AES.block_size)
    if usageRAM < psutil.cpu_percent():
         usageRAM = psutil.cpu_percent()
    # Initial Data file with key(password has been hash), Mode of has, iv.
    # Cipher-Block Chaining (CBC). Each of the ciphertext blocks depends on the current and all previous plaintext blocks. An Initialization Vector (IV) is required.
    # The IV is a data block to be transmitted to the receiver. The IV can be made public, but it must be authenticated by the receiver and it should be picked randomly.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    #return data file with encrypted data.
    return iv + cipher.encrypt(message)
    
# Decrypt message with password
def decrypt(ciphertext, key):
    #get Iv from encrypted data file
    iv = ciphertext[:AES.block_size]
    #initial new AES with key, Mode, iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    #decrypt Data file.
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")
    
# Encrypt file
def encrypt_file(file_name, key):
    global usageRAM
	# Open file to get file Data
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    # Encrypt plaintext with key has been hash by SHA256.
    enc = encrypt(plaintext, key)
    #write Encrypted file
    with open("2018-09-19-11_55_21_VN100-AESen.csv", 'wb') as fo:
        fo.write(enc)
        if usageRAM < psutil.cpu_percent():
           usageRAM = psutil.cpu_percent()
        
# Decrypt file
def decrypt_file(file_name, key):
    #read file to get encrypted data
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    # decrypt file with password has been hash by SHA256    
    dec = decrypt(ciphertext, key)
    #save decrypted file
    with open("2018-09-19-11_55_21_VN100-AESende.csv", 'wb') as fo:
        fo.write(dec)
# hash pasword to get 16 bytes key.

def getKey(password):
    # Use SHA256 to hash password for encrypting AES 
    hasher = SHA256.new(password.encode())
    return hasher.digest()


def main():
    global usageRAM
    usageRAM = 0
    filename = "2018-09-19-11_55_21_VN100.csv"
    password = input("Enter the password:")
    start = time.time()
    encrypt_file(filename, getKey(password))
    totalTime = time.time() - start
    print("Total run time: ", totalTime)
    print("Total RAM usage: ", usageRAM)
    
    filename = "2018-09-19-11_55_21_VN100-AESen.csv"
    password = input("Password: ")
    decrypt_file(filename, getKey(password))
 
if __name__ == "__main__":
    main()
