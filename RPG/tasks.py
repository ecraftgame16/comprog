import random

def task_1(name):
    task = f'''villager:
        "{name} will you please go into the forest and get me some wood so i can buld a house '''
    payment_1 = ' you will be payed handomsly of course'
    payment_2 = ' you will be payed faily of course'
    payment_3= ' you will be payed'
    payment = random.randint (1,3)
    if payment == 1:
        print(task+payment_1)
    elif payment == 2:
        print (task+payment_2)
    elif payment == 3:
        print (task+payment_3)

def task_2(name):
    task = f'''villager:
        "{name} Please find this anchaint hiden shrine dedicated to the god
        Fudo Myo-o '''
    payment_1 = ' you will be payed handomsly of course'
    payment_2 = ' you will be payed faily of course'
    payment_3= ' you will be payed'
    payment = random.randint (1,3)
    if payment == 1:
        print(task+payment_1)
    elif payment == 2:
        print (task+payment_2)
    elif payment == 3:
        print (task+payment_3)

def task_3(name):
    task = f'''villager:
        "{name} please i need you to go get thease mgaical mountain herbs
        my wife will die if you dont '''
    payment_1 = ' you will be payed handomsly of course'
    payment_2 = ' you will be payed faily of course'
    payment_3= ' you will be payed'
    payment = random.randint (1,3)
    if payment == 1:
        print(task+payment_1)
    elif payment == 2:
        print (task+payment_2)
    elif payment == 3:
        print (task+payment_3)\
        
def task_4(name):
    task = f'''villager:
        "{name} there are some monks further up the montain who have been concerning us 
        please go find out there deal '''
    payment_1 = ' you will be payed handomsly of course'
    payment_2 = ' you will be payed faily of course'
    payment_3= ' you will be payed'
    payment = random.randint (1,3)
    if payment == 1:
        print(task+payment_1)
    elif payment == 2:
        print (task+payment_2)
    elif payment == 3:
        print (task+payment_3)
    
def task_5   (name):
    task = f'''villager:
        "{name} I need you to go into the wispering woods i heard at the rock
        that is in the center there is a great tresure '''
    payment_1 = ' you will be payed handomsly of course'
    payment_2 = ' you will be payed faily of course'
    payment_3= ' you will be payed'
    payment = random.randint (1,3)
    if payment == 1:
        print(task+payment_1)
    elif payment == 2:
        print (task+payment_2)
    elif payment == 3:
        print (task+payment_3)