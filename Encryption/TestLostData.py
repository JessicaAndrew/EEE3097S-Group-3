import filecmp
  
f1 = "2018-09-19-03_57_11_VN100.csv"
f2 = "2018-09-19-03_57_11_VN100-revrev.csv"

result = filecmp.cmp(f1, f2, shallow=False)
print("The result will return True if the files match and False if they do not:\n",result)