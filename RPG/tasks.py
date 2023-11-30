import random
from RPG import *

def task_1():
    task = '''villager:
        "{name} will you please go into the forest and get me some wood so i can buld a house"'''
    payment_1 = "you will be payed handomsly of course"
    payment_2 = "you will be payed faily of course"
    payment_3= "you will be payed"
    payment = random.randint (1,3)
    if payment == 1:
        print(task+payment_1)
    elif payment == 2:
        print (task+payment_2)
    elif payment == 3:
        print (task+payment_3)