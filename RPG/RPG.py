# imports
import random
import time
from seting import *
from tasks import *
from tutorial import tutorial

# variables
inventory = []

# game code
def main_game():
    day_start = True  # makes new day true for start of while loop
    day = 0
    while setting.current_health > 0 and game_finished == False:
        if day_start == True:
            day += 1
            if day == 5:
                the_Great_Kanto_Earthquake()
            walked_times = 0
            arrived = False
            if day > 1:
                setting.max_health += 50
            setting.current_health = setting.max_health
            task_selection()
            accept = input(f"{name} will you take on this task y/n:>")
            if accept == "y":
                day_start = False
            elif accept == "n":
                print("you laze around for the day")
                print("...")
                time.sleep(10)
                print("it is now the next day")
                time.sleep(3)
                continue
            else:
                print("please use y for yes and n for no")
                indecisive = True
                while indecisive == True:
                    accept = input(f"{name} will you take on this task y/n:>")
                    if accept == "y":
                        day_start = False
                        indecisive = False
                    elif accept == "n":
                        print("you laze around for the day")
                        print("...")
                        time.sleep(10)
                        print("it is now the next day")
                        time.sleep(3)
                        indecisive = False
        else:  # main functions
            # when player has walked between 10 - 20 times
            requierd_walk_times = random.randint(10,20)
            if walked_times >= requierd_walk_times and arrived == False:
                arrived = True
                print("you have arrived and done your task")
                print("time to return home")
                walked_times = 0  # resets walk time for the return walk
            # checks if the player has both arrived and walked then walked 10 - 20 times (the same number it took to get there)
            elif walked_times >= requierd_walk_times and arrived == True:
                print("we made it home finally")
                day_start = True
                new_item = random.choice(setting.lDecorationItems)
                inventory.append(new_item)
                inventory.append(setting.items_decoration[new_item])
                continue
            action = input("""what would you like to do w - walk i - inventory:>""")
            # makes walking work and calls attacks
            if action == "w":
                walked_times += 1
                attack = random.randint(1, 3)
                if attack == 2:  # if the number selected is 2 starts the attack option
                    attacker = random.choice(setting.lEnemies)  # selects the enemy
                    print(f"oh no a foe has appeared it is a {attacker} here is a description")  # describes the enemy
                    print(setting.enemies[attacker]['description'])
                    run_attack = input("would you like to try and run - r or attack - a:>")  # asks if player wants to run or attack
                    if run_attack == "a":
                        attack_player_first(attacker)  # calls attack where player attacks first since they chose attack
                    elif run_attack == "r":
                        success = random.randint(1, 50)
                        if success % 2 == 0:  # checks if player ran away successfully
                            print("you got away")
                            continue
                        else:  # if player didn't run away successfully tells player and calls the enemy attacking first
                            print("you couldn't run away")
                            attack_enemy_first(attacker)
            elif action == "i":  # runs inventory check
                print(f"you have {inventory} in your inventory")
                print(f"you have {money} current money")
                print(f"your health is {setting.current_health}/{setting.max_health}")
            else:  # error check
                print("invalid input please use i for inventory or w for walking")

def task_selection():  # selects tasks
    tasks_asked = []  # Keep track of asked tasks
    while True:
        task_number = random.randint(1, 5)
        if task_number not in tasks_asked:  # Check if the task has not been asked before
            tasks_asked.append(task_number)  # Add the new task to the list
            break  # Exit the loop once a new task is found

    # calling the tasks from tasks.py
    print("A local villager comes up to you and asks ...")
    time.sleep(3)
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

# Function called when player chooses attack
def attack_player_first(attacker):
    enemy_health = random.randint(setting.enemies[attacker]["health minimum"], setting.enemies[attacker]["health maximum"])
    not_run = True
    while enemy_health > 0 and setting.current_health > 0 and not_run == True:
        # Player's attack
        if setting.current_health > 0:
            run_attack = input("Would you like to attack or run away? a - attack, r - run:>")
            if run_attack == "a":
                hero_damage = random.randint(30,60)
                enemy_health -= hero_damage
                print(f"You do {hero_damage} damage")
            elif run_attack == "r":
                success = random.randint(1,50)
                if success % 2 == 0:
                    print("You got away")
                    not_run = False
                else:
                    print("You couldn't run away")
        
        # Enemy's attack
        if enemy_health > 0 and not_run == True:
            enemy_damage = random.randint(setting.enemies[attacker]["damage minimum"], setting.enemies[attacker]["damage maximum"])
            print(f"You got hit and took {enemy_damage} damage")
            setting.current_health -= enemy_damage

        if setting.current_health <= 0:
            print("You have died and failed the mission, sorry")
            exit()

        if enemy_health <= 0:
            profit = random.randint(10, 50)
            print(f"You beat them and have won {profit}")
            hp_gain = random.randint(20, 30)
            total_health = hp_gain + setting.current_health
            if total_health <= setting.max_health:
                setting.current_health += hp_gain
                print(f"You gain {hp_gain} health, totaling {total_health}")
            elif total_health > setting.max_health:
                setting.current_health = setting.max_health
                print(f"Your health goes back to max, which is {setting.max_health}")

# Function called when the player runs and fails
def attack_enemy_first(attacker):
    # Enemy's attack
    enemy_health = random.randint(setting.enemies[attacker]["health minimum"], setting.enemies[attacker]["health maximum"])
    not_run = True
    while enemy_health > 0 and setting.current_health > 0 and not_run == True:
        if enemy_health > 0 and not_run == True:
            enemy_damage = random.randint(setting.enemies[attacker]["damage minimum"], setting.enemies[attacker]["damage maximum"])
            print(f"You got hit and took {enemy_damage} damage")
            setting.current_health -= enemy_damage
        
        # Player's attack
        if setting.current_health > 0:
            run_attack = input("Would you like to attack or run away? a - attack, r - run:>")
            if run_attack == "a":
                hero_damage = random.randint(20,40)
                enemy_health -= hero_damage
                print(f"You do {hero_damage} damage")
            elif run_attack == "r":
                success = random.randint(1,50)
                if success % 2 == 0:
                    print("You got away")
                    not_run = False
                else:
                    print("You couldn't run away")

        if setting.current_health <= 0:  # Checks if player is dead
            print("You have died and failed the mission, sorry")
            exit()

        if enemy_health <= 0:  # Checks if enemy is defeated
            profit = random.randint(10, 50)
            print(f"You beat them and have won {profit}")
            hp_gain = random.randint(20, 30)
            total_health = hp_gain + setting.current_health  # Defines health after health gain
            if total_health <= setting.max_health:  # Makes sure current health doesn't exceed max health
                setting.current_health += hp_gain
                print(f"You gain {hp_gain} health, totaling {total_health}")
            elif total_health > setting.max_health:  # If total health is greater than max health, sets health to max
                setting.current_health = setting.max_health
                print(f"Your health goes back to max, which is {setting.max_health}")

                
def the_Great_Kanto_Earthquake(): #the final game code
    print ("september 11th 1923")
    print ("today no one comes up to ask you somthing you decide to enjoy the day")
    print ("as you are cooking lunch over a fire it is around 11:59AM ")
    print ("you hear a rumbling")
    print ("...")
    time.sleep(5)
    print (f"""The ground shook violently, and {name} felt the villa shudder around them.
    In a matter of seconds, the once-steady mountain retreat became a perilous trap""")
    print (f"""With quick thinking, {name} attempted to escape the collapsing villa.
    But as they dashed through the doorway, a massive quake shook the foundation, causing {name} to stumble. 
    In a tragic turn of events, they fell back into the villa,
    right into the open fire they had been cooking over.""")
    print (f"""The quake had ruptured a gas line, and within moments, 
    the villa was engulfed in flames. Trapped among the inferno, 
    {name} was overcome by the blaze. Despite their many adventures and close calls, 
    this unforeseen disaster claimed their life.""")
    print (f"""When the earthquake subsided, 
    the villagers in the valley below noticed a plume of smoke rising from the mountainside. 
    Fearing the worst, they quickly formed search parties and ascended the mountain to MC's villa. 
    Upon arrival, they were met with a heartbreaking sight - the villa, {name} beloved home, was reduced to ashes.""")
    print (f"""The entire village mourned the loss of {name}. 
    They remembered the adventurer not only for their heroic deeds but also for the quiet moments 
    - the times {name} had shared stories of distant lands, helped mend fences, and joined in village celebrations. 
    MC had been more than an adventurer; they had been a friend, a neighbor, and a cherished member of the community.""")
    print (f"""In honor of {name}, the villagers held a solemn and dignified funeral.
    They gathered amidst the ruins of the villa, sharing memories and paying tribute to the life and spirit of {name}. 
    As the funeral pyre burned against the backdrop of the mountains,
    the villagers sang a song of farewell,
    a melody of gratitude and remembrance for an adventurer who had become part of their lives.""")
    print (f"""In the heart of Chiba, a memorial was erected at the site of the villa.
    It stood not only as a testament to {name} adventurous
    spirit but also as a symbol of the bond they had formed with the villagers.
    {name} story, marked by courage, kindness, and a zest for life,
    continued to inspire those who remembered the adventurer who had once called the mountain
    villa their home.""")
    exit()


# driver
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")
game_finished = False
tutorial_question = input(f"{name} would you like to go through the tutorial y/n:>")
money = 0
if tutorial_question == "y":
    tutorial(name)
main_game()