#!/usr/bin/python3
'''
a script that removes duplicates from a list
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
uniq=[]
for num in my_list:
    if num in uniq:
        continue
    else:
        uniq.append(num)
print("The list with unique elements only:", uniq)
print("List with duplicates:", my_list)
