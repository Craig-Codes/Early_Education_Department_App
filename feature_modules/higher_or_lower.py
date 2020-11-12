# Class creates the higher or lower game once instantiated.
# Allows user to input a sentence and get the correctly formatted sentence back

import random  # random module used to generate a random entry from a tuple of numbers
import config  # config module gives access to global styling


class HigherLower:
    def __init__(self):  # set variables when class initialised
        self.is_running = True  # variable contains program on or off state, always start as True
        self.replay = True  # variable used to control if user is asked if they want to retry the game
        self.win_counter = 0  # variable stores number of consecutive wins, 3 in a row is required to win

        self.number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # tuple stores list of all numbers user can choose
        self.random_number = 0  # variable holds a random number which is set when the game starts
        self.second_random_number = 0  # variable holds second generated random number

        print("🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆃🅷🅴 🅷🅸🅶🅷🅴🆁 🅾🆁 🅻🅾🆆🅴🆁 🅶🅰🅼🅴".center(44))  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')
        print("\nThe game is played with numbers between 1 and {} inclusive".format(len(self.number_tuple)))
        # number_tuple length is used to keep feature dynamic, this way we can easily increase the future number range

        self.higher_lower_start()  # trigger the higher_lower_start method to provide user instructions

        # method is used to start the application, and guide the user through
    def higher_lower_start(self):
        while self.is_running:  # when this while loop breaks, we return to the main module
            self.random_number = random.choice(self.number_tuple)  # get a random entry from the number tuple
            print("\n===========================================")  # divide to break up the text between rounds
            print("You have won {} in a row, you need 3 to win!".format(
                self.win_counter))  # let user know current wins
            print("\nThe number is {}".format(
                self.random_number))  # number user needs to guess higher or lower against
            print("\nWill the next number be higher or lower?")
            print("Enter '1' for Higher, and '2' for Lower")
            number_guess = self.input_check()  # method handles the input, checking if valid and for keywords help/exit
            if number_guess == "exit":  # check for the "exit" keyword.
                print("Goodbye from the higher or lower game! \U0000263B")
                self.replay = False  # ensure user doesnt get asked to replay quiz at the end
                break  # if "exit" found we break the loop, leaving this feature module
            self.higher_or_lower_check(
                number_guess)  # if input is valid and not a keyword, method checks if user wins
            if self.win_counter == 3:  # variable incremented each time user wins a game, if three in a row, game ends
                print(config.Style.bold, "*** Well done you have won 3 times in a row, and beaten the game! ***",
                      config.Style.end, config.Style.purple)  # winning message in bold
                break  # exits the game after declaring the user a winner for winning 3 times in a row
        #  ask user if they want to play again- if yes game state is reset, if no, game exits
        self.replay_check()

    # method checks to ensure correct string is entered by user - a valid in range integer
    def input_check(self):
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            user_input = input(": ")
            try:
                user_input = int(user_input)  # if input is a number, then its valid
                if user_input in self.number_tuple:  # tuple storing all possible correct number inputs
                    break  # valid input between 1 and 10, break the loop returning the user_input
                else:
                    print("Please enter a number between 1 and {} 👍".format(len(self.number_tuple)))
                    # error message to user - using number_tuple length to allow for number range to change if required
            except ValueError:  # if input isn't a number then its "help" / "exit" or a typo
                self.help_exit_check(user_input)  # help_exit_check function checks the input, looking for keywords
                user_input = user_input.lower()  # need to remove case sensitivity for exit check in the start method
        return user_input  # return the valid input

    # method checks user input for "exit" or "help" keywords, providing descriptive feedback
    def help_exit_check(self, user_input):
        if user_input.lower() == "exit":
            self.replay = False  # ensure user doesnt get asked to replay quiz at the end
            self.is_running = False  # statement breaks input while loops
        elif user_input.lower() == "help":  # if/else statement controls tailored help messages
            print("\nYou are in the higher or lower game! Type in '1' to guess higher or '2' to guess lower")
            print("The current number is {}".format(self.random_number))
        else:
            print("\nSomething went wrong, please try typing in the number again 👍")

    # method takes in the users guess of higher or lower, and compares it to the current random number
    def higher_or_lower_check(self, user_guess):
        # generate a second random number to see if it was higher or lower than the first
        self.second_random_number = random.choice(self.number_tuple)
        print("\nThe second number is {}".format(self.second_random_number))
        if user_guess == 1:  # user chose higher
            if self.random_number < self.second_random_number:
                print("The number was higher, you win!\n")
                self.win_counter += 1  # increment the win counter
            elif self.random_number == self.second_random_number:
                # if the numbers are the same, nothing happens to the win counter
                print("The number was equal, That's a tie!")
            else:
                print("The number was lower, you lose this time!\n")
                self.win_counter = 0  # reset the win counter back to zero
        elif user_guess == 2:  # user chose lower
            if self.random_number > self.second_random_number:
                print("The number was lower, you win!\n")
                self.win_counter += 1
            elif self.random_number == self.second_random_number:
                print("The number was equal, That's a tie!")
            else:
                print("The number was higher, you lose this time!\n")
                self.win_counter = 0  # reset the win counter back to zero

    # method checks to see if user wants to replay the game after its finished
    def replay_check(self):
        while self.replay:
            print("\nWould you like to play again?")
            replay = input("Enter '1' for yes, '2' for no: ")
            if replay == "1":
                # if user wants to restart we need to reset game state and restart
                self.win_counter = 0  # reset win counter back to zero
                self.is_running = True  # re-enter the start loop
                self.higher_lower_start()  # restart the game
            elif replay == "2" or replay.lower() == "exit":  # user wants to leave the game
                print("Goodbye from the higher or lower game! \U0000263B")
                self.replay = False  # ensure user doesnt get asked to replay quiz at the end
                # leaving the method will cause the script to end and put the user back to the main menu
            elif replay.lower() == "help":
                print("\nYou are in the higher or lower game! Type in '1' to play again, or '2' to exit the game")