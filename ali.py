import random
def your_Number ():
	top_of_range=input("Type a number : ")

	if top_of_range.isdigit():
		top_of_range=float(top_of_range)
		print(top_of_range)
		if top_of_range <=0:
			print('type larger number next time')
			
	else:
		print('type number please ? ')
	return top_of_range , type(top_of_range) ,random.randint(0,top_of_range)
print(your_Number())