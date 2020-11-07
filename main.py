# Main.py contains the menu system and controls overall application state, calling in feature modules when required

# from feature_modules import styles  # import the styles module for font manipulation
import config  # config/py holds global variables which can be edited and shared across modules


# class contains the menu and all of the methods necessary to prompt user and open the applications features
class Menu:
    def __init__(self):
        self.program_state = "menu"  # variable contains which feature is open and in use
        self.features = ("1. Calculator", "2. Daily Schedule", "3. Difficult Word Checker", "4. Higher or Lower",
                         "5. Hangman", "6. Quiz", "7. Notes")  # tuple containing all features
        self.text_color = config.Style.purple  # variable contains the menus text colour

    # method provides the starting instructions to the user
    def menu_start(self):
        # Unicode characters used to make heading more interesting to children
        print(self.text_color + config.Style.bold + config.Style.underline + "\n" +
              "⟆𝜏Ꭿ⨍⨍𝖮ᖇᖱ⟆Ꮒ⫯ᖇ∈ ⋃ﬡ⫯ᨆ∈ᖇ⟆⫯𝜏Ⴘ ᕮᎯᖇ𝘭Ⴘ ᕮᕍυ⊂Ꭿ𝜏⫯𝖮ﬡ ↁ∈ᖰᎯᖇ𝜏ⲙ∈ﬡ𝜏".center(80) + config.Style.end)
        print(self.text_color + "\nPlease use this application to help with your day to day school tasks "
              + "\U0001F3EB")  # unicode school symbol used to add visual interest
        print('If at any time you need guidance on how to use this application, just type "help"')
        print('If you want to leave the application just type "exit"')

    # method starts a loop to get the user to select a feature
    def menu_display(self):
        while self.program_state == "menu":  # while program state is "menu", keep looping until user chooses a feature
            print('\nChoose an activity from the bellow list by typing in its number:' + config.Style.bold)
            print(*self.features, sep="\n")  # use * to remove parenthesis and separate by new line
            self.program_state = str(input(config.Style.end + self.text_color + "\nEnter choice (1 - 7): "))
            print(config.Style.end + self.text_color)  # remove bold and reset colour

            # if program_state is not a valid feature number
            if self.program_state in ("1", "2", "3", "4", "5", "6", "7"):
                self.open_module(self.program_state)  # method opens the correct feature module for user
            else:
                self.help_exit_check(self.program_state)  # check to see if input was "help", "exit" or a typo

    # method handles input errors, "exit" and "help" input
    def help_exit_check(self, user_input):
        self.program_state = "menu"
        if user_input.lower() == "exit":
            print("Have a great day! \U0000263B")
            exit()  # quit the application
        elif user_input.lower() == "help":  # if/else statement controls tailored help messages
            print("You are currently in the application menu. To enter an activity type its number")
        else:
            print("Try typing in the activity number again \U0001F44D")

    # method controls the importing and opening of different app modules to give user access to feature modules
    def open_module(self, module):
        self.program_state = module.lower()
        if self.program_state == "1":
            # import the calculator module and start it - only importing what we need when we need it
            from feature_modules import calculator
            # create a new instance of the calculator (enter the calculator.py script) - pass in the config.py
            # memory value as a starting value, which is then updated throughout the session
            calculator.Calculator(config.memory_value)
        elif self.program_state == "2":
            # import the daily schedule module and start it - only importing what we need when we need it
            from feature_modules import schedule
            # create a new instance of the schedule (enter the schedule.py script), using global variables from the
            # config.py script to share data
            schedule.Schedule(config.schedule[0], config.schedule[1], config.schedule[2], config.schedule[3],
                              config.schedule[4], config.schedule[5])
        elif self.program_state == "3":
            # import the spell checker module and start it
            from feature_modules import spell_checker
            spell_checker.Checker()  # create a new instance of the hangman game (enter hangman.py script)
        elif self.program_state == "4":
            # import the higher_or_lower module and start it
            from feature_modules import higher_or_lower
            # create a new instance of the higher or lower game (enter higher_or_lower.py script)
            higher_or_lower.HigherLower()
        elif self.program_state == "5":
            # import the hangman module and start it
            from feature_modules import hangman
            # create a new instance of the hangman game (enter hangman.py script) - use the word_list as an argument
            hangman.Hangman(config.hangman_word_list)
        elif self.program_state == "6":
            # import the hangman module and start it
            from feature_modules import quiz
            # create a new instance of the quiz (enter quiz.py script) - pass in arguments form config.py
            quiz.Quiz(config.maths_questions, config.maths_answers, config.maths_correct_answers,
                      config.history_questions, config.history_answers, config.history_correct_answers,
                      config.geography_questions, config.geography_answers, config.geography_correct_answers)
        elif self.program_state == "7":
            # import the hangman module and start it
            from feature_modules import hangman
            # create a new instance of the hangman game (enter hangman.py script) - use the word_list as an argument
            hangman.Hangman(config.hangman_word_list)
        self.program_state = "menu"  # once finished in module return to the menu keeping the while loop going


menu = Menu()  # create a new instance of Menu
menu.menu_start()  # show one off start up text and instructions
menu.menu_display()  # show the list of features to the user and ask them to select one
