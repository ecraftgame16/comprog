import random

def task_1(name):
    task = f'''Villager:
        "{name}, will you please go into the forest and get me some wood so I can build a house?'''
    payment_1 = ' You will be paid handsomely, of course.'
    payment_2 = ' You will be paid fairly, of course.'
    payment_3 = ' You will be paid.'
    payment = random.randint(1, 3)
    if payment == 1:
        print(task + payment_1)
    elif payment == 2:
        print(task + payment_2)
    elif payment == 3:
        print(task + payment_3)

def task_2(name):
    task = f'''Villager:
        "{name}, please find this ancient hidden shrine dedicated to the god Fudo Myo-o.'''
    payment_1 = ' You will be paid handsomely, of course.'
    payment_2 = ' You will be paid fairly, of course.'
    payment_3 = ' You will be paid.'
    payment = random.randint(1, 3)
    if payment == 1:
        print(task + payment_1)
    elif payment == 2:
        print(task + payment_2)
    elif payment == 3:
        print(task + payment_3)

def task_3(name):
    task = f'''Villager:
        "{name}, please, I need you to go get these magical mountain herbs. My wife will die if you don't.'''
    payment_1 = ' You will be paid handsomely, of course.'
    payment_2 = ' You will be paid fairly, of course.'
    payment_3 = ' You will be paid.'
    payment = random.randint(1, 3)
    if payment == 1:
        print(task + payment_1)
    elif payment == 2:
        print(task + payment_2)
    elif payment == 3:
        print(task + payment_3)
        
def task_4(name):
    task = f'''Villager:
        "{name}, there are some monks further up the mountain who have been concerning us. Please go find out their deal.'''
    payment_1 = ' You will be paid handsomely, of course.'
    payment_2 = ' You will be paid fairly, of course.'
    payment_3 = ' You will be paid.'
    payment = random.randint(1, 3)
    if payment == 1:
        print(task + payment_1)
    elif payment == 2:
        print(task + payment_2)
    elif payment == 3:
        print(task + payment_3)
    
def task_5(name):
    task = f'''Villager:
        "{name}, I need you to go into the Whispering Woods. I heard that at the rock in the center, there is a great treasure.'''
    payment_1 = ' You will be paid handsomely, of course.'
    payment_2 = ' You will be paid fairly, of course.'
    payment_3 = ' You will be paid.'
    payment = random.randint(1, 3)
    if payment == 1:
        print(task + payment_1)
    elif payment == 2:
        print(task + payment_2)
    elif payment == 3:
        print(task + payment_3)
