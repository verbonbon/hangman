# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 12:15:20 2023

@author: WingYee.Cheung
"""
#Task 1

#Step 1:
#Create a list containing the names of your 5 favorite fruits.
#Step 2:
#Assign this list to a variable called word_list.

word_list = ["apple", "strawberry", "sharon fruit", "mango", "durian"]

#Step 3:
#Print out the newly created list to the standard output (screen)

print(word_list)


#Task 2 Choose a random word from the list
#Step 1:
#Go to the first line of your file.
#Step 2:
#Write import random on the line. 
#Note: To import a module, you have to use the import keyword at the top of the file.

import random

#Step 3:
#Create the random.choice method and pass the word_list variable into the choice method.
#Step 4:
#Assign the randomly generated word to a variable called word.
#Step 5:
#Print out word to the standard output. 
#Run the code several times and observe the words printed out after each run.

word = random.choice(word_list)

print(word)


#Task 3: ask the user for an input
#In this task, you are required to take user input. 
#As you now know, the print() function in Python displays output on the screen. 
#Conversely, Python has an input() function that takes input from the screen. 
#Note that the input function returns the user input in form of a string.

#Step 1:
#Using the input function, ask the user to enter a single letter.
#Step 2:
#Assign the input to a variable called guess.


guess = input("Enter your guess here: \n")


#task 4: check that the input is a single character
#Step 1:
#Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
#Step 2:
#In the body of the if statement, print a message that says "Good guess!".
#Step 3:
#Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

if len(guess == 1 and guess.isalpha == True ):
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")


