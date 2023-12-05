#imports
import random
from seting import *
from tasks import *


#variabls
inventory = []


#game code
def main_game():

    day_start = True
    while seting.curent_helth > 0:
        if day_start == True:
            task_number = random.randint(1,5)
            print (task_number)
            taskes_asked = []
            taskes_asked.append(task_number)
            taskes_asked.sort
            if task_number in taskes_asked:
                continue
            if task_number == 1:
                task_1()
            elif task_number == 2:
                task_2()
            elif task_number == 3:
                task_3()
            elif task_number == 4:
                task_4()
            elif task_number == 5:
                task_5()
            accept = input(f"{name} will you take on this task y/n:>")
            if accept == "y" or "Y":
                day_start = False
            else: 
                "you laze around for the day"

        else:

            pass



#driver
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")

main_game()