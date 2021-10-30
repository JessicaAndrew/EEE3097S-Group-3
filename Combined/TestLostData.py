import filecmp
import sys

f1 = str(sys.argv[1])
f2 = f1.replace(".csv", "_compressed_encypted_decrypted")

result = filecmp.cmp(f1, f2, shallow=True)
print("The result will return True if the files match and False if they do not:")
print("Shallow match: ", result)


# reading files
f1 = open(f1, "r")  
f2 = open(f2, "r")  

i = 0
boolean = True

for line1 in f1:
	i += 1
	
	for line2 in f2:
		
		# matching line1 from both files
		if line1 == line2:
			# print IDENTICAL if similar
			# print("Line ", i, ": IDENTICAL")
			boolean = True	
		else:
			print("Line ", i, ":")
			# else print that line from both files
			print("\tFile 1:", line1, end='')
			print("\tFile 2:", line2, end='')
			boolean = False
		break

# closing files
f1.close()									
f2.close()									

print("Deep match: ", boolean)