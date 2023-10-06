# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:13:54 2023

@author: WingYee.Cheung
"""
import random
word_list1 = ["play", "truth", "glow", "computer"]


class Hangman:
    """This is a word guessing game.
    
    It asks users to guess one alphabet at a time.
    The answer (a word) is randomly chosen from any predefined word list.
    The default is for users to have 5 lives to start with. 
    Each wrong guess takes away a live.
    The game ends when there is no more lives left."""
    
    def __init__(self, word_list, num_lives = 5):
        """There are two parameters. 
        The first one is the word list (word_list). 
        Administrators of the game can create a word list of any length, to be stored as a list.
        The second parameter is number of lives left (num_lives).
        The default is set as 5. Adminstrators/users of the game can change it.        
        
        A word will be randomly selected as the answer of the game.
        In the output, the game will display the alphabet(s) guessed (list_of_guesses), 
        successful guesses achieved (word_guessed), and
        number of lives remain (num_lives).      
        """
        
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] *len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    
    def check_guess(self, guess):
       """This check_guess method converts the guess into lowercase, 
           and checks if the letter is in the word. 
           If it is, the game will display the letter within the word (to show the index of the letter within the word).
           They will also see how many unique letter is left to be guessed in the word.
           
           If they guessed wrong, they have lose one live. 
           They will see the number of lives left in the game.
              
       """
       
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
  
    
    def ask_for_input(self):
        """This ask_for_input method asks users to enter a single alphabet.
        It first checks if the input is a single alphabet.
        If not, it'll ask for another input.
        If it is a single alphabet, it'll check if the input has already been guessed.
        
        If both checks were cleared, the game will call he check_guess method, 
        to see if the letter is in the word. 
        
        In the output, users will see the list of letters they have already guessed.
        
        The game ends when there is no more live left.       
        """

        self.guess = input("Please enter a letter that you think is part of the word: \n" )
        if (self.guess.isalpha() == False and len(self.guess) != 1):
            print("Invalid letter. Please, enter a single alphabetical character")
        elif self.guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)
            print(f"These are the letters you have already guessed: \n{self.list_of_guesses}")
            print(f" This is the number of unique letters left (num_letters) for guessing: {self.num_letters}")


### an attempt to follow the practical instructions:
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if (game.num_lives == 0):
            print("You lost!")
            break
        elif game.num_letters > 0:
             game.ask_for_input()       
        else:
            print("Congratulations. You won the game!")
            break


 

play_game(word_list1) 


### tried an alternative way, still couldn't stop the game from running after num_lives == 0:

#def play_game(word_list):
#    num_lives = 5
#    game = Hangman(word_list, num_lives)
#    while True:
#        if (num_lives == 0):
#            print("You lost!")
#            break   
#        if num_lives != 0:
#            if game.num_letters > 0:
#               game.ask_for_input()       
#            else:
#               print("Congratulations. You won the game!")

        
