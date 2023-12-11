import time
from seting import *

# all while loops are to make sure player does the prompted input
def tutorial(name):
    print(f"hello {name}, welcome to the tutorial. Everything done here will not affect your gameplay.")
    print("Starting tutorial...")
    time.sleep(3)
    print("Tutorial started")
    print("In the actual game, items, damage, and such are randomized. Here they are going to be the same every time.")
    print("Every new day, you will get a new task and then a random fairness of payment.")
    print("The villager will come to you and ask you to do something. Here is an example:")
    print(f"""Villager:
           {name}, will you please go into the peaks and rescue my daughter? She went up there and got stuck. You will be paid fairly, of course.>""")
    print("Then the game will ask you if you will accept this task. This time, let's accept the task.")
    task = True
    while task:
        task_acceptance = input(f"{name}, will you accept this task y/n:>")
        if task_acceptance == "y":
            print("Alright, let's go on our adventure.")
            task = False
        else:
            print("Please accept the task.")
    print("Alright, we have accepted the task. Next up is to start going.")
    print("Once you accept the task, we must leave the villa.")
    print("The game will ask if you would like to walk - w or check inventory - i in the prompt following this. Let's open our inventory.")
    inventory = True
    while inventory:
        inventoryPrompt = input("What would you like to do? w - walk, i - inventory:>")
        if inventoryPrompt == "i":
            print("You have [] in your inventory.")
            print("You have 0 current money.")
            print("Your health is 100/100.")
            inventory = False
        elif inventoryPrompt == "w":
            print("Please select i.")
        else:
            print("Make sure you only select i, nothing else.")
    print("Now let's go on our task. This time, let's press w in the prompt.")
    print("Every time you press w, you will be prompted to choose again, unless of course something happens.")
    walk = True
    walkTime = 0
    while walk and walkTime <= 6:
        walkPrompt = input("What would you like to do? w - walk, i - inventory:>")
        if walkPrompt == "w":
            walkTime += 1
        elif walkPrompt == "i":
            print("Please select w.")
        else:
            print("Make sure you only select w, nothing else.")
    print("Oh no, we came across a Bandit gang. Here is a description:")
    print(setting.enemies["Bandit Gang"]['description'])
    print("We have 2 options: 1 attack, which is 'a', and 2 run, which is 'r'. When you run, you have a 50 percent chance of getting away.")
    print("Let's run this time; I don't like our chances 3 against 1.")
    run1 = True
    while run1:
        run_success = input("Would you like to try and run - r or attack - a:>")
        if run_success == "r":
            print("Yay, we got away. That was close.")
            run1 = False
        elif run_success == "a":
            print("Please input r, which stands for run, for this one.")
        else:
            print("Make sure you only have the r, nothing else.")
    walk = True
    walkTime = 0
    while walk and walkTime <= 6:
        walkPrompt = input("What would you like to do? w - walk, i - inventory:>")
        if walkPrompt == "w":
            walkTime += 1
        elif walkPrompt == "i":
            print("Please select w.")
        else:
            print("Make sure you only select w, nothing else.")
    print("Oh no, another enemy. This time it is a Forest Yokai. Here is a description:")
    print(setting.enemies["Forest Yokai"]["description"])
    print("Let's run again.")
    run2 = True
    while run2:
        run_fail = input("Would you like to try and run - r or attack - a:>")
        if run_fail == "r":
            run2 = False
        elif run_fail == "a":
            print("Please input r, which stands for run, for this one.")
        else:
            print("Make sure you only have the r, nothing else.")
    print("Dang, we couldn't get away this time.")
    print("You took 50 damage.")
    print("I'm mad. Let's fight this.")
    attackVar = True
    while attackVar:
        attack = input("Would you like to attack or run away? a - attack, r - run:>")
        if attack == "a":
            print("You do 150 damage and defeat the Yokai.")
            print("You gain 50 coins.")
            print("You gain 30 HP, leaving you at 80/100.")
            attackVar = False
        elif attack == "r":
            print("Please select a for attack.")
        else:
            print("Make sure you only input a, nothing else.")
    print("Hey, 50 coins, that's cool. Anyway, let's continue.")
    walk = True
    walkTime = 0
    while walk and walkTime <= 6:
        walkPrompt = input("What would you like to do? w - walk, i - inventory:>")
        if walkPrompt == "w":
            walkTime += 1
        elif walkPrompt == "i":
            print("Please select w.")
        else:
            print("Make sure you only select w, nothing else.")
    print("Oh no, not another enemy. This time it is a Mountain Tengu. Here is a description:")
    print(setting.enemies['Mountain Tengu']['description'])
    print("I'm feeling confident this time. Let's fight instead of running.")
    fight = True
    while fight:
        fightPrompt = input("Would you like to attack or run away? a - attack, r - run:>")
        if fightPrompt == "a":
            print("You do 150 damage and defeat the Yokai.")
            print("You gain 50 coins.")
            print("You gain 20 HP, leaving you at 100/100.")
            fight = False
        elif fightPrompt == "r":
            print("Please select a for attack.")
        else:
            print("Make sure you only input a, nothing else.")
    print("And finally, we made it. We saved the person. Let's go home.")
    print(f"You are now ready to play the game, {name}. Good luck!")
    print("Shutting down tutorial...")
    print("...")
    time.sleep(3)
