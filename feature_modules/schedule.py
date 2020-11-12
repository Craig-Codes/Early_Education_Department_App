# Class creates the users schedule once instantiated
# User can select a period and edit it to reflect a schedule change

import config  # config module used to store schedule data and gives access to global styling


class Schedule:
    def __init__(self):  # set variables when class initialised
        self.is_running = True  # variable contains program on or off state, always start as True
        self.stage = 1  # variable used to provide tailored help when user requests it

        # schedule is stored as a dictionary. Initially created using arguments from the config.py script
        self.schedule = {"Period 1:": config.schedule[0], "Period 2:": config.schedule[1],
                         "Period 3:": config.schedule[2], "Period 4:": config.schedule[3],
                         "Period 5:": config.schedule[4], "Period 6:": config.schedule[5]}
        self.class_list = config.class_list
        # list of all possible class choices stored in a list - teacher can easily add to the list from config.py

        print("🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆈🅾🆄🆁 🅳🅰🅸🅻🆈 🆂🅲🅷🅴🅳🆄🅻🅴".center(44))  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')

        self.schedule_start()  # call the checker_start method to provide user instructions

    # method is used to start the application, and guide the user through
    def schedule_start(self):
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
            # method updates the global schedule list, used to persist data when schedule module is closed
            self.edit_global(class_input, class_change)

    # method checks to ensure correct string is entered by user - a valid in range integer
    def input_check(self):
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
        return user_input  # return the valid input

    # method checks user input for "exit" or "help" keywords, providing tailored descriptive feedback
    def help_exit_check(self, user_input):
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
        print("\nYour current daily schedule is:", config.Style.bold)  # make all list contents bold
        for key, value in self.schedule.items():  # loop through the keys and values from schedule dictionary
            print(key, value)  # display the key value pairs to the user
        print(config.Style.end, config.Style.purple)  # stop bold style

    # method changes the schedule based on the input period number and subject number
    def edit_schedule(self, period_number, new_class):
        # tuple stores all possible class selections

        # edit the schedule dictionary to reflect users choice
        self.schedule["Period {}:".format(str(period_number))] = self.class_list[new_class - 1]

    # method changes the global schedule list to allow data to persist across modules
    def edit_global(self, period_number, new_class):
        # edit the variable in config.py to allow schedule to save across modules so schedule upto date if re-entered
        config.schedule[period_number - 1] = self.class_list[new_class - 1]  # edit the global list with updated class
