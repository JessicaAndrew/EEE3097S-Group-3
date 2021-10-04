# note this encryption code was adapted for use from the code on the website: https://kentjuno.com/learning/python/encrypt-file-with-aes-in-python/?__cf_chl_managed_tk__=pmd_hlkUY4MSLokfXLP0W7X5pldoV.w7AWDdhgcb_gkkEJM-1633346584-0-gqNtZGzNAuWjcnBszROl
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os
import time
import psutil
import bz2

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
    
    w = open("2018-09-19-11_55_21_VN100_compressed_encypted.bz2",'w+b')
    w.write(enc)
    w.close()

# using the password to make a key for the encyption
def getKey(password):
    return (SHA256.new(password.encode())).digest()
    
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
    encrypt(filename, getKey(password))
    totalTime = time.time() - start
    print("Total run time: ", totalTime)
    print("Total RAM usage: ", usageRAM)

 
if __name__ == "__main__":
    main()