#!/usr/bin/python3
'''
write a line of code that prompts the user to replace the middle number
 in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3)
'''
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
number=int(input("enter a number\n"))
# to replace the middle number with an integer number entered by the user.
hat_list[2] = number
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
print("The length of the list is:",len(hat_list))
print("List values: ",hat_list)

