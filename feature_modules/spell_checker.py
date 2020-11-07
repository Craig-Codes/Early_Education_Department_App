# Class creates the spell checker once instantiated.
# Allows user to input a sentence and get the correctly formatted sentence back

import config  # config module used to store calculator data and gives access to global styling


class Checker:
    def __init__(self):  # set variables when class initialised
        self.is_running = True  # variable contains program on or off state, always start as True
        self.sentence = "A structure which humans occupy"  # sentence used to check user types in correct sentence
        # dictionary of possible word entries and their corresponding corrections
        # this prototype takes into account some variations of case sensitivity - this could easily be expanded on
        self.words_to_check = {"structure": "building", "STRUCTURE": "BUILDING", "Structure": "Building"}

        print(
            "🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆃🅷🅴 🅳🅸🅵🅵🅸🅲🆄🅻🆃 🆆🅾🆁🅳 🅲🅷🅴🅲🅺🅴🆁")  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')

        self.checker_start()  # trigger the checker_start method to provide user instructions

    # method checks to ensure correct string is entered by user
    def input_check(self):
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            user_input = input(": ")
            if user_input.lower() == "exit" or user_input.lower() == "help":
                # if input has the keywords exit or help
                self.help_exit_check(user_input)  # call the help_exit_check method to handle keywords
            else:
                break
        return user_input  # return the correct input, storing it in a variable

    # method checks user input for "exit" or "help" keywords, providing descriptive feedback
    def help_exit_check(self, user_input):
        if user_input.lower() == "exit":
            self.is_running = False  # statement breaks input while loops
        elif user_input.lower() == "help":  # if/else statement controls tailored help messages
            print("\nYou are in the spell checker! Type in the sentence you would like to have checked")
        else:
            print("\nPlease try typing in the sentence again 👍")

    # method searches the sentence for a word, and replaces it with the correct word
    def word_swap(self, sentence):
        no_swap = True  # variable used to signal if the input sentence changes
        modified_word = ""  # variable holds the new replacement word
        original_word = ""  # variable holds the original wrong word
        # iterate over the dictionary using a for loop, checking for words which match and replacing them if found
        for key, replacement in self.words_to_check.items():
            # the replace function is a simple way of editing the sentence. It parses the string and finds any matches
            # if found, the key is replaced by its value
            new_sentence = sentence.replace(key, replacement)
            if new_sentence != sentence:  # if the new sentence is different to the original its been modified
                no_swap = False
                sentence = new_sentence  # set the sentence to equal the modified sentence
                modified_word = replacement
                original_word = key
                # get the word which was modified and store it in the variables
        if no_swap:
            print("\nUnable to find any words to swap, well done!")
        else:
            print("\nYou were close, keep up the good work! The correct wording is:")
            print(sentence)
            print("The word which can be changed is " + original_word + " for " + modified_word)

    # method is used to start the application, and guide the user through
    def checker_start(self):
        while self.is_running:  # when this while loop breaks, we return to the main module
            print("\nType in the sentence you want to check for difficult words and have corrected")
            print('**** For this prototype please type "A structure which humans occupy" ****')
            sentence_input = self.input_check()
            if sentence_input.lower() == "exit":  # check for the "exit" keyword.
                print("Goodbye from the difficult word checker!")
                break  # if "exit" found we break the loop, leaving this feature module
            self.word_swap(sentence_input)  # method is called to output corrected sentence to user
