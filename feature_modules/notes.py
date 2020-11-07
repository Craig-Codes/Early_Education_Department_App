# Class creates the Notes feature once instantiated

# Allows user to create and edit notes to use to help throughout the day
# The memory value is stored in the config.py file so that notes persists during the applications entire session


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
        while self.is_running:  # when while loop breaks, we return to the main module
            print("\nType the first number of your calculation")
            print(self.notes)
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
        import sys
        # use sys module to add ".." in front of module import file path allowing import from parent directory
        sys.path.append("..")
        # sys.path gives access to the PYTHONPATH set in the current system. ".." goes up one directory
        import config  # config imported from ../config.py due to sys.path.append("..")
        config.memory_value = self.memory_value  # memory_value variable in config.py given current memory value