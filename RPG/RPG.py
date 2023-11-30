#imports
import random
from seting import *
# from tasks import task_1


#variabls
inventory = []


#game code
def game():

    while seting.curent_helth > 0:
        if day_start == True:
            # task_1()
            pass



#driver
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")
print(f"The year is taisho 12 (1923) the date is may 2nd in Chiba japan your name is {name} you find yourself in your villa over looking the mountain when a person from the local village comes to you")
print('''villager:
    {name} help will you please go into the forest and get me some wood so i can buld a house you will be payd hansomly of course''')
acept_task = input("will you take on this task {name}? y/n:>")
if acept_task == "y":
    day_start = False
    game()
else:
    print("you laze around thoughout the day")
    day_start = True
    game()