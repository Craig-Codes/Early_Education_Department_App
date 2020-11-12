# Module is used to share global variables across all of the applications modules
# This file can be easily modified by teachers to edit how certain features work
# Data can be saved using this file, and reused when instantiating objects during the users session

# schedule global variable - users starting schedule, also used if the schedule module is re-instantiated
schedule = ["Maths", "Science", "History", "Geography", "Art", "PE"]  # teacher can easily input the days schedule
class_list = ["Maths", "Science", "History", "Geography", "Art", "PE", "English", "Free Period"]
# teacher can easily add in more subjects, such as Coding, French, Business etc

# Calculator global variable - allowing memory function to hold saved data when calculator is re-instantiated
memory_value = 0  # start memory value as zero, this can then be changed during applications current session

# hangman word list - add words here to expand the list
hangman_word_list = ["apple", "laugh", "tiger", "pizza", "music", "party", "piano",
                     "women", "dream", "earth", "space", "river", "money", "smile"]

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

# notes saved entries - stored in a list of lists, with each inner list being a saved note
# ordered datatype required to help code remain easily reusable and user friendly
# starting notes are here, this variable is updated as notes are created, modified and deleted
notes_list = [["Break", "Break is 15 minutes earlier today, at 1030"],
              ["Snacks", "Mom packed me a banana and an apple, "
                         "but i've still got a Mars bar in my backpack from last week ... "],
              ["After School", "I've got coding club on Wednesday, swimming on Thursday and chess on Friday!"]]


# Class contains colours and styles to be used to make the terminal output more exciting for children
# Bold colors may add some visual appeal for the children, and are an example of how colours can be implemented
# ANSI codes will work in pyCharm, but will not work in the terminal / powershell / IDLE - limitation!
# More font colours and styles can easily be added if required then accessed across the application
class Style:
    bold = '\033[1m'
    underline = '\033[4m'
    purple = '\033[0;35m'
    end = '\033[0m'
