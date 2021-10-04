import pyDes
import time
import psutil

fFILE = open("2018-09-19-03_57_11_VN100.csv", "r")
eFILE = open("2018-09-19-03_57_11_VN100-done4.csv", "a")
dFILE = open("2018-09-19-03_57_11_VN100-check4.csv", "a")
usageRAM = 0
start = time.time()
k = pyDes.des(b"DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

for data in fFILE:
   d = k.encrypt(data)
   eFILE.write(d.decode('ISO-8859-1'))


totalTime = time.time() - start
print("Total run time: ", totalTime)
print("Total RAM usage: ", usageRAM)

fFILE.close()
eFILE.close()

eFILE = open("2018-09-19-03_57_11_VN100-done4.csv", "r")

for data2 in eFILE:
   t = k.decrypt(data2.encode('ISO-8859-1'))
   dFILE.write(t.decode('ISO-8859-1'))