#imports
import random
from seting import *
from tasks import *


#variabls
inventory = []


#game code
def main_game():
    day_start = True #makes new day true for start of while loop
    tasks_asked = []  # Keep track of asked tasks

    while seting.curent_helth > 0:
        if day_start:
            while True:
                task_number = random.randint(1, 5)
                if task_number not in tasks_asked:  # Check if the task has not been asked before
                    tasks_asked.append(task_number)  # Add the new task to the list
                    break  # Exit the loop once a new task is found
            
            #calling the tasks
            if task_number == 1:
                task_1(name)
            elif task_number == 2:
                task_2(name)
            elif task_number == 3:
                task_3(name)
            elif task_number == 4:
                task_4(name)
            elif task_number == 5:
                task_5(name)
            accept = input(f"{name} will you take on this task y/n:>")
            if accept == "y" or "Y":
                day_start = False
            else: 
                "you laze around for the day"
                day_start = True
                
        else:
            action = input("""what would you like to do w - walk i - inventory""")



#driver
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")

main_game()