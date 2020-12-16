# Class creates the calculator once instantiated
# Allows user to calculate maths problems ( +, -, /, *), along with the storage and retrieval of a memory value

import config  # config module used to store calculator memory data and gives access to global styling


class Calculator:
    """ Class creates the calculator, allowing for basic calculations along with memory features"""

    # when class is instantiated, set the following variable values and run the calculator
    def __init__(self):
        self.is_running = True  # variable controls the start loop and keeps user in the calculator until exit keyword
        print("🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆃🅷🅴 🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁 \U0001F5A9".center(60))  # give user starting instructions
        # UNICODE Icon is used to draw a calculator to add visual interest for children
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')
        print('To get information about the memory functions type "memory" at any time')

        self.first_input = None  # variable used to store the first half of the users sum
        self.second_input = None  # variable used to store the second half of the users sum
        self.operator = None  # variable used to store the users chosen operator (+, =, /, *)
        self.total = None  # variable used to store the sums total
        # stage is used to determine which input stage calculator is on,
        self.stage = 1   # required for the "help" functionality and memory functions
        self.memory_value = config.memory_value  # get the current memory value from config.py on instantiation
        self.calculator_start()  # start the calculator

    # Method starts off the calculator, requesting user inputs
    def calculator_start(self):
        """ method starts the calculator, requesting user inputs to form a valid sum """
        while self.is_running:  # when while loop breaks, we return to the main module
            print("\nType the first number of your calculation")
            self.first_input = self.input_check()
            # input_check method checks for numbers, keywords and memory functions
            self.stage = 1  # get the first number input
            if self.first_input == "exit":  # if input_check method returns "exit", break the loop returning to menu
                print("Goodbye from the calculator! \U0000263B")
                break

            self.stage = 2  # get the operator
            print("Type an operator - plus(+), minus(-), multiply(*) or divide(/)")
            self.operator = self.operator_check()
            # operator_check method checks for operators, keywords and memory functions
            if self.operator.lower() == "exit":
                print("Goodbye from the calculator! \U0000263B")
                break

            self.stage = 3  # get the second number input
            print("Type the second number of your calculation")
            self.second_input = self.input_check()
            if self.second_input == "exit":
                print("Goodbye from the calculator! \U0000263B")
                break

            self.stage = 4  # calculate the answer
            self.total = self.calculate()  # calculate the inputs
            if self.total == "impossible":  # check to avoid divide by zero runtime error
                print("Cannot divide by zero, try another sum")
                continue  # go back to the start of the run loop

            # output the whole sum to the user, the int_check method is used to remove unnecessary decimal points
            print(config.Style.bold + "\n{} {} {} = {}"
                  .format(self.int_check(self.first_input), self.operator, self.int_check(self.second_input),
                          self.int_check(self.total)) + config.Style.end, config.Style.purple)

    # method sanitises the user input, checking to see if it's a number
    def input_check(self):
        """ Method handles the user input ensuring its valid """
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            user_input = input(": ")
            try:  # if input is a number, then its valid
                user_input = float(user_input)
                break  # leave the while loop as valid input
            except ValueError:  # if input isn't a number then its help / exit or typo
                self.help_exit_check(user_input)  # method checks for keywords and memory functions
                user_input = user_input.lower()  # ensure we return the string in lowercase to remove case sensitivity
        return user_input  # return the value to store in input variable

    # method sanitises the user input, checking to make sure it's an operator
    def operator_check(self):
        """ Method handles the user operator input ensuring its valid """
        user_input = ""  # ensure user_input is cleared
        possible_operators = ('+', '-', '*', '/')  # tuple holding the operators
        while self.is_running:  # while loop ensures user gives a valid input
            user_input = input(": ")
            if user_input in possible_operators:  # check to see if user input is a valid operator
                break  # leave the while loop as valid input
            else:  # if no valid operator found, check for keywords or memory functions
                self.help_exit_check(user_input)
                user_input = user_input.lower()  # ensure we return the string in lowercase to remove case sensitivity
        return user_input  # return the value to store in operator variable

    # Method checks to see if user has input "help" or "exit"
    def help_exit_check(self, user_input):
        """ Handles the user input, checking for exit and help keywords. Exit quits app, help provides instructions """
        if user_input.lower() == "exit":
            self.is_running = False  # statement breaks input while loops, causing calculator to exit to main menu
        elif user_input.lower() == "help":  # if/else statement controls tailored help messages
            if self.stage == 1:
                print("You are in the calculator! Type in the first number of your calculation")
            elif self.stage == 2:
                print("You are in the calculator! Type an operator (plus(+), minus(-), multiply(*), divide(/))")
            elif self.stage == 3:
                print("You are in the calculator! Type the second number of your calculation")
            elif self.stage == 4:
                print("You are in the calculator! Type in the first number of your calculation")
        elif user_input.lower() == "memory":  # provide the user instructions on how to use memory functions
            print("Type 'm+' to add the last input number to the memory")
            print("Type 'm-' to minus the last input number from the memory")
            print("Type 'mr' to recall the memory number")
            print("Type 'mc' to clear the memory number")

        # if user passes in a memory function pass input to the memory_functions method
        elif user_input == "m+" or user_input == "m-" \
                or user_input == "mr" or user_input == "mc":
            self.memory_functions(user_input)  # pass the user input into the memory_functions method
        else:
            print("Please try typing an input again, type 'help' for tailored assistance 👍")

    # method does the maths on the two given inputs and the operator
    def calculate(self):
        """ Method carries out calculations on the valid user inputs """
        if self.operator == "+":
            return self.first_input + self.second_input
        elif self.operator == "-":
            return self.first_input - self.second_input
        elif self.operator == "/":
            # validation check to avoid runtime error when dividing by zero
            if self.second_input == 0:  # dividing by zero causes an error in python
                return "impossible"  # flag used to detect an error
            else:
                return self.first_input / self.second_input
        elif self.operator == "*":
            return self.first_input * self.second_input

    # method checks to see if float value can be converted into an integer to remove the decimal places
    def int_check(self, total):
        """ Method checks to see if argument can be turned into an integer to remove unnecessary decimal places """
        if total.is_integer():  # check to see if input can be cast to int datatype
            return int(total)
        else:
            return total

    # method checks to see which memory functionality the user requires, and implements it
    def memory_functions(self, memory_key):
        """ Method takes in valid user input string as an argument, using it to perform a memory function """
        if memory_key == "m+":  # add last input to memory value
            if self.stage == 1:  # no input has been added yet, so simply add zero to memory
                self.memory_value += 0
            elif self.stage == 2 or self.stage == 3:  # first input has a value, add it to the current memory
                self.memory_value += float(self.first_input)
            elif self.stage == 4:
                self.memory_value += float(self.second_input)
            self.memory_save()  # method saves updated memory value into config.py file
        elif memory_key == "m-":  # take last input from memory value
            if self.stage == 1:  # no input has been added yet, so simply add zero to memory
                self.memory_value -= 0
            elif self.stage == 2 or self.stage == 3:  # first input has a value, add it to the current memory
                self.memory_value -= float(self.first_input)
            elif self.stage == 4:
                self.memory_value -= float(self.second_input)
            self.memory_save()  # method saves updated memory value into config.py file
        elif memory_key == "mr":  # recall and display current memory value
            self.memory_value = float(self.memory_value)  # ensure memory_value is a float
            self.memory_value = self.int_check(self.memory_value)  # check to see if we can remove decimal places
            memory_value_length = len(str(self.memory_value))
            # get the length of the memory value - used to create neat boundaries matching memory output length
            print("\n-------------------------" + memory_value_length * "-")
            print("Current memory value is: {}".format(self.memory_value))
            print("-------------------------" + memory_value_length * "-" + "\n")
        elif memory_key == "mc":  # clear memory value back to zero
            self.memory_value = 0
            self.memory_save()  # method saves updated memory value into config.py file

    # method saves the memory value into the config.py file
    def memory_save(self):
        """ Method saves the memory value to the config.py file """
        config.memory_value = self.memory_value  # memory_value variable in config.py given current memory value
        # this allows the memory value to be correct if calculator is re-entered
