#!/usr/bin/python3
'''
A program that eats vowels and prints the nonvowels
'''
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = str.upper(input("enter a random word\n"))
for letter in user_word:
    # Complete the body of the for loop.
    if letter in 'AEIOU':
        continue
    print(letter)
