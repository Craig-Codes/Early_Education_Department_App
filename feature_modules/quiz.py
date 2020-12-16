# Class creates a quiz once instantiated
# Allows user to select a subject to take a quiz on, then provides five randomly ordered questions and a score

from random import randrange  # random module used to generate a random number from a range of numbers. From is used
# as we only need the randrange function from the random module. We can also now refer to the choice function as
# .randrange() not random.randrange(), allowing code to be more concise
import config  # config module used to get question data and gives access to global styling

# quiz questions and answers -  add questions and answers here to expand the quiz
maths_questions = [["What is the sum of 2 x 2?"],
                   ["What is the sum of 3 + 3?"],
                   ["What is the sum of 23 - 3?"],
                   ["What is the sum of 10 / 2?"],
                   ["How many tens are in 32?"]]

maths_answers = [[["1. 4"], ["2. 5"], ["3. 6"], ["4. 12"]],
                 [["1. 3"], ["2. 6"], ["3. 9"], ["4. 12"]],
                 [["1. 18"], ["2. 19"], ["3. 20"], ["4. 21"]],
                 [["1. 1"], ["2. 2"], ["3. 4"], ["4. 5"]],
                 [["1. 1"], ["2. 2"], ["3. 3"], ["4. 30"]]]

maths_correct_answers = [["1"],
                         ["2"],
                         ["3"],
                         ["4"],
                         ["3"]]

history_questions = [["What type of flower is worn on Remembrance Day in Britain?"],
                     ["How many wives did King Henry VIII have?"],
                     ["What year did World War 2 begin?"],
                     ["Julius Caesar was the leader of which army?"],
                     ["What country did William the Conqueror come from?"]]

history_answers = [[["1. Rose"], ["2. Lily"], ["3. Orchid"], ["4. Poppy"]],
                   [["1. 2"], ["2. 4"], ["3. 6"], ["4. 8"]],
                   [["1. 1914"], ["2. 1918"], ["3. 1939"], ["4. 1945"]],
                   [["1. Roman"], ["2. British"], ["3. Viking"], ["4. Mongol"]],
                   [["1. England"], ["2. France"], ["3. Belgium"], ["4. Brazil"]]]

history_correct_answers = [["4"],
                           ["3"],
                           ["3"],
                           ["1"],
                           ["2"]]

geography_questions = [["What is the capital of England?"],
                       ["Which is the largest country in the world?"],
                       ["Which Italian city is famous for its canals?"],
                       ["Dublin is the largest city in which country?"],
                       ["Which large river flows through London?"]]

geography_answers = [[["1. Birmingham"], ["2. Manchester"], ["3. Leeds"], ["4. London"]],
                     [["1. Canada"], ["2. Russia"], ["3. Iceland"], ["4. Argentina"]],
                     [["1. Venice"], ["2. Rome"], ["3. Palermo"], ["4. Pisa"]],
                     [["1. Wales"], ["2. Scotland"], ["3. Ireland"], ["4. England"]],
                     [["1. Thames"], ["2. Trent"], ["3. Severn"], ["4. Clyde"]]]

geography_correct_answers = [["4"],
                             ["2"],
                             ["1"],
                             ["3"],
                             ["1"]]


class Quiz:
    """ Class creates the quiz, allowing for users to take a short revision quiz on different subjects """
    # set variables when class initialised, taking arguments from the config.py file, via main.py
    def __init__(self):
        self.is_running = True  # variable contains program on or off state, always start as True
        self.stage = 1  # stage is used to determine which input stage quiz is on, for the 'help' functionality
        self.replay = True  # variable used to control if user is asked if they want to retry quiz

        # arrays store the input from the config.py file, allowing the quiz to be easily modified and updated
        self.question_bank_maths = maths_questions
        self.answer_bank_maths = maths_answers
        self.correct_maths = maths_correct_answers

        self.question_bank_history = history_questions
        self.answer_bank_history = history_answers
        self.correct_history = history_correct_answers

        self.question_bank_geography = geography_questions
        self.answer_bank_geography = geography_answers
        self.correct_geography = geography_correct_answers

        self.current_question_bank = []  # empty placeholder array used to store questions
        self.current_answer_bank = []  # empty placeholder array used to store answers
        self.current_correct = []  # empty placeholder array used to store answers

        self.score_counter = 0  # variable stores number of correct answers
        self.questions_taken = 0  # variable stores number of questions user has attempted

        print("🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆃🅷🅴 🆁🅴🆅🅸🆂🅸🅾🅽 🆀🆄🅸🆉".center(45))  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')
        print("\nThe quiz covers topics you are currently learning in school.")

        self.quiz_start()  # trigger the quiz_start method to provide user instructions

    # method is used to start the quiz, guiding the user throughout
    def quiz_start(self):
        """ method starts the quiz, requesting user inputs to generate the quiz and answer questions """
        while self.is_running:  # when this while loop breaks, we return to the main module
            self.stage = 1  # stage 1 is the setup stage - user must choose the subject to take the quiz about
            print("\nSelect the subject you would like to take a quiz about?")
            print("Type '1' for Maths, '2' for History, or '3' for Geography")
            quiz_selection = self.input_check()  # input_check method checks for keywords and ensures correct user input
            if quiz_selection == "exit":  # check for the "exit" keyword.
                print("Goodbye from the quiz! \U0000263B")
                self.replay = False  # ensure user doesnt get asked to replay quiz at the end
                break  # if "exit" found we break the loop, leaving this feature module

            self.stage = 2  # stage 2 is the quiz stage
            self.quiz_builder(quiz_selection)  # method builds the quiz based on subject user selected

            # while loop is used to keep the quiz going until the user completes all of the questions in a random order
            while len(self.current_question_bank) > 0:  # while we still have questions in the question bank
                # get a random number between 0 and question_bank length - allows for dynamic question numbers
                random_number = randrange(0, len(self.current_question_bank))
                self.question(random_number)  # get a random question from the question bank
                question_answer = self.input_check()  # method used to get users question answer and check for keywords
                if question_answer == "exit":  # check for the "exit" keyword.
                    print("Goodbye from the quiz! \U0000263B")
                    self.replay = False  # ensure user doesnt get asked to replay quiz at the end
                    break  # if "exit" found we break the loop, leaving this feature module
                self.answer_check(random_number, question_answer)  # increment to score if correct
                # remove question from arrays before we then fetch another random question
                self.question_remove(random_number)
                self.completed_check()   # check to see if the quiz has finished rather than simply been exited
        self.replay_check()  # if user wants to play again, properties are reset and quiz restarts

    # method populates the current question, answer and correct arrays
    def quiz_builder(self, subject_selection):
        """ Method takes in the users chosen subject as an argument and generates a quiz about that subject """
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

    # method outputs the question and possible answers to the user using the random number as the list index position
    def question(self, random_number):
        """ Method takes in a random number as an argument, and prints a question and its potential answers """
        # get the length of the question so we can use it to create a neat barrier from the last question
        question = str(self.current_question_bank[random_number])  # get the question as a string
        print("\n" + ("-" * (len(question) - 4)), config.Style.bold)
        # new line for spacing and make title bold - divide to break up the text between rounds based on question length
        print(*self.current_question_bank[random_number], config.Style.end,config.Style.purple)
        # print question without brackets, and remove bold styling
        for answer in self.current_answer_bank[random_number]:
            print(*answer)  # print out each possible answer without brackets

    # method checks to see if user got the question right, incrementing to the counter if so
    def answer_check(self, random_number, user_answer):
        """ Method takes in the users answer as an argument and checks it against the correct answer based on the
        random number argument """
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
        """ Method removes a question and its associated answers from the question bank once its been used,
        based on the question number argument """
        del self.current_question_bank[question_number]  # delete question from array using its index position
        del self.current_answer_bank[question_number]
        del self.current_correct[question_number]

    # method checks to ensure correct string is entered by user
    def input_check(self):
        """ Method handles the user input ensuring its valid whilst looking for keywords 'exit' and 'help' """
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            if self.stage == 1:  # if user is at quiz selection
                user_input = input(": ")
                if user_input.lower() == "exit":
                    self.is_running = False  # statement breaks input while loops
                    self.replay = False  # ensure user doesnt get asked to replay quiz at the end
                    user_input = user_input.lower()  # .lower ensures the input is returned in correct format
                elif user_input.lower() == "help":  # if/else statement controls tailored help messages
                    print("\nYou are in the revision quiz! Type in a number to choose the quiz topic")
                elif user_input == "1" or user_input == "2" or user_input == "3":
                    break
                else:  # user didnt enter "help" or "exit" but put in more than one letter
                    print("\nPlease try again, type '1' for Maths, '2' for History and '3' for Geography 👍")
            elif self.stage == 2:  # if user is at answer input
                user_input = input("\nEnter your answer (1-4): ")
                if user_input.lower() == "exit":
                    self.is_running = False  # statement breaks input while loops
                    self.replay = False  # ensure user doesnt get asked to replay quiz at the end
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
        """ Method checks to see if the user has completed all the questions on a subject and provides a score if so """
        if len(self.current_question_bank) == 0:  # if zero, no questions are remaining
            print("\nWell done for taking the quiz!")
            print(config.Style.bold)  # add bold styling to final score line
            print("***** Your score is {}/{} *****".format(self.score_counter, self.questions_taken))
            print(config.Style.end, config.Style.purple)  # remove bold styling
            self.is_running = False  # break out of the start loop
            self.replay = True  # ensure user is asked if they want to re try quiz

    # method checks to see if user wants to replay the game after its finished
    def replay_check(self):
        """ Method asks user if they would like to replay the quiz """
        while self.replay:
            print("\nWould you like to try again?")
            replay = str(input("Enter '1' for yes, '2' for no: "))
            if replay == "1":  # if user wants to restart we need to reset game state and restart
                self.score_counter = 0  # reset score counter back to zero
                self.questions_taken = 0  # reset question counter back to zero
                self.is_running = True  # re-enter the start loop
                self.quiz_start()  # restart the game
            elif replay == "2" or replay.lower() == "exit":  # user wants to leave the game
                print("Goodbye from the quiz! \U0000263B")
                self.is_running = False
                # leaving the method will cause the script to end and put the user back to the main menu
                self.replay = False  # ensure user doesnt get asked to replay quiz at the end
            elif replay.lower() == "help":
                print("\nYou are in the revision quiz! Type in '1' to try again, or '2' to exit the quiz")
