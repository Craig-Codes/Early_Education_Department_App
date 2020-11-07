# Class creates the Notes feature once instantiated
# Allows user to create and edit notes to use to help throughout the day

import textwrap  # textwrap module is used to nicely wrap long text to multiple lines
import config  # config module used to store note data and gives access to global styling


class Notes:

    # when class is instantiated, set the following variable values and run the notes feature
    def __init__(self, notes):
        self.is_running = True  # variable controls the start loop and keeps user in the notes feature
        self.notes = notes
        print("\n🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🅽🅾🆃🅴🆂")  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')

        # stage is used to determine which input stage calculator is on,
        self.stage = 1   # required for the "help" functionality and memory functions
        self.notes_start()  # start the calculator

    # Method starts off the notes feature, requesting user input
    def notes_start(self):
        #while self.is_running:  # when while loop breaks, we return to the main module
        print("\nCurrent saved notes:")
        self.output_notes()
            #self.first_input = self.input_check()
            # input_check method checks for numbers, keywords and memory functions
           #self.stage = 1  # get the first number input
           # if self.first_input == "exit":  # if input_check method returns "exit", break the loop returning to menu
               # print("Goodbye from the calculator!")
               # break

            #self.stage = 2  # get the operator
            #print("Type an operator ( plus(+), minus(-), multiply(*), divide(/))")
            #self.operator = self.operator_check()
            # operator_check method checks for operators, keywords and memory functions
            #if self.operator.lower() == "exit":
               # print("Goodbye from the calculator!")
               # break

           # self.stage = 3  # get the second number input
            #print("Type the second number of your calculation")
            #self.second_input = self.input_check()
            #if self.second_input == "exit":
               # print("Goodbye from the calculator!")
               # break

    # method neatly outputs all of the notes to the user
    def output_notes(self):
        for title, note in self.notes.items():
            title_string = title  # variable holds the title string
            note_length = len(note)  # get the length of the note text
            print(config.Style.bold, config.Style.underline)  # make title bold and underlined
            print("Title:", title_string)
            print(config.Style.end, config.Style.purple)
            if note_length > 100:  # check to see if note content is longer than 100 character
                # if longer than 100 characters we want to line break so that the notes look nice in the console
                print(textwrap.fill(note, 100))  # wrap the note every 100 characters to a new line
                print("-" * 100)  # draw a divide to differentiate between the different notes
            else:
                print(note)  # print the note
                print("-" * note_length)  # draw a divide to differentiate between the different notes


    # method sanitises the user input, checking to see if it's a number
    def input_check(self):
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            user_input = input(": ")
            try:  # if input is a number, then its valid
                user_input = float(user_input)
                break  # leave the while loop as valid input
            except ValueError:  # if input isn't a number then its help / exit or typo
                self.help_exit_check(user_input)  # method checks for keywords and memory functions
        return user_input  # return the value to store in input variable


    # method saves the memory value into the config.py file
    def memory_save(self):
        config.memory_value = self.memory_value  # memory_value variable in config.py given current memory value