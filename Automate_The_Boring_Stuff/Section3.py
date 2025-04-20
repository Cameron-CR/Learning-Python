################## Section 3, Lesson 8 – Python's Built-in Functions #################

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

#import pyperclip

#pyperclip.copy('Hello World')
#text = pyperclip.paste()
#print(text)



##################### LESSON 9 - Writing your own functions  ####################

# functions are mini programs inside of a program 

#* def hello(): #what does def stand for? Define? 
   # print('Howdy!')
   # print('Howdy!')
   # print('Hello There')


# use pythontutor.com to visualize code! 

# arguments are variables pass into a function

#def hello(name):
 #       print('Hello ' + name)
    

#hello('Cameron')
#hello('Bob')



### PRACTICE QUESTIONS#####


#. Write a script that simulates rolling a 6-sided die three times using random.randint(), and prints each result with labels.

#Stretch: Calculate and print the total score

import random

def rollDice(): # function to simulate the diceroll, and out put it, my thinking is that I can just call this function 3 times, trying to reuse it. 
    diceRoll = random.randint(1,6)
    return diceRoll

def calculateSum(number1, number2, number3): # seperated function for the calculation
        newNumber = number1 + number2 + number3
        return newNumber


num1 = rollDice()
num2 = rollDice()
num3 = rollDice()

print('Dice roll 1 is: ' +  str(num1)) # violates dry principle but just playing right now 
print('Dice roll 2 is: ' +  str(num2)) # could make this a loop, ask gpt how I could get the variable names to increment as well maybe
print('Dice roll 3 is: ' +  str(num3))

total = calculateSum(num1, num2, num3)

print('Your total score is: ' + str(total))



####Question 2 - 2. Conditional Clipboard
#Use pyperclip to copy a message only if a variable called enabled is set to True.

#If enabled == True, copy “Automation Activated!”

#If enabled == False, print “Clipboard is disabled.”
import pyperclip

input = "Carefully Copy Me"
enabled = False


if enabled == True:
    pyperclip.copy(text_to_copy)
    print("Copied to clipboard!")
else:
    print("Clipboard copy disabled.")



#Question 3 ###################

#import sys

#print('1')
#print('2')
#sys.exit(0)
#print('3')


########## QUESTION 4 ########


#generating a random number, gonna modify the code / requirements a bit to test functions to get more reps in 
import random
def generateRandomNumber():
    randomNumber = random.randint(1, 10)
    return randomNumber


def compareGuessWithRandom(answer, userGuessedNumber): #wrote this so I can either hard code the number, take input, or use the generateRandomNumber function to run this over and over again (which is what I am going to do )
     if(userGuessedNumber == answer):
          print('You got it! The number Was ' + str(answer))
          sys.exit(0)
     else:
        print('Sorry! You guessed ' + str(userGuessedNumber) + ' but the number was ' + str(answer))

Q4number1 = generateRandomNumber()
Q4number2 = generateRandomNumber()

compareGuessWithRandom(Q4number1,Q4number2)