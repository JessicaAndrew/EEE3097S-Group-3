from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os,sys
from os import listdir
from os.path import isfile, join
import time
import psutil
import bz2


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
    
# Encrypt file
def encrypt_file(file_name, key):
    global usageRAM
	# Open file to get file Data
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    # Encrypt plaintext with key has been hash by SHA256.
    enc = encrypt(plaintext, key)
    #write Encrypted file
    with open("2018-09-19-11_55_21_VN100_compressed_encypted.bz2", 'wb') as fo:
        fo.write(enc)
        if usageRAM < psutil.cpu_percent():
           usageRAM = psutil.cpu_percent()
        

def getKey(password):
    # Use SHA256 to hash password for encrypting AES 
    hasher = SHA256.new(password.encode())
    return hasher.digest()


def main():
    filename_in = "2018-09-19-11_55_21_VN100.csv"
    filename_out = "2018-09-19-11_55_21_VN100_compressed.bz2"

    start = time.time()
    with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
        fout.write(fin.read())
    stop = time.time()

    timeStart = stop - start
    print(f"Uncompressed size: {os.stat(filename_in).st_size}")
    # Uncompressed size: 1000000
    print(f"Compressed size: {os.stat(filename_out).st_size}")
    # Compressed size: 48
    print("Time:",timeStart) 

    global usageRAM
    usageRAM = 0
    filename = "2018-09-19-11_55_21_VN100_compressed.bz2"
    password = input("Enter the password:")
    start = time.time()
    encrypt_file(filename, getKey(password))
    totalTime = time.time() - start
    print("Total run time: ", totalTime)
    print("Total RAM usage: ", usageRAM)

 
if __name__ == "__main__":
    main()