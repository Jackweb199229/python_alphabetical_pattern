for i in range(6):
	for j in range(6):
		if  ((j==0 or j==5) and (i!=0 and i!=5)) or ((i==0 or i==5) and (j>0 and j<5)):
			print("*",end=" ")
		else:
			print(end="  ")
	print()