# note this encryption code was adapted for use from the code on the website: https://kentjuno.com/learning/python/encrypt-file-with-aes-in-python/?__cf_chl_managed_tk__=pmd_hlkUY4MSLokfXLP0W7X5pldoV.w7AWDdhgcb_gkkEJM-1633346584-0-gqNtZGzNAuWjcnBszROl
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os
import time
import psutil
import bz2
import sys

# function to pad the data to fit how the AES encyption library works
def pad(section):
    return section + b"\0" * (AES.block_size - len(section) % AES.block_size)
   
# encrypt file
def encrypt(fileName, key):
    global usageRAM
    f = open(fileName,'r+b')
    fileData = f.read()
    f.close()
    
    fileData = pad(fileData) # pad the section of the file if it isn't the needed length
    iv = Random.new().read(AES.block_size) # create the needed IV to be used in the encyption
    if usageRAM < psutil.cpu_percent():
         usageRAM = psutil.cpu_percent() # checking for RAM usage
    cipher = AES.new(key, AES.MODE_CBC, iv) # create the cipher using the AES library
    enc = iv + cipher.encrypt(fileData) # encrypt the file
    name = fileName.replace(".bz2", "_e.bz2")
    w = open(name,'w+b')
    w.write(enc)
    w.close()

# using the password to make a key for the encyption
def getKey(password):
    return (SHA256.new(password.encode())).digest()
    
def main():
    filename_in = str(sys.argv[1]).strip()
    filename_out = filename_in.replace(".csv", "_c.bz2")

    start = time.time()
    with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
        fout.write(fin.read())
    stop = time.time()

    timeStart = stop - start
    print(f"Uncompressed size: {os.stat(filename_in).st_size}")
    # Uncompressed size: 1000000
    print(f"Compressed size: {os.stat(filename_out).st_size}")
    # Compressed size: 48
    print("Total compression time:",timeStart) 

    global usageRAM
    usageRAM = 0
    filename = filename_out
    password = str(sys.argv[2]).strip()
    start = time.time()
    encrypt(filename, getKey(password))
    totalTime = time.time() - start
    print("Total encyption time: ", totalTime)
    print("Total RAM usage: ", usageRAM)

 
if __name__ == "__main__":
    main()