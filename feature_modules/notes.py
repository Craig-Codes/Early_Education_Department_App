# Class creates the Notes feature once instantiated
# Allows user to create and edit notes to use to help throughout the day

import textwrap  # textwrap module is used to nicely wrap long text to multiple lines
import config  # config module used to store note data and gives access to global styling


class Notes:
    # when class is instantiated, set the following variable values and start the notes feature
    def __init__(self):
        self.is_running = True  # variable controls the start loop and keeps user in the notes feature
        self.notes = config.notes_list  # variable gets the notes list from the config.py file
        print("🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🅽🅾🆃🅴🆂".center(50))  # give user starting instructions
        print('\nTo return to the main menu just type "exit" at any time')
        print('To get help just type "help" at any time')

        # stage is used to determine which input stage calculator is on,
        self.stage = 1  # required for the "help" functionality and memory functions
        self.notes_start()  # start the notes application - instructions and user input

    # Method starts off the notes feature, requesting user input
    def notes_start(self):
        while self.is_running:  # when while loop breaks, we return to the main module
            # display all of the current notes to the user
            self.stage = 1  # stage 1 is user selection, where user chooses what to do (create, edit, delete)
            print("\nCurrent saved notes:")
            for index in range(len(self.notes)):  # get the length of the notes list, getting all of the index values
                self.output_note(index)  # pass the index value into the method to output the individual notes

            # user selects if they want to add, edit or delete a note
            action_choice = self.input_check()  # input_check method checks for keywords and ensures correct user input
            if action_choice == "exit":  # check for the "exit" keyword.
                print("Goodbye from notes! \U0000263B")
                break  # if "exit" found we break the loop, leaving this feature module

            elif action_choice == "1":  # user wants to add a note
                self.stage = 2  # user adding note
                self.add_note()  # method adds a new note

            elif action_choice == "2":  # user wants to edit a note
                self.stage = 3  # user editing note
                self.edit_note()  # method edits an existing note

            elif action_choice == "3":  # user want to delete a note
                if len(self.notes) > 0:  # check to ensure we have notes in the notes list
                    self.stage = 4  # user deleting note
                    self.delete_note()  # method deletes an existing note
                else:
                    print("\n***** There are no notes to delete! *****")

    # method displays an individual note
    def output_note(self, note_number):
        frontend_note_number = note_number + 1  # removes the '0' so note numbers start at 1
        print(config.Style.bold, config.Style.underline)  # make title bold and underlined
        print("{}.{}".format(frontend_note_number, self.notes[note_number][0]))
        # print notes title with its index number(+1) which user can use to access it
        print(config.Style.end, config.Style.purple)  # reset styling back to normal
        if len(self.notes[note_number][1]) > 60:  # check to see if note content is longer than 60 characters
            # if longer than 60 characters we want to line break so that the notes look nice in the console
            print(textwrap.fill(self.notes[note_number][1], 60))  # wrap the note every 60 characters to a new line
            print("-" * 60)  # draw a divide to differentiate between the different notes
        else:  # if notes are less than 60 characters long
            print(self.notes[note_number][1])  # print the note
            print("-" * len(self.notes[note_number][1]))  # draw a divide to differentiate between the different notes

    # method sanitises the user input, checking to see if it's a valid input
    def input_check(self):
        user_input = ""  # ensure user_input is cleared
        while self.is_running:  # while loop ensures user gives a valid input
            if self.stage == 1:  # user in add, edit or delete selection stage
                print("\nTo add a note type '1', to edit a note's content type '2' or to delete a note type '3'")
                user_input = input(": ")  # user provides an input
                if user_input in ("1", "2", "3"):  # tuple of correct input values
                    break  # leave the while loop as valid input
                else:
                    self.help_exit_check(user_input)  # method checks for keywords and typos

            elif self.stage == 2.1:  # user in new title input
                print("\nType in the title of the new note")
                user_input = input(": ")
                if user_input.lower() == "exit" or user_input.lower() == "help":  # check for keywords
                    self.help_exit_check(user_input)  # method checks for keywords and typos
                elif len(user_input) > 60:  # dont want the title to be longer than 60 characters
                    print("Title can't be longer than 60 characters, try again")
                else:
                    break  # valid user input

            elif self.stage == 2.2:  # user in new content input
                print("\nType in the content of the new note")
                user_input = input(": ")
                if user_input.lower() == "exit" or user_input.lower() == "help":
                    self.help_exit_check(user_input)
                else:
                    break

            elif self.stage == 3.1:  # user selecting which note number to edit
                print("\nType in the number of the note you want to edit")
                user_input = input(": ")
                valid_note_entries = self.valid_note_numbers()  # method gets a list of all valid note numbers
                if user_input in valid_note_entries:  # check to see if user input is in valid note entries list
                    break  # valid user input - note number exists
                else:
                    self.help_exit_check(user_input)

            elif self.stage == 3.2:  # user in edit content input
                print("\nType in the notes new content")
                user_input = input(": ")
                if user_input.lower() == "exit" or user_input.lower() == "help":  # check for keywords
                    self.help_exit_check(user_input)
                else:
                    break

            elif self.stage == 4:  # user selecting which not number to delete
                print("\nType in the number of the note you want to delete")
                user_input = input(": ")
                valid_note_entries = self.valid_note_numbers()  # method gets a list of all valid note numbers
                if user_input in valid_note_entries:  # check to see if user input is a valid note entry
                    break  # valid user input - note number exists
                else:
                    self.help_exit_check(user_input)
        return user_input  # return the value to store sanitised input into a variable

    # Method checks to see if user has input "help" or "exit" or simply a typo
    def help_exit_check(self, user_input):
        if user_input.lower() == "exit":
            self.is_running = False  # statement breaks input while loops, causing notes feature to exit to main menu
        elif user_input.lower() == "help":  # if/else statement controls tailored help messages
            if self.stage == 1:
                print("You are in the notes feature! "
                      "To add a note type '1', to edit a note type '2' or to delete a note type '3'")
            elif self.stage == 2.1:
                print("You are in the notes feature! Type the new notes title")
            elif self.stage == 2.2:
                print("You are in the notes feature! Type the new notes content")
            elif self.stage == 3.1:
                print("You are in the notes feature! Type the number of the note you want to edit")
            elif self.stage == 3.2:
                print("You are in the notes feature! Type the edited content of the note to update it")
            elif self.stage == 4:
                print("You are in the notes feature! Type in the number of the note you wish to delete")
        else:
            print("\nPlease try typing in a number again 👍")  # generic error for a typo

    #  method adds a note to the notes list
    def add_note(self):
        while self.is_running:  # while loop ensures user gives a valid input
            self.stage = 2.1  # title creation stage
            title = self.input_check()  # get the sanitised user input
            if title == "exit":  # check for the "exit" keyword.
                print("Goodbye from notes! \U0000263B")
                break  # if "exit" found we break the loop, leaving this feature module
            self.stage = 2.2  # content creation stage
            content = self.input_check()
            if content == "exit":
                print("Goodbye from notes! \U0000263B")
                break

            self.notes.append([title, content])  # add the new note to the notes list - create note from user inputs
            self.save_notes()  # method saves notes to config.py file allowing data to persist during session
            print("A new note has been added!")
            break  # new note added, break from the loop and return to the start method where all notes are displayed

    # method edits an existing notes content
    def edit_note(self):
        while self.is_running:  # while loop ensures user gives a valid input
            self.stage = 3.1  # provide user with a list of notes with their number and title
            print("\nNotes which can be edited:")
            for index, note in enumerate(self.notes):  # get the index and values of all notes
                print("{}. {}".format(index + 1, note[0]))  # output the notes number and title so that users see them

            note_number = self.input_check()  # get the sanitised user input - user chooses note number to delete
            if note_number == "exit":  # check for the "exit" keyword.
                print("Goodbye from notes! \U0000263B")
                break  # if "exit" found we break the loop, leaving this feature module
            note_number = int(note_number) - 1  # we now have the users selected note and its index position
            # remove 1 from note number to get the actual index number (arrays start at 0 not 1)

            self.stage = 3.2  # user is in the note editing stage
            note_content = self.input_check()  # get the sanitised user input
            if note_content == "exit":  # check for the "exit" keyword.
                print("Goodbye from notes! \U0000263B")
                break  # if "exit" found we break the loop, leaving this feature module
            self.notes[note_number][1] = note_content  # assign the new content to the note
            self.save_notes()  # method saves notes to config.py file allowing data to persist during session
            print("A note has been updated!")
            break  # note updated, break from the loop and return to the start method where all notes are displayed

    # method deletes an existing note
    def delete_note(self):
        while self.is_running:  # while loop ensures user gives a valid input
            # provide user with a list of notes with their number and title
            print("\nNotes which can be deleted:")
            for index, note in enumerate(self.notes):  # get the index and values of all notes
                print("{}. {}".format(index + 1, note[0]))  # output the notes number and title

            note_number = self.input_check()  # get the sanitised user input - ensures number matches a note number
            if note_number == "exit":  # check for the "exit" keyword.
                print("Goodbye from notes! \U0000263B")
                break  # if "exit" found we break the loop, leaving this feature module
            note_number = int(note_number) - 1
            # remove 1 from note number to get the actual index number (arrays start at 0 not 1)
            del self.notes[note_number]  # remove the note from the notes list based on its index
            self.save_notes()  # method saves notes to config.py file allowing data to persist during session
            print("A note has been deleted!")
            break  # note deleted, break from the loop and return to the start method where all notes are displayed

    # method returns a list containing all of the current notes index numbers (+1) as string values
    def valid_note_numbers(self):
        list_length = len(self.notes) + 1  # get length of notes and add 1 so that all note numbers are included
        list_indexes = list(range(1, list_length))  # create a new list from 1 to list_length
        return list(map(str, list_indexes))  # use map to convert list entries from int to strings

    # method saves the memory value into the config.py file
    def save_notes(self):
        config.notes_dict = self.notes  # memory_value variable in config.py given current memory value
