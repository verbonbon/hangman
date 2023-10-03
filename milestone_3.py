# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:01:27 2023

@author: WingYee.Cheung
"""

#Write code that will continuously ask the user for a letter and validate it.


#Create a new script called milestone_3.py. This file will contain the code for this milestone.

#Step 1:
#Create a while loop and set the condition to True. 
#Setting the condition to True` ensures that the code runs continuously.
#In the body of the loop, write the code required for the following steps.

#Step 2:
#Ask the user to guess a letter and assign this to a variable called guess.


#Step 3:
#Check that the guess is a single alphabetical character. 
#Hint: You can use Python's isalpha method to check if the guess is alphabetical.

#Step 4:
#If the guess passes the checks, break out of the loop.

#Step 5:
#If the guess does not pass the checks, 
#then print a message saying "Invalid letter. Please, enter a single alphabetical character."

def check_validity():
    while True:
        user_input = input("Please enter a letter that you think is part of the word: \n" )
        if (user_input.isalpha() == True and len(user_input) == 1):
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character")

#Good job so far!
#But your code probably doesn't look great.
#It's hard to tell which lines do what.

#Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things.
#The check_guess function will take the guessed letter as an argument and check if the letter is in the word.

#Step 1:
#Define a function called check_guess. 
#pass in the guess as a parameter for the function.
#Write the code for the following steps in the body of this function.

#Step 2:
#Convert the guess into lower case.

#Step 3:
#Move the code that you wrote to check if the guess 
#is in the word into this function block.

answer = ["p","l", "a", "y"]

def check_guess(user_input):
    user_input = user_input.lower()
    for letter in user_input:
        if letter in answer:
            print("This letter is in the word")
        else:
            print("This letter is not in the word")
    
 


#The ask_for_input function.
#Step 1:
#Define a function called ask_for_input.

#Step 2:
#Move the code that you wrote in the Iteratively check if the input 
#is a valid guess task into this function block.

#Step 3:
#Outside the while loop, but within this function, 
#call the check_guess function to check if the guess is in the word.
# Don't forget to pass in the guess as an argument to the method.



def ask_for_input():
    
    while True:
        user_input = input("Please enter a letter that you think is part of the word: \n" )
        if (user_input.isalpha() == True and len(user_input) == 1):
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character")
    
    
    check_guess(user_input)
   

ask_for_input()
    
        
        

#Step 4:
#Outside the function, call the ask_for_input function to test your code.

    



