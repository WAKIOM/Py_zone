#!/usr/bin/python3
'''
Write a script to reverse a list
'''

my_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
length = len(my_list)
new_list = []

for i in range(length):
        new_list.insert(0, my_list[i])

print(new_list)
