#imports
import random
import time
from seting import *
from tasks import *
from tutorial import tutorial


#variabls
inventory = []


#game code
def main_game():
    day_start = True #makes new day true for start of while loop
    
    while seting.curent_helth > 0 and game_finished == False:
        if day_start == True:
            task_selection()
            accept = input(f"{name} will you take on this task y/n:>")
            if accept == "y":
                day_start = False
            else: 
                print ("you laze around for the day")
                print ("...")
                time.sleep(10)
                print("it is now the next day")
                time.sleep(3)
                continue
        else:
            action = input("""what would you like to do w - walk i - inventory:>""")

def task_selection():
    tasks_asked = []  # Keep track of asked tasks
    while True:
        task_number = random.randint(1, 5)
        if task_number not in tasks_asked:  # Check if the task has not been asked before
            tasks_asked.append(task_number)  # Add the new task to the list
            break  # Exit the loop once a new task is found
    
    #calling the tasks
    print("A local villiger comes up to you and asks ...")
    time.sleep(2)
    if task_number == 1:
        task_1(name)
        day_start = False
    elif task_number == 2:
        task_2(name)
        day_start = False
    elif task_number == 3:
        task_3(name)
        day_start = False
    elif task_number == 4:
        task_4(name)
        day_start = False
    elif task_number == 5:
        task_5(name)
        day_start = False


#driver
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")
game_finished = False
tutorial_question = input(f"{name} would you like to go though the tutrial y/n:>")
if tutorial_question == "y":
    tutorial(name)
main_game()