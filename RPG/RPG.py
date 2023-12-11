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
    day = 0
    while seting.curent_helth > 0 and game_finished == False:
        if day_start == True:
            day += 1
            if day == 5:
                the_Great_Kanto_Earthquake()
            walked_times = 0
            arived = False
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
        else: #main functions 
            #when player has walked 70 times they arive at there destination
            if walked_times >= 70 and arived == False: 
                arived = True
                print("you have arived and done your task")
                print ("time to return home")
                walked_times = 0 #resets walk time for the return walk
            #cheacks if the player has both arived and walked 70 more times
            elif walked_times >= 70 and arived == True:
                print ("we made it home finaly")
                day_start = True
                continue
            action = input("""what would you like to do w - walk i - inventory:>""")
            #makes walking work and calles atacks
            if action == "w":
                walked_times += 1     
                atack = random.randint (1,3)
                if atack == 2: #if the number selected is 2 starts the atack option
                    atacker = random.choice(seting.lEnimies)#selects the ename
                    print(f"ohh no a foe has apperd it is a {atacker} hear is a discription") #discribies the ename
                    print(seting.enimies[atacker]['discription'])
                    run_atack = input("would you like to try and run - r or atack - a:>")#asks if player wants to run or atack
                    if run_atack == "a": 
                        atack_player_first(atacker) #calls atack where player atacks first since they chose atack
                    elif run_atack == "r":
                        sucess = random.randint(1,50)
                        if sucess % 2 == 0: #cheacks if player ran away susscessfully
                            print ("you got away")
                            continue
                        else: #if player didn't run away succsefuly tels player and calles the enime atacking first
                            print("you couldn't run away")
                            atack_enimie_first(atacker)
            elif action == "i": #runs invetory cheack
                print(f"you have {inventory} in your inventory")
                print(f"you have {money} curent money")
                print(f"your health is {seting.curent_helth}/{seting.max_health}")
            else: #error cheack 
                print("invalid input please use i for inventory or w for walking")

def task_selection():#selects tasks
    tasks_asked = []  # Keep track of asked tasks
    while True:
        task_number = random.randint(1, 5)
        if task_number not in tasks_asked:  # Check if the task has not been asked before
            tasks_asked.append(task_number)  # Add the new task to the list
            break  # Exit the loop once a new task is found
    
    #calling the tasks from tasks.py
    print("A local villiger comes up to you and asks ...")
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

#function called when player choses atack
def atack_player_first(atacker):
    enime_helth = random.randint (seting.enimies[atacker]["health minumim"],seting.enimies[atacker]["health maxumim"])
    not_run = True
    while enime_helth > 0 and seting.curent_helth > 0 and not_run == True:
        #player's atack
        if seting.curent_helth > 0:
            run_atack = input("would you like to atack or runaway? a - atack r - run:>")
            if run_atack == "a":
                hero_damage = random.randint(30,60)
                enime_helth -= hero_damage
                print (f"you do {hero_damage} damage")
            elif run_atack == "r":
                sucess = random.randint(1,50)
                if sucess % 2 == 0:
                    print ("you got away")
                    not_run = False
                else:
                    print("you couldn't run away")
        
        #enime's atack
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

#the function called when the player runs and fails
def atack_enimie_first(atacker):
    #enime's atack
    enime_helth = random.randint (seting.enimies[atacker]["health minumim"],seting.enimies[atacker]["health maxumim"])
    not_run = True
    while enime_helth > 0 and seting.curent_helth > 0 and not_run == True:
        if enime_helth > 0 and not_run == True:
            enime_damage = random.randint(seting.enimies[atacker]["dammage minum"],seting.enimies[atacker]["dammage maximum"])
            print (f"you got hit you took {enime_damage} damage")
            seting.curent_helth -= enime_damage
        
        #player's atack
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

        if seting.curent_helth <= 0: #cheaks if player is dead
            print("You have died and faild the mission sorry")
            exit()

        if enime_helth <= 0: #cheaks if enamy is defeted
            profit = random.randint(10, 50)
            print (f"you beat them you have won {profit}")
            hp_gain = random.randint (20, 30)
            total_health = hp_gain + seting.curent_helth #defins health after health gain
            if total_health <= seting.max_health: #makes sure curent health dosent excied max health
                seting.curent_helth += hp_gain
                print(f"you gain {hp_gain} health totaling {total_health}")
            elif total_health > seting.max_health: #if total health greater than max health sets health to max
                seting.curent_helth = seting.max_health
                print(f"your health goes back to max which is {seting.max_health}")

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


#driver
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")
game_finished = False
tutorial_question = input(f"{name} would you like to go though the tutrial y/n:>")
money = 0
if tutorial_question == "y":
    tutorial(name)
main_game()
