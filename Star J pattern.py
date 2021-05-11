for i in range(7):
	for j in range(5):
		if  (i==0 or j==2) or (j==0) and (i>3 and i<6) or (i==6 and j==1):
			print("*",end=" ")
		else:
			print(end="  ")
	print()