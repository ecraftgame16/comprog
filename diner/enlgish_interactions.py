from menu import *
import time
def english():
    print ("follow me to you table")
    time.wait(2)
    try:
        which_menu = int(input("""which menue would you like to look at
                               1 entree"""))
    except ValueError:
        print("Input Error, please ensure that you only use a number")
    pass