import filecmp
  
f1 = "/Users/theodorepsillos/Desktop/UCT/Third Year/EEE3097S/2018-09-19_IMU/1.csv"
f2 = "/Users/theodorepsillos/Desktop/UCT/Third Year/EEE3097S/2018-09-19_IMU/2.csv"
  
# shallow comparison
# result = filecmp.cmp(f1, f2)
# print(result)
# deep comparison

result = filecmp.cmp(f1, f2, shallow=False)
print("The result will return True if the files match and False if they do not:\n",result)
