# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:13:54 2023

@author: WingYee.Cheung
"""

import random
word_list1 = ["play", "truth", "glow", "computer"]

#define the class Hangman
class Hangman:
    #intialize the attributes
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] *len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    # define the check_guess method to convert the guess into a lowercase, and to see if the letter is in the word (answer)  
    def check_guess(self, guess):
       self.guess = self.guess.lower()
       for letter in self.guess:
           if letter in self.word:
               print(f"Good guess! {guess} is in the word.")
               self.word_guessed[self.word.index(self.guess)] = self.guess
               print(f" Here is what you have achieved so far: {self.word_guessed}")
               self.num_letters -= 1
               print(f" You still have {self.num_letters} letters in the word you need to find out")
           else:
               self.num_lives -= 1
               print(f"Sorry, {self.guess} is not in the word")
               print(f"You have {self.num_lives} lives left.")

   
    # define the ask_for_input method,to ask user for a guess (input)
    # this methods checks if the guess is a single alphabetical character
    # and if the letter has already been guessed
    # if the checks are cleared, the check_guess method is called    
    def ask_for_input(self):
        while self.num_lives != 0:
            self.guess = input("Please enter a letter that you think is part of the word: \n" )
            if (self.guess.isalpha() == False and len(self.guess) != 1):
                print("Invalid letter. Please, enter a single alphabetical character")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
                print(f"These are the letters you have already guessed: \n{self.list_of_guesses}")
        


player1 = Hangman(word_list1)    
player1.ask_for_input()

