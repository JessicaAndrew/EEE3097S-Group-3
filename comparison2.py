# reading files
f1 = open("/Users/theodorepsillos/Desktop/UCT/Third Year/EEE3097S/2018-09-19_IMU/1.csv", "r")  
f2 = open("/Users/theodorepsillos/Desktop/UCT/Third Year/EEE3097S/2018-09-19_IMU/2.csv", "r")  

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

print(boolean)

