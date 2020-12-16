# Class creates the users schedule once instantiated
# User can select a period and edit it to reflect a schedule change

import os  # operating system module used to easily interact with the file structure
import config  # config module gives access to global styling


class Schedule:
    """ Class creates the schedule, allowing for users to view and edit their daily schedule """

    def __init__(self):  # set variables when class initialised
        self.is_running = True  # variable contains program on or off state, always start as True
        self.stage = 1  # variable used to provide tailored help when user requests it

        self.schedule = {}  # schedule is stored as a dictionary populated from the data inside the schedule.txt file

        self.class_list = ["Maths", "Science", "History", "Geography", "Art", "PE", "English", "Free Period"]
        # list of all possible class choices stored in a list

        print("🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆈🅾🆄🆁 🅳🅰🅸🅻🆈 🆂🅲🅷🅴🅳🆄🅻🅴".center(44))  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')

        self.import_schedule()  # call method to retrieve the saved schedule from the schedule.txt file
        self.schedule_start()  # call the checker_start method to provide user instructions

    # method imports the schedule from a text file - creates a dynamically sized dictionary based on number of lines
    # found in the schedule.txt file. Allows for flexibility if day is longer or shorted etc
    def import_schedule(self):
        """ method reads the schedule.txt file, adding values found to the schedule dictionary """
        schedule_list = []  # list to hold all found lines inside the schedule.txt file

        # os.path.join allows the given file path to work on windows, linux and mac systems
        # Windows systems use '\' between directories, but linux and mac use '/'. os.path.join automatically
        # works this out based on the users operating system, generating the correct file path
        file = os.path.join("data", "schedule.txt")  # notes.txt is the file we want to read from the data directory

        with open(file, "r") as file:  # using 'with' automatically closes the file once method has finished
            for line in file:  # loop through found lines
                schedule_list.append(line.strip())  # loop through each line in the file, and add it to the list.

            # dynamically update the schedule dictionary based on text file data
            for index, subject in enumerate(schedule_list):  # loop through schedule list, pulling out index and data
                self.schedule["Period {}:".format(index + 1)] = subject  # assign each list entry to dictionary

    # method is used to start the application, and guide the user through
    def schedule_start(self):
        """ method starts the schedule editor, requesting user inputs to change the current schedule """
        while self.is_running:  # when this while loop breaks, we return to the main module
            self.current_schedule_print()  # method displays the current schedule to the user
            self.stage = 1  # currently in stage 1 for user help feedback
            print("Type in the number of the period you want to edit (1-{})".format(len(self.schedule)))
            #  length of self.schedule dictionary is used so that more or less periods could be added or removed and
            #  this value is updated dynamically rather than editing a static number
            class_input = self.input_check()  # method ensures we get a valid input, dealing with keywords and errors
            if class_input == "exit":
                print("Goodbye from the daily schedule! \U0000263B")
                break  # breaks the while loop, leaving the module and returning to the main menu

            self.stage = 2  # now in stage 2 for user help feedback
            print("\nType in the number of the subject to add it to the selected period:")
            # create dynamic list of number of school subjects - so that more can be added without breaking feature
            number_of_subjects_list = list(range(1, (len(self.class_list) + 1)))
            # create a new list from 1 to class_list length + 1, giving us all possible options
            # zip list of subjects with list of subject numbers, printing out each subject and its number
            for number, subject in zip(number_of_subjects_list, self.class_list):
                print("{}. {}".format(number, subject))

            class_change = self.input_check()  # method ensures we get a valid input, dealing with keywords and errors
            if class_change == "exit":
                print("Goodbye from the daily schedule! \U0000263B")
                break  # breaks the while loop, leaving the module and returning to the main menu
            # method takes in the selected period and chosen subject, amending the schedule accordingly
            self.edit_schedule(class_input, class_change)

        self.save_schedule()  # save the schedule before exiting the feature module

    # method checks to ensure correct string is entered by user - a valid in range integer
    def input_check(self):
        """ Method handles the user input ensuring its valid """
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            user_input = input(": ")
            try:
                user_input = int(user_input)  # if input is a number, then its valid
                if self.stage == 1:  # stage one is period selection, a choice of 6 integers
                    period_number = len(self.schedule) + 1
                    # get number of periods add 1 so that all note numbers are included
                    # dynamic allowing for different period numbers on different days / terms
                    period_number_tuple = tuple(range(1, period_number))  # create a new tuple from 1 to period_number
                    if user_input in period_number_tuple:  # if user input is a valid period defined in the tuple
                        break  # leave the while loop as valid expected input
                    else:
                        print("Please enter a number between 1 and {} 👍".format(len(self.schedule)))  # error message
                elif self.stage == 2:  # stage two is class selection, a choice of 8 integers
                    class_number = len(self.class_list) + 1
                    # get number of possible classes, add 1 so that all class numbers are included
                    # dynamic allowing for different class types to be added to the feature module
                    class_number_tuple = tuple(range(1, class_number))  # create a new tuple from 1 to class_number
                    if user_input in class_number_tuple:
                        break
                    else:
                        print("Please enter a number between 1 and {} 👍".format(len(self.class_list)))
            except ValueError:  # if input isn't a number then its "help" / "exit" or a typo
                self.help_exit_check(user_input)  # help_exit_check function checks the input, looking for keywords
                user_input = user_input.lower()  # ensure we return the string in lowercase to remove case sensitivity
        return user_input  # return the valid input

    # method checks user input for "exit" or "help" keywords, providing tailored descriptive feedback
    def help_exit_check(self, user_input):
        """ Handles the user input, checking for exit and help keywords. Exit quits app, help provides instructions """
        if user_input.lower() == "exit":
            self.is_running = False  # statement breaks input while loops, allowing user to return to main menu
        elif user_input.lower() == "help":  # if/else statement controls tailored help messages
            if self.stage == 1:
                print("\nYou are in the daily schedule! Type in the number of the period you would like to edit (1-{})"
                      .format(len(self.schedule)))
            elif self.stage == 2:
                print("\nYou are in the daily schedule! Type in the number of the class you would like to change "
                      "your current period selection to (1-{})".format(len(self.class_list)))
        else:
            print("\nPlease try typing in a number again 👍")  # generic error for a typo

    # method prints the current schedule to the user
    def current_schedule_print(self):
        """ Method prints the current schedule to to display allowing users to see it """
        print("\nYour current daily schedule is:", config.Style.bold)  # make all list contents bold
        for key, value in self.schedule.items():  # loop through the keys and values from schedule dictionary
            print(key, value)  # display the key value pairs to the user
        print(config.Style.end, config.Style.purple)  # stop bold style

    # method changes the schedule based on the input period number and subject number
    def edit_schedule(self, period_number, new_class):
        """ Method takes in the chosen period number and the new class, updating the schedule dictionary"""
        # edit the schedule dictionary to reflect users choice
        self.schedule["Period {}:".format(str(period_number))] = self.class_list[new_class - 1]

    # method updates the schedule.txt file with the current schedule
    # provides persistent data across sessions so users data is always saved and retrievable
    def save_schedule(self):
        """ Method saves the users current schedule to the schedule.txt file """
        file = os.path.join("data", "schedule.txt")  # schedule.txt is the file we want to write from the data directory
        updated_schedule = open(file, 'w')  # open schedule.txt file in write mode
        for period, lesson in self.schedule.items():  # loop through each value in the schedule
            updated_schedule.write(lesson + "\n")  # write each lesson to the schedule.txt file
        updated_schedule.close()  # close the file as we are done writing to it
