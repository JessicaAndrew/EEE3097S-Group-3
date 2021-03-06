# note this code was adapted for use from the code on the website: https://kentjuno.com/learning/python/encrypt-file-with-aes-in-python/?__cf_chl_managed_tk__=pmd_hlkUY4MSLokfXLP0W7X5pldoV.w7AWDdhgcb_gkkEJM-1633346584-0-gqNtZGzNAuWjcnBszROl
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time
import psutil

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
    
    w = open("2018-09-19-11_55_21_VN100-AESen.csv",'w+b')
    w.write(enc)
    w.close()
    
# decrypt file
def decrypt(fileName, key):
    f = open(fileName,'r+b')
    fileData = f.read()
    f.close()
    
    iv = fileData[:AES.block_size] # retrieve the IV used for encyption
    cipher = AES.new(key, AES.MODE_CBC, iv) # create the cipher using the AES library
    decyptedText = cipher.decrypt(fileData[AES.block_size:]) # decrypt the section of the file
    dec = decyptedText.rstrip(b"\0")
    
    w = open("2018-09-19-11_55_21_VN100-AESen.csv",'w+b')
    w.write(dec)
    w.close()

# using the password to make a key for the encyption
def getKey(password):
    return (SHA256.new(password.encode())).digest()

def main():
    global usageRAM
    usageRAM = 0
    filename = "2018-09-19-11_55_21_VN100.csv"
    password = input("Enter the password:")
    
    start = time.time()
    encrypt(filename, getKey(password))
    totalTime = time.time() - start
    print("Total run time: ", totalTime)
    print("Total RAM usage: ", usageRAM)
    
    filename = "2018-09-19-11_55_21_VN100-AESen.csv"
    password = input("Password: ")
    decrypt(filename, getKey(password))
 
if __name__ == "__main__":
    main()
