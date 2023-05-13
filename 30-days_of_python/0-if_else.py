#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    #prompt a user to input a number
    n = int(input("Enter a number less than 100: ").strip())
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n > 5 and n <= 20:
            print("Weird")
        elif n > 20 and n <= 100:
            print("Not Weird")