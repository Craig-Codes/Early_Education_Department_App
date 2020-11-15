# Module is used to share global variables and Classes across all of the applications modules

# Calculator global variable - allowing memory function to hold saved data when calculator is re-instantiated
# This value does not need to be saved when the entire application is restarted, only during the session
memory_value = 0  # start memory value as zero, this can then be changed during applications current session


# Class contains colours and styles to be used to make the terminal output more exciting for children
# Bold colors may add some visual appeal for the children, and are an example of how colours can be implemented
# ANSI codes will work in pyCharm, but some will not work in the terminal / powershell / IDLE - limitation!
# More font colours and styles can easily be added if required then accessed across the application
class Style:
    """ Class allows for output styling to be manipulated """
    bold = '\033[1m'
    underline = '\033[4m'
    purple = '\033[0;35m'
    end = '\033[0m'
