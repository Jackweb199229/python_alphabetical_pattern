for i in range(7):
	for j in range(5):
		if  (j==0 or j==4-i or j==i-2):
			print("*",end=" ")
		else:
			print(end="  ")
	print()