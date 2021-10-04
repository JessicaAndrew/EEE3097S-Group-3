# note this code was edited based on code from: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm
import time
import psutil

f = open("2018-09-19-12_20_31_VN100.csv", "r")
e = open("2018-09-19-12_20_31_VN100-rev.csv", "a")
usageRAM = 0
start = time.time()

for message in f:
   i = len(message) - 1
   translated = ""

   while i >= 0:
      translated = translated + message[i]
      i = i - 1
   e.write(translated)
   if usageRAM < psutil.cpu_percent():
         usageRAM = psutil.cpu_percent()

totalTime = time.time() - start
print("Total run time: ", totalTime)
print("Total RAM usage: ", usageRAM)

f.close()
e.close()
