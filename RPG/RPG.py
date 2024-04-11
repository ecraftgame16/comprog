# imports
import random
import time
from seting import *
from tasks import *
from dev_comands import dev_comands
from tutorial import tutorial

#variables
game_finished = False


# game code
def main_game():
    inventory = []
    do_combat = True
    money = 10
    day_start = True  # makes new day true for start of while loop
    day = 0
    password_got = False
    waiting = True
    defense = 0
    extra_attack = 0
    attack_equiped = False
    defense_equiped = False
    equiped_item_attack = ""
    equiped_item_defense = ""
    while setting.current_health > 0 and game_finished == False:
        if day_start == True:
            day += 1
            if day == 5:
                the_Great_Kanto_Earthquake(waiting)
            walked_times = 0
            arrived = False
            if day > 1:
                setting.max_health += 50
            setting.current_health = setting.max_health
            task_selection(waiting)
            accept = input(f"{name} will you take on this task y/n:>")
            if accept == "y":
                day_start = False
            elif accept == "n":
                print("you laze around for the day")
                print("...")
                if waiting == True:
                    time.sleep(10)
                print("it is now the next day")
                if waiting == True:    
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
                        if waiting == True:
                            time.sleep(10)
                        print("it is now the next day")
                        if waiting == True:
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
                new_item = random.choice(setting.l_decoration_items)
                inventory.append(new_item)
                inventory.append(setting.items_decoration[new_item])
                continue
            test = input ("shop y/n") #debug temp shop access
            if test == "y": #debug temp shop access
                inventory, money = shop(inventory, money) #debug temp shop access
            action = input("""what would you like to do w - walk i - inventory:>""")
            # makes walking work and calls attacks
            if action == "w":
                walked_times += 1
                attack = random.randint(1, 3)
                shop_true = random.randint(1, 50)
                if attack == 2 and do_combat == True:  # if the number selected is 2 starts the attack option and combat is not dissabled from dev commands
                    attacker = random.choice(setting.lEnemies)  # selects the enemy
                    print(f"oh no a foe has appeared it is a {attacker} here is a description")  # describes the enemy
                    print(setting.enemies[attacker]['description'])
                    attack_dicision = True
                    while attack_dicision == True:
                        run_attack = input("would you like to try and run - r or attack - a:>")  # asks if player wants to run or attack
                        if run_attack == "a":
                            attack_dicision = False
                            money = attack_player_first(attacker, money, extra_attack, defense)  # calls attack where player attacks first since they chose attack
                        elif run_attack == "r":
                            success = random.randint(1, 50)
                            if success % 2 == 0:  # checks if player ran away successfully
                                attack_dicision = False
                                print("you got away")
                                continue
                            else:  # if player didn't run away successfully tells player and calls the enemy attacking first
                                attack_dicision = False
                                print("you couldn't run away")
                                money = attack_enemy_first(attacker, money, extra_attack, defense)
                        else:
                            print("make sure you use a for attack and r for run")
                if shop_true == 8:
                    indeciveness = True
                    if indeciveness:
                        shop_q = input("would you like to go to the shop? y/n:>")
                        if shop_q == "y":
                            inventory, money = shop(inventory, money)
                            indeciveness = False
                        elif shop_q == "n":
                            print("you continue on")
                            indeciveness = False
                        else:
                            print("please ensure that you enter y for yes n for no and nothing ealse")
                        
            elif action == "i":  # runs inventory check
                defense, extra_attack = inventory_manegment(inventory, money, extra_attack, defense, attack_equiped, defense_equiped, equiped_item_attack, equiped_item_defense)
            elif action == "dc":
                if password_got == True:
                    inventory, day, do_combat, money, password_got, waiting = dev_comands(inventory, day, do_combat, money, password_got, waiting, tutorial, name)
                elif password_got == False:
                    password_guess = input("what is the password for dev comands?")
                    if password_guess == setting.DEV_PASSWORD:
                        password_got = True
                        inventory, day, do_combat, money, password_got, waiting = dev_comands(inventory, day, do_combat, money, password_got, waiting, tutorial, name)
                    else:
                        print ("password incorect")
            else:  # error check
                print("invalid input please use i for inventory or w for walking")

def task_selection(waiting):  # selects tasks
    tasks_asked = []  # Keep track of asked tasks
    while True:
        task_number = random.randint(1, 5)
        if task_number not in tasks_asked:  # Check if the task has not been asked before
            tasks_asked.append(task_number)  # Add the new task to the list
            break  # Exit the loop once a new task is found

    # calling the tasks from tasks.py
    print("A local villager comes up to you and asks ...")
    if waiting == True:    
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
def attack_player_first(attacker, money, extra_attack, defense):
    enemy_health = random.randint(setting.enemies[attacker]["health minimum"], setting.enemies[attacker]["health maximum"])
    not_run = True
    while enemy_health > 0 and setting.current_health > 0 and not_run == True:
        # Player's attack
        if setting.current_health > 0:
            run_attack = input("Would you like to attack or run away? a - attack, r - run:>")
            if run_attack == "a":
                hero_damage = random.randint(30,60)
                hero_damage += extra_attack
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
            enemy_damage -= defense
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
            money += profit #calculates new money
            if total_health <= setting.max_health:
                setting.current_health += hp_gain
                print(f"You gain {hp_gain} health, totaling {total_health}")
            elif total_health > setting.max_health:
                setting.current_health = setting.max_health
                print(f"Your health goes back to max, which is {setting.max_health}")
            return money #sends new total back
                

# Function called when the player runs and fails
def attack_enemy_first(attacker, money, extra_attack, defense):
    # Enemy's attack
    enemy_health = random.randint(setting.enemies[attacker]["health minimum"], setting.enemies[attacker]["health maximum"])
    not_run = True
    while enemy_health > 0 and setting.current_health > 0 and not_run == True:
        if enemy_health > 0 and not_run == True:
            enemy_damage = random.randint(setting.enemies[attacker]["damage minimum"], setting.enemies[attacker]["damage maximum"])
            enemy_damage -= defense
            print(f"You got hit and took {enemy_damage} damage")
            setting.current_health -= enemy_damage
        
        # Player's attack
        if setting.current_health > 0:
            run_attack = input("Would you like to attack or run away? a - attack, r - run:>")
            if run_attack == "a":
                hero_damage = random.randint(20,40)
                hero_damage += extra_attack
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
            money += profit #caclulated money total
            if total_health <= setting.max_health:  # Makes sure current health doesn't exceed max health
                setting.current_health += hp_gain
                print(f"You gain {hp_gain} health, totaling {total_health}")
            elif total_health > setting.max_health:  # If total health is greater than max health, sets health to max
                setting.current_health = setting.max_health
                print(f"Your health goes back to max, which is {setting.max_health}")
            return money #sends new total back

def inventory_manegment(inventory, money, extra_attack, defense, attack_equiped, defense_equiped, equiped_item_attack, equiped_item_defense):
    print(f"you have {inventory} in your inventory")
    print(f"you have {money} current money")
    print(f"your health is {setting.current_health}/{setting.max_health}")
    print(f"you curently have equieped{equiped_item_attack} for atacking and {equiped_item_defense} for your defense")
    equip = input("would you like to equip an item y/n:>")
    if equip == "y":
        chosen_item = input("what would you like to equip it must be an attack type or defense type")
        if chosen_item in setting.items_defense:
            if defense_equiped == True:
                acknlodge = input("you allready have an item equiepd for defense would you like to equip a new item unequiping the other item y/n:>")
                if acknlodge == "y":
                    defense_attack = "defense"
                    defense, extra_attack = unequip_item(defense, extra_attack, defense_attack)
                    defense, extra_attack = item_efficetiveness(inventory, chosen_item, defense, extra_attack)
                    print(f"{chosen_item} has been equiped")
                elif acknlodge == "n":
                    print("wont equip item leaving the other one equiped")
            elif defense_equiped == False:
                item_efficetiveness(inventory, chosen_item, defense, extra_attack, equiped_item_attack, equiped_item_defense)
                print(f"{chosen_item} has been equiped")
            elif attack_equiped == True:
                acknlodge = input("you allready have an item equiepd for attack would you like to equip a new item unequiping the other item y/n:>")
                if acknlodge == "y":
                    defense_attack = "attack"
                    defense, extra_attack = unequip_item(defense, extra_attack, defense_attack)
                    defense, extra_attack, equiped_item_attack, equiped_item_defense = item_efficetiveness(inventory, chosen_item, defense, extra_attack, equiped_item_attack, equiped_item_defense)
                    print(f"{chosen_item} has been equiped")
                elif acknlodge == "n":
                    print("wont equip item leaving the other one equiped")
            elif attack_equiped == False:
                defense, extra_attack, equiped_item_attack, equiped_item_defense = item_efficetiveness(inventory, chosen_item, defense, extra_attack, equiped_item_attack, equiped_item_defense)
                print(f"{chosen_item} has been equiped")
    elif equip == "n":
        unequip_question = input("would you like to unequip an item y/n:>")
        if unequip_question == "y":
            which_item_unequip = input("which item would you like to unequip d for defense item a for attack item:>")
            if which_item_unequip == "a":
                defense_attack = "attack"
                defense, extra_attack = unequip_item(defense, extra_attack, defense_attack)
            elif which_item_unequip == "d":
                defense_attack = "defense"
                defense, extra_attack = unequip_item(defense, extra_attack, defense_attack)
        elif unequip_question == "n":
            healing_question = input("Would you like to use a healing item?y/n:>")
            if healing_question == "y":
                healing_func(inventory)
    return defense, extra_attack


def item_efficetiveness(inventory, chosen_item, defense, extra_attack, equiped_item_attack, equiped_item_defense):
    if chosen_item in setting.items_attack and chosen_item in inventory:
        new_attack = random.randint(setting.items_attack[chosen_item]["attack_bonus_min"], setting.items_attack[chosen_item]["attack_bonus_max"])
        new_defense = 0
        defense, extra_attack, new_defense, new_attack = item_effects(defense, new_defense, extra_attack, new_attack)
        equiped_item_attack = chosen_item
    elif chosen_item in setting.items_defense and chosen_item in inventory:
        new_defense = random.randint(setting.items_defense[chosen_item]["defense_bonus_min"], setting.items_defense[chosen_item]["defense_bonus_max"])
        new_attack = 0
        defense, extra_attack, new_defense, new_attack = item_effects(defense, new_defense, extra_attack, new_attack)
        equiped_item_defense = chosen_item
    else:
        print("Either the item does not exist or it is not in your inventory. Here is your current inventory")
        print(inventory)
    return defense, extra_attack, equiped_item_attack, equiped_item_defense

def item_effects(defense, new_defense, extra_attack, new_attack):
    if new_defense != 0:
        defense = new_defense
        new_attack = 0
    if new_attack != 0:
        extra_attack = new_attack
        new_defense = 0
    new_defense = 0
    new_attack = 0
    return defense, extra_attack, new_defense, new_attack

def unequip_item(defense, extra_attack, defense_attack):
    if defense_attack == "attack":
        extra_attack = 0
    if defense_attack == "defense":
        defense = 0
    return defense, extra_attack

def healing_func(inventory):
    try:
        heal_type = int(input("""would you like to use a small medium or large heal pack
                            1 small
                            2 medium
                            3 large"""))
    except ValueError:
        print("invalid input please make sure you only have a 1 2 or 3")
    else:
        if heal_type == 1:
            healing_box = "small_heal_pack"
        elif heal_type == 2:
            healing_box = "medium_heal_pack"
        elif heal_type == 3:
            healing_box = "large_heal_pack"
        else:
            print("please make sure the input is eather 1 2 or 3")
            return
        if healing_box in inventory:
            extra_health = random.randint(setting.items_heal[healing_box]["healing power min"], setting.items_heal[healing_box]["healing power max"])
            if setting.current_health == setting.max_health:
                print("you are allready at max health which you cannot exceed")
            elif setting.current_health + extra_health >= setting.max_health:
                are_you_sure_question = input(f"using this heal would bring you above or equal to max health your curent health is {setting.current_health} and the max is {setting.max_health} this heal pack would heal you {extra_health} y/n:>")
                if are_you_sure_question == "y":
                    setting.current_health = setting.max_health
                    inventory.remove(healing_box)
                    inventory.remove(setting.items_heal[healing_box])
            else:
                setting.current_health += extra_health
                print(f"you have been heald {extra_health} much totaling {setting.current_health} out of a max of {setting.max_health}")
                inventory.remove(healing_box)
                inventory.remove(setting.items_heal[healing_box])
        else:
            print("you dont have that healing box in your inventory hear is your inventory again")
            print(inventory)

def shop(inventory, money):
    print("hello adventrure, welcome to the shop")
    healing_gen = []
    attack_gen = []
    defense_gen = []
    decoration_gen = []
    healing_gen, attack_gen, defense_gen, decoration_gen = shop_generation(healing_gen, attack_gen, defense_gen, decoration_gen)
    shop_loop = True
    while shop_loop == True:
        try:
            shop_action = int(input("""what would you like to do
                                    1 sell your items
                                    2 buy some items
                                    3 leave the store:>"""))
        except ValueError:
            print("please make sure you enter a 1, 2, or 3 and nothing elase")
        else:
            if shop_action == 1:
                inventory, money = selling_your_items(inventory, money)
            elif shop_action == 2:
                inventory, money, healing_gen, attack_gen, defense_gen, decoration_gen = buying_items(inventory, money, healing_gen, attack_gen, defense_gen, decoration_gen)
            elif shop_action == 3:
                shop_loop = False
    return inventory, money

def shop_generation(healing_gen, attack_gen, defense_gen, decoration_gen):
    filled = False
    while filled == False:
        item_attack = random.choice(setting.l_attack_items)
        if item_attack not in attack_gen:
            attack_gen.append(item_attack)
        if len(attack_gen) == 3:
            filled = True
    filled = False
    while filled == False:
        items_defense = random.choice(setting.l_defense_items)
        if items_defense not in defense_gen:
            defense_gen.append(items_defense)
        if len(defense_gen) == 3:
            filled = True
    filled = False
    while filled == False:
        items_heal = random.choice(setting.l_healing_items)
        if items_heal not in healing_gen:
            healing_gen.append(items_heal)
        if len(healing_gen) == 3:
            filled = True
    filled = False
    while filled == False:
        items_decoration = random.choice(setting.l_decoration_items)
        if items_decoration not in decoration_gen:
            decoration_gen.append(items_decoration)
        if len(decoration_gen) == 3:
            filled = True
    return healing_gen, attack_gen, defense_gen, decoration_gen

def selling_your_items(inventory, money):
    # money = old_money
    print("""shopkeeper:
                        I see you are intrested in selling something to me.""")
    print(inventory)
    item_sold = input("what would you like to offer?:>")
    if item_sold in inventory:
        if item_sold in setting.items_attack:
            loss = random.randint(1,5)
            original_cost = setting.items_attack[item_sold]["cost"]
            offered_price = original_cost // loss
            item_type = "attack"
        elif item_sold in setting.items_defense:
            loss = random.randint(1,5)
            original_cost = setting.items_defense[item_sold]["cost"]
            offered_price = original_cost // loss
            item_type = "defense"
        elif item_sold in setting.items_heal:
            loss = random.randint(1,5)
            original_cost = setting.items_heal[item_sold]["cost"]
            offered_price = original_cost // loss
            item_type = "heal"
        elif item_sold in setting.items_decoration:
            loss = random.randint(1,5)
            original_cost = setting.items_decoration[item_sold]["cost"]
            offered_price = original_cost // loss
            item_type = "decoration"
        else:
            print("unable to find item")
            # old_money = money
            return inventory, money
        
        confirmation = input(f"""shopkeeper:
                                    i will offer you this at a price of {offered_price} 
                                    you think to your self you bought this for {original_cost}
                                shopkeeper:
                                    will you accept my offer? y/n:>""")
        decide = True
        while decide == True:
            if confirmation == "y":
                money += offered_price
                inventory.remove(item_sold)
                if item_type == "attack":
                    inventory.remove(setting.items_attack[item_sold])
                if item_type == "defense":
                    inventory.remove(setting.items_defense[item_sold])
                if item_type == "heal":
                    inventory.remove(setting.items_heal[item_sold])
                if item_type == "decoration":
                    inventory.remove(setting.items_decoration[item_sold])
                decide = False
            elif confirmation == "n":
                print("you turn the shop keeper down")
                decide = False
            else:
                print("please make sure you input y for yes and n for no lowercase")
        return inventory, money

    else:
        print("item not in inventory")
        return inventory, money

def buying_items(inventory, money, healing_gen, attack_gen vbnen,defense_gen,decoration_gen):
    print(""" Shopkeeper:
                        I see you would like to buy something.""")
    print (f"attack type {attack_gen}")
    print (f"defense type {defense_gen}")
    print (f"healing type {healing_gen}")
    print (f"decoration type {decoration_gen}")
    try:
        buy_type = int(input("""what type of item would you like to buy
                        1 attack
                        2 defense
                        3 healing
                        4 decoration:>"""))
    except ValueError:
        print("please ensure your input is a nuber 1 2 3 or 4 note there shouledt be anything like a space or anything")
    else:
        bought_item = ""
        if buy_type == 1:
            item_details = input("would you like to see more details for an item y/n?:>")
            if item_details == "y":
                item_cheack = input("which item would you like to see the details of:>")
                if item_cheack in setting.items_attack:
                    print(setting.items_attack[item_cheack])
                else:
                    print("item not found please try again")
                    return
                item_buy = input("would you like to buy the item y/n:>")
                if item_buy == "y":
                    buy_script = True
                    bought_item = item_cheack
                elif item_buy == "n":
                    buy_script = False
            elif item_details == "n":
                buy_script = True
            else:
                print("error, invalid input please ensure you only enter y for yes n for no")
                return
            if buy_script == True:
                if bought_item == "":
                    bought_item = input("what would you like to buy:>")
                if bought_item in attack_gen:
                    if money >= setting.items_attack[bought_item]["cost"]:
                        inventory.append(bought_item)
                        inventory.append(setting.items_attack[bought_item])
                        attack_gen.remove(bought_item)
                        money -= setting.items_attack[bought_item]["cost"]
                        print(f"you have succesfully bought {bought_item}")
                    elif money < setting.items_attack[bought_item]["cost"]:
                        print("you do not have enough money for this object")
                else:
                    print("item not avaible") 
        elif buy_type == 2:
            item_details = input("would you like to see more details for an item y/n?:>")
            if item_details == "y":
                item_cheack = input("which item would you like to see the details of:>")
                if item_cheack in setting.items_defense:
                    print(setting.items_defense[item_cheack])
                else:
                    print("item not found please try again")
                    return
                item_buy = input("would you like to buy the item y/n:>")
                if item_buy == "y":
                    buy_script = True
                    bought_item = item_cheack
                elif item_buy == "n":
                    buy_script = False
            elif item_details == "n":
                buy_script = True
            else:
                print("error, invalid input please ensure you only enter y for yes n for no")
                return
            if buy_script == True:
                if bought_item == "":
                    bought_item = input("what would you like to buy:.")
                if bought_item in defense_gen:
                    if money >= setting.items_defense[bought_item]["cost"]:
                        inventory.append(bought_item)
                        inventory.append(setting.items_defense[bought_item])
                        defense_gen.remove(bought_item)
                        money -= setting.items_defense[bought_item]["cost"]
                        print(f"you have succesfully bought {bought_item}")
                    elif money < setting.items_defense[bought_item]["cost"]:
                        print("you do not have enough money for this object")
                else:
                    print("item not avaible") 
        elif buy_type == 3:
            item_details = input("would you like to see more details for an item y/n?:>")
            if item_details == "y":
                item_cheack = input("which item would you like to see the details of:>")
                if item_cheack in setting.items_heal:
                    print(setting.items_heal[item_cheack])
                else:
                    print("item not found please try again")
                    return
                item_buy = input("would you like to buy the item y/n:>")
                if item_buy == "y":
                    buy_script = True
                    bought_item = item_cheack
                elif item_buy == "n":
                    buy_script = False
            elif item_details == "n":
                buy_script = True
            else:
                print("error, invalid input please ensure you only enter y for yes n for no")
                return
            if buy_script == True:
                if bought_item == "":
                    bought_item = input("what would you like to buy:>")
                if bought_item in healing_gen:
                    if money >= setting.items_heal[bought_item]["cost"]:
                        inventory.append(bought_item)
                        inventory.append(setting.items_heal[bought_item])
                        healing_gen.remove(bought_item)
                        money -= setting.items_heal[bought_item]["cost"]
                        print(f"you have succesfully bought {bought_item}")
                    elif money < setting.items_heal[bought_item]["cost"]:
                        print("you do not have enough money for this object")
                else:
                    print("item not avaible") 
        elif buy_type == 4:
            item_details = input("would you like to see more details for an item y/n?:>")
            if item_details == "y":
                item_cheack = input("which item would you like to see the details of:>")
                if item_cheack in setting.items_decoration:
                    print(setting.items_decoration[item_cheack])
                else:
                    print("item not found please try again")
                    return
                item_buy = input("would you like to buy the item y/n:>")
                if item_buy == "y":
                    buy_script = True
                    bought_item = item_cheack
                elif item_buy == "n":
                    buy_script = False
            elif item_details == "n":
                buy_script = True
            else:
                print("error, invalid input please ensure you only enter y for yes n for no")
                return
            if buy_script == True:
                if bought_item == "":
                    bought_item = input("what would you like to buy:>")
                if bought_item in decoration_gen:
                    if money >= setting.items_decoration[bought_item]["cost"]:
                        inventory.append(bought_item)
                        inventory.append(setting.items_decoration[bought_item])
                        decoration_gen.remove(bought_item)
                        money -= setting.items_decoration[bought_item]["cost"]
                        print(f"you have succesfully bought {bought_item}")
                    elif money < setting.items_decoration[bought_item]["cost"]:
                        print("you do not have enough money for this object")
                else:
                    print("item not avaible")
    return inventory, money, healing_gen, attack_gen, defense_gen, decoration_gen

                
def the_Great_Kanto_Earthquake(waiting): #the final game code
    print ("september 1st 1923")
    print ("today no one comes up to ask you somthing you decide to enjoy the day")
    print ("as you are cooking lunch over a fire it is around 11:59AM ")
    print ("you hear a rumbling")
    print ("...")
    if waiting == True:
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
    Fearing the worst, they quickly formed search parties and ascended the mountain to {name}'s villa. 
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
print ("you wake up in your villa in Chiba Japan just as you have done almost evryday in you adult life you look over the mountain seeing the village down it is the 27th of augest a brand new day")
print ("you recently lost most of your money gambling and you are left with a mesly 10 coins")
name = input("hello adventurer welcome, now please tell me adventurer what is your name?:>")
tutorial_question = input(f"{name} would you like to go through the tutorial y/n:>")
if tutorial_question == "y":
    tutorial(name)
main_game()