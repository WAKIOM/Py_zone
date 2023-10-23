#!/usr/bin/python3
'''
take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, go back to point 2.
Write a program which reads one natural number and 
executes the above steps as long as c0 remains different from 1. 
We also want you to count the steps needed to achieve the goal.
Your code should output all the intermediate values of c0, too.
'''
c0 = int(input("enter a positive number\n"))
count=0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0/2
    elif  c0 % 2 != 0:
        c0 = 3 * c0 + 1
    print(int(c0))
    count+=1
    
print("steps =", count)
