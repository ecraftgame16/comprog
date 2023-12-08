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
    day = 1
    while seting.curent_helth > 0 and game_finished == False:
        if day_start == True:
            if day > 1:
                seting.max_health += 50
            seting.curent_helth = seting.max_health
            task_selection()
            accept = input(f"{name} will you take on this task y/n:>")
            if accept == "y":
                day_start = False
            elif accept == "n": 
                print ("you laze around for the day")
                print ("...")
                time.sleep(10)
                print("it is now the next day")
                time.sleep(3)
                continue
            else:
                print("please use y for yes and n for no")
                indicive = True
                while indicive == True:
                    accept = input(f"{name} will you take on this task y/n:>")
                    if accept == "y":
                        day_start = False
                        indicive = False
                    elif accept == "n":
                        print ("you laze around for the day")
                        print ("...")
                        time.sleep(10)
                        print("it is now the next day")
                        time.sleep(3)
                        indicive = False
        else:
            action = input("""what would you like to do w - walk i - inventory:>""")
            if action == "w":     
                atack = random.randint (1,3)
                if atack == 2:
                    atacker = random.choice(seting.lEnimies)
                    print(f"ohh no a foe has apperd it is a {atacker} hear is a discription")
                    print(seting.enimies[atacker]['discription'])
                    run_atack = input("would you like to try and run - r or atack - a:>")
                    if run_atack == "a":
                        atack_player_first(atacker)
                    elif run_atack == "r":
                        sucess = random.randint(1,50)
                        if sucess % 2 == 0:
                            print ("you got away")
                            continue
                        else:
                            print("you couldn't run away")
                            atack_enimie_first(atacker)
            elif action == "i":
                print(f"you have {inventory} in your inventory")
                print(f"you have {money} curent money")
                print(f"your health is {seting.curent_helth}/{seting.max_health}")
            else:
                print("please use i for inventory or w for walking")

def task_selection():
    tasks_asked = []  # Keep track of asked tasks
    while True:
        task_number = random.randint(1, 5)
        if task_number not in tasks_asked:  # Check if the task has not been asked before
            tasks_asked.append(task_number)  # Add the new task to the list
            break  # Exit the loop once a new task is found
    
    #calling the tasks
    print("A local villiger comes up to you and asks ...")
    # time.sleep(2)
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

def atack_player_first(atacker):
    enime_helth = random.randint (seting.enimies[atacker]["health minumim"],seting.enimies[atacker]["health maxumim"])
    not_run = True
    while enime_helth > 0 and seting.curent_helth > 0 and not_run == True:
        #player atack
        if seting.curent_helth > 0:
            run_atack = input("would you like to atack or runaway? a - atack r - run:>")
            if run_atack == "a":
                hero_damage = random.randint(20,40)
                enime_helth -= hero_damage
                print (f"you do {hero_damage} damage")
            elif run_atack == "r":
                sucess = random.randint(1,50)
                if sucess % 2 == 0:
                    print ("you got away")
                    not_run = False
                else:
                    print("you couldn't run away")
        
        #enime atack
        if enime_helth > 0 and not_run == True:
            enime_damage = random.randint(seting.enimies[atacker]["dammage minum"],seting.enimies[atacker]["dammage maximum"])
            print (f"you got hit you took {enime_damage} damage")
            seting.curent_helth -= enime_damage

        if seting.curent_helth <= 0:
            print("You have died and faild the mission sorry")
            exit()

        if enime_helth <= 0:
            profit = random.randint(10, 50)
            print (f"you beat them you have won {profit}")
            hp_gain = random.randint (20, 30)
            total_health = hp_gain + seting.curent_helth
            if total_health <= seting.max_health:
                seting.curent_helth += hp_gain
                print(f"you gain {hp_gain} health totaling {total_health}")
            elif total_health > seting.max_health:
                seting.curent_helth = seting.max_health
                print(f"your health goes back to max which is {seting.max_health}")


def atack_enimie_first(atacker):
    #enime atack
    enime_helth = random.randint (seting.enimies[atacker]["health minumim"],seting.enimies[atacker]["health maxumim"])
    not_run = True
    while enime_helth > 0 and seting.curent_helth > 0 and not_run == True:
        if enime_helth > 0 and not_run == True:
            enime_damage = random.randint(seting.enimies[atacker]["dammage minum"],seting.enimies[atacker]["dammage maximum"])
            print (f"you got hit you took {enime_damage} damage")
            seting.curent_helth -= enime_damage
        
        #player atack
        if seting.curent_helth > 0:
            run_atack = input("would you like to atack or runaway? a - atack r - run:>")
            if run_atack == "a":
                hero_damage = random.randint(20,40)
                enime_helth -= hero_damage
                print (f"you do {hero_damage} damage")
            elif run_atack == "r":
                sucess = random.randint(1,50)
                if sucess % 2 == 0:
                    print ("you got away")
                    not_run = False
                else:
                    print("you couldn't run away")

        if seting.curent_helth <= 0:
            print("You have died and faild the mission sorry")
            exit()

        if enime_helth <= 0:
            profit = random.randint(10, 50)
            print (f"you beat them you have won {profit}")
            hp_gain = random.randint (20, 30)
            total_health = hp_gain + seting.curent_helth
            if total_health <= seting.max_health:
                seting.curent_helth += hp_gain
                print(f"you gain {hp_gain} health totaling {total_health}")
            elif total_health > seting.max_health:
                seting.curent_helth = seting.max_health
                print(f"your health goes back to max which is {seting.max_health}")

#driver
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")
game_finished = False
tutorial_question = input(f"{name} would you like to go though the tutrial y/n:>")
money = 0
if tutorial_question == "y":
    tutorial(name)
main_game()