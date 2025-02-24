number_1 = int(input("Enter the first number to add: "))
number_2 = int(input("Enter the second number to add: "))

bigger_number = number_1
if number_2 == bigger_number:
	print("These numbers are equal: ")
	
elif number_2 > bigger_number:
	bigger_number = number_2
	print("The biggest number is: ", bigger_number)
else:
	print("The biggest number is: ", bigger_number)