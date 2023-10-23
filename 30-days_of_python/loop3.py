#!/usr/bin/python3
'''
Write a program that eats vowels then creates a word out of the remaining letters
'''
word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = str.upper(input("Enter a random word\n"))

for letter in user_word:
    # Complete the body of the loop.
    if letter in 'AEIOU':
        continue
    word_without_vowels+=letter
# Print the word assigned to word_without_vowels.
print(word_without_vowels)

