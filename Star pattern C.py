'''
two types of 
patern C
 first part simple pattrrn 
 2nd part little modified
 '''
print("\n\t\t This is first part\n\n")
for row in range(7):
 		for col in range(5):
 			if (col==0) or ((row ==0 or row==6) and (col>0)):
 				print("*" , end=" ")
 			else :
 				print(end="  ")
 		print()
 		
# 2nd part modifiying
print(" \n\t\t This is second part\n\n")
for row in range(7):
 		for col in range(5):
 			if (col==0 and row!=0 and row!=6) or ((row ==0 or row==6) and (col>0)):
 				print("*" , end=" ")
 			else :
 				print(end="  ")
 		print()