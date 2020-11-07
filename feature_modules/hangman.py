# Class creates the hangman game once instantiated.
# Users are given 5 attempts to guess a random word

import random  # random module used to generate a random entry from a list of words
import config  # config module used to retrieve word list and gives access to global styling


class Hangman:
    def __init__(self):
        # variable contains program on or off state, always start as True to indicate menu running
        self.is_running = True
        self.word_list = config.hangman_word_list  # import the word list from the config.py file
        self.word = random.choice(self.word_list)  # string holds the current word to guess
        self.word_letters = list(self.word)  # list holds a list of all the random words letters
        self.guessed_word = ""  # string holds the users correct guesses
        self.guessed_letters = []  # list holds all guessed letters
        self.guess_counter = 8  # variable holds the amount of guesses a user has left

        print("\n🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆃🅷🅴 🅷🅰🅽🅶🅼🅰🅽 🅶🅰🅼🅴")  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')

        self.hangman_start()  # trigger the hangman_start method to provide user instructions

    # method guides the user through the game, looping each time the user enters an input until the game ends
    def hangman_start(self):
        while self.is_running:  # when this while loop breaks, we return to the main module
            self.word_mask()  # masks the characters in the word which the user hasn't guessed yet
            print("\n====================================================\n")
            print("The word you are guessing is {}".format(self.guessed_word))
            print("You have {} guesses left".format(self.guess_counter))
            print("You have already guessed these letters: {}".format(self.guessed_letters))

            # while word is masked - loop the following actions!
            letter_guess = self.input_check()
            if letter_guess == "exit":  # check for the "exit" keyword.
                print("Goodbye from the hangman game!")
                break  # if "exit" found we break the loop, leaving this feature module
            self.guess_number(letter_guess)  # method checks if the letter is in the self.word variable
            self.guessed_letters.append(letter_guess)
            self.word_mask()
            self.completed_check()
        #  ask user if they want to play again- if yes game state is reset, if no, game exits
        self.replay_check()

    # method used to hide the word, making all unknown characters * symbols
    def word_mask(self):
        self.guessed_word = ""  # set the word to an empty string
        for entry in self.word_letters:  # loop through each character in the word_letter array (5)
            if entry in self.guessed_letters:  # loop though all of the letters a user has guessed
                # If a letter matches, the letter is concatenated to the guessed_word variable
                self.guessed_word += entry
            else:
                # If a letter isn't found, a * is concatenated to the guessed_word variable
                self.guessed_word += "*"

    # method checks to ensure correct string is entered by user
    def input_check(self):
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            user_input = input(": ")
            if len(user_input) > 1:  # check to see if user_input length is greater than 1 character
                if user_input.lower() == "exit":
                    self.is_running = False  # statement breaks input while loops
                    user_input = user_input.lower()  # .lower ensures the input is returned in correct format
                elif user_input.lower() == "help":  # if/else statement controls tailored help messages
                    print("\nYou are in the hangman game! Type in a single letter to guess the word")
                else:  # user didnt enter "help" or "exit" but put in more than one letter
                    print("\nYou can only input a single letter, please try again 👍")
            else:
                break  # input is a valid single character, break the loop to return the user input
        return user_input  # return the valid input

    # method checks to see if users guess is in the random word, if not decreases the guess_counter
    def guess_number(self, user_input):
        if user_input not in self.word:
            self.guess_counter -= 1  # decrease the counter by 1. Game ends at 0 after 5 guesses

    # method checks to see if a user has won or lost the game, breaking the is_running while loop either way
    def completed_check(self):
        if self.word == self.guessed_word:
            print("\n*** Congratulations you successfully guessed the word! ***")
            self.is_running = False  # setting variable to false breaks the play loop
        elif self.guess_counter == 0:  # if guessed more than 5 times player loses and game ends
            print("\nYou didnt manage to guess the word this time!")
            print("The word was {}".format(self.word))
            self.is_running = False

    # method checks to see if user wants to replay the game after its finished
    def replay_check(self):
        selection = False  # local variable to control while loop, ensuring user makes a choice
        while not selection:
            print("\nWould you like to play again?")
            replay = input("Enter '1' for yes, '2' for no: ")
            if replay == "1":
                # if user wants to restart we need to reset game state and restart
                self.word = random.choice(self.word_list)  # get a new random word from list of possible words
                self.word_letters = list(self.word)  # list holds a list of all the random words letters
                self.guessed_word = ""  # string holds the users correct guesses
                self.guessed_letters = []  # list holds all guessed letters
                self.guess_counter = 5  # re-set try counter to 5
                self.is_running = True  # re-enter the start loop
                self.hangman_start()  # restart the game
            elif replay == "2" or replay.lower() == "exit":  # user wants to leave the game
                print("Goodbye from the hangman game!")
                selection = True
                # leaving the method will cause the script to end and put the user back to the main menu
            elif replay.lower() == "help":
                print("\nYou are in the hangman game! Type in '1' to play again, or '2' to exit the game")
