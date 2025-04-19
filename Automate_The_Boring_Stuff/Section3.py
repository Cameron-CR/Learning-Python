# Section 3, Chapter 8 – Python's Built-in Functions

# # Import random module and print a random integer between 1 and 10
#import random

#random_number = random.randint(1, 10)

#print(random_number) 

#demonstrating how to import multiple functions 


#video is just showing another way to import, but notes it is not recommendded
#from random import *
#randint(1,10)


#how to terminate a program early
#import sys

#print('Hello')

#sys.exit(0)  #notice, this is where it ends, we never get to the goodbye part

#print('Goodbye')


#next part is explaining how to install a thirdy party module with pip in the command line - goal is to install "pyperclip"
#pyperclip is used to copy and paste text 

import pyperclip

pyperclip.copy('Hello World')
text = pyperclip.paste()
print(text)