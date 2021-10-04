# note this code was edited based on code from: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm
d = open("2018-09-19-04_22_21_VN100-revrev.csv", "a")
e = open("2018-09-19-04_22_21_VN100-rev.csv", "r")

for message in e:
   i = len(message) - 1
   translated = ""

   while i >= 0:
      translated = translated + message[i]
      i = i - 1
   d.write(translated)


d.close()
e.close()
