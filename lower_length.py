#!/bin/env python3
### code for taking a user-inputted sentence, making all lowercase & removing spaces
### then counting number of characters & printing out length
### comments above code

# should be run from terminal line with: python3 lower_length.py
### playing with input so anyone can choose the sentence!
sentence = input("Write a sentence... with some capital letters of course:")
### once you type in the sentence in t
lowsent = sentence.lower()
### using the replace function to remove spaces - essentially, replacing " " with nothing
lownospace = lowsent.replace(" ","")
### now we see if it works!
print(lownospace)
#it does! so we can comment out above statement
### now making a new variable that is the length of the sentence
length = len(lownospace)
### and finally printing 
print(length)