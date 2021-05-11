for i in range(7):
	for j in range(7):
		if  ((j==0 or j==5) and (i!=0 and i!=5 and i!=6)) or ((i==0 or i==5) and (j>0 and j<5)) or (i==j and j>3 and j<=6):
			print("*",end=" ")
		else:
			print(end="  ")
	print()