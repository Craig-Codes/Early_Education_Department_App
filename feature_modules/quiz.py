# Class creates a quiz once instantiated
# Allows user to select a subject to take a quiz on, then provides five randomly ordered questions and a score

import random  # import the random module - used to randomise question order to increase replay value


class Quiz:
    # set variables when class initialised, taking arguments from the config.py file, via main.py
    def __init__(self, maths_questions, maths_answers, maths_correct,
                 history_questions, history_answers, history_correct,
                 geo_questions, geo_answers, geo_correct):

        self.is_running = True  # variable contains program on or off state, always start as True
        self.stage = 1  # stage is used to determine which input stage quiz is on, for the 'help' functionality

        # arrays store the input from the config.py file, allowing the quiz to be easily modified and updated
        self.question_bank_maths = maths_questions
        self.answer_bank_maths = maths_answers
        self.correct_maths = maths_correct

        self.question_bank_history = history_questions
        self.answer_bank_history = history_answers
        self.correct_history = history_correct

        self.question_bank_geography = geo_questions
        self.answer_bank_geography = geo_answers
        self.correct_geography = geo_correct

        self.current_question_bank = []  # empty placeholder array used to store questions
        self.current_answer_bank = []  # empty placeholder array used to store answers
        self.current_correct = []  # empty placeholder array used to store answers

        self.score_counter = 0  # variable stores number of correct answers
        self.questions_taken = 0  # variable stores number of questions user has attempted

        print("\n🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆃🅷🅴 🆁🅴🆅🅸🆂🅸🅾🅽 🆀🆄🅸🆉")  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')
        print("\nThe quiz covers topics you are currently learning in school.")

        self.quiz_start()  # trigger the quiz_start method to provide user instructions

    # method is used to start the quiz, guiding the user throughout
    def quiz_start(self):
        while self.is_running:  # when this while loop breaks, we return to the main module
            self.stage = 1  # stage 1 is the setup stage - user must choose the subject to take the quiz about
            print("\nSelect the subject you would like to take a quiz about?")
            print("Type '1' for Maths, '2' for History, or '3' for Geography")
            quiz_selection = self.input_check()  # input_check method checks for keywords and ensures correct user input
            if quiz_selection == "exit":  # check for the "exit" keyword.
                print("Goodbye from the quiz! \U0000263B")
                break  # if "exit" found we break the loop, leaving this feature module

            self.stage = 2  # stage 2 is the quiz stage
            self.quiz_builder(quiz_selection)  # method builds the quiz based on subject user selected

            # while loop is used to keep the quiz going until the user completes all of the questions in a random order
            while len(self.current_question_bank) > 0:  # while we still have questions in the question bank
                # get a random number between 0 and question_bank length - allows for dynamic question numbers
                random_number = random.randrange(0, len(self.current_question_bank))
                self.question(random_number)  # get a random question from the question bank
                question_answer = self.input_check()  # method used to get users question answer and check for keywords
                if question_answer == "exit":  # check for the "exit" keyword.
                    print("Goodbye from the quiz! \U0000263B")
                    break  # if "exit" found we break the loop, leaving this feature module
                self.answer_check(random_number, question_answer)  # increment to score if correct
                # remove question from arrays before we then fetch another random question
                self.question_remove(random_number)
                print("\n==============================================")  # divide to break up the text between rounds
                self.completed_check()   # check to see if the quiz has finished rather than simply been exited
        self.replay_check()  # if user wants to play again, properties are reset and quiz restarts

    # method populates the current question, answer and correct arrays
    def quiz_builder(self, subject_selection):
        if subject_selection == "1":
            # make copies of the current arrays so that we can mutate the data without effecting the originals
            self.current_question_bank = self.question_bank_maths.copy()
            self.current_answer_bank = self.answer_bank_maths.copy()
            self.current_correct = self.correct_maths.copy()
        elif subject_selection == "2":
            self.current_question_bank = self.question_bank_history.copy()
            self.current_answer_bank = self.answer_bank_history.copy()
            self.current_correct = self.correct_history.copy()
        elif subject_selection == "3":
            self.current_question_bank = self.question_bank_geography.copy()
            self.current_answer_bank = self.answer_bank_geography.copy()
            self.current_correct = self.correct_geography.copy()

    # method outputs the question and possible answers to the user
    def question(self, random_number):
        print("\n")
        print(*self.current_question_bank[random_number])  # print question without brackets
        for answer in self.current_answer_bank[random_number]:
            print(*answer)

    # method checks to see if user got the question right, incrementing to the counter if so
    def answer_check(self, random_number, user_answer):
        self.questions_taken += 1  # increment the number of questions the user has attempted
        # if the users answer is the answer in the current_correct array for the current random number slot
        if user_answer in self.current_correct[random_number]:
            self.score_counter += 1  # increment the score counter
            print("\nWell done you were correct! Your score is {}/{}".format(self.score_counter, self.questions_taken))
        else:
            print("\nThe correct answer was answer {}. keep practicing to improve your score!"
                  .format(*self.current_correct[random_number]))
            print("Your score is {}/{}".format(self.score_counter, self.questions_taken))

    # method removes the random question from all of the associated current arrays so that its doesnt appear again
    def question_remove(self, question_number):
        del self.current_question_bank[question_number]  # delete question from array using its index position
        del self.current_answer_bank[question_number]
        del self.current_correct[question_number]

    # method checks to ensure correct string is entered by user
    def input_check(self):
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            if self.stage == 1:  # if user is at quiz selection
                user_input = input(": ")
                if user_input.lower() == "exit":
                    self.is_running = False  # statement breaks input while loops
                    user_input = user_input.lower()  # .lower ensures the input is returned in correct format
                elif user_input.lower() == "help":  # if/else statement controls tailored help messages
                    print("\nYou are in the revision quiz! type in a number to choose the quiz topic")
                elif user_input == "1" or user_input == "2" or user_input == "3":
                    break
                else:  # user didnt enter "help" or "exit" but put in more than one letter
                    print("\nPlease try again, type '1' for Maths, '2' for History and '3' for Geography 👍")
            elif self.stage == 2:  # if user is at answer input
                user_input = input("\nEnter your answer (1-4): ")
                if user_input.lower() == "exit":
                    self.is_running = False  # statement breaks input while loops
                    user_input = user_input.lower()  # .lower ensures the input is returned in correct format
                elif user_input.lower() == "help":  # if/else statement controls tailored help messages
                    print("\nYou are in the revision quiz! Choose your answer by typing its number (1-4)")
                elif user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4":
                    break
                else:  # user didnt enter "help" or "exit" but put in more than one letter
                    print("\nPlease try again, type the number of the answer you wish to enter between 1 - 4 👍")
        return user_input  # return the valid input

    # method checks to see if a user has answered 5 questions, breaking the is_running while loop if so
    def completed_check(self):
        if len(self.current_question_bank) == 0:
            print("\nWell done for taking the quiz!")
            print("***** Your score is {}/{} *****".format(self.score_counter, self.questions_taken))
            self.is_running = False  # break out of the start loop

    # method checks to see if user wants to replay the game after its finished
    def replay_check(self):
        replay_check = True
        while replay_check:
            print("\nWould you like to play again?")
            replay = str(input("Enter '1' for yes, '2' for no: "))
            if replay == "1":  # if user wants to restart we need to reset game state and restart
                self.score_counter = 0  # reset score counter back to zero
                self.questions_taken = 0  # reset question counter back to zero
                self.is_running = True  # re-enter the start loop
                self.quiz_start()  # restart the game
            elif replay == "2" or replay.lower() == "exit":  # user wants to leave the game
                print("Goodbye from the quiz! \U0000263B")
                # leaving the method will cause the script to end and put the user back to the main menu
                replay_check = False
            elif replay.lower() == "help":
                print("\nYou are in the revision quiz! Type in '1' to try again, or '2' to exit the quiz")
