from seting import *
from rpg import *
def dev_comands():
    print ("hello and welcome to the testing termanal")
    exit = False
    while exit == False:
        comand = int(input ("""what varable would you like to change
                1 exit dev commands
                2 helth
                3 max helth
                4 inventory
                5 disable combat
                6 re enable combat
                7 day:>"""))
        if comand == 1:
            exit = True
            print ("exiting dev commands")
        elif comand == 2:
            old_health = 0
            setting.current_health = old_health
            setting.current_health = int(input(f"what is the new health must be below max_health which is {setting.max_health}:>"))
            if setting.current_health > setting.max_health:
                print (f"unable must be below max health whitch is {setting.max_health}")
        elif comand == 3:
            setting.max_health = int(input("what would you like the max health to be:>"))
            max_current = input("would you like to set current health to the new max health y/n:>")
            if max_current == "y":
                setting.current_health = setting.max_health
        elif comand == 4:
            print(f"current inventory = {inventory}")
            inventory_edit = True
            while inventory_edit == True:
                new_item = input(f"what would you like to add {setting.items_decoration}")
                if new_item in setting.items_decoration:
                    inventory.append(setting.items_decoration[new_item])
                else:
                    print("no item named that found")
                exit_invetory_loop = input("do you want to add more items to the inventory y/n:>")
                if exit_invetory_loop == "y":
                    inventory_edit = False
                    print("exiting inventory editor")
        elif comand == 5:
            do_combat = False
            print ("combat is now dissabled")
        elif comand == 6:
            do_combat = True
        elif comand == 7:
            day_proposed = int(input("what day do you want up to 5"))
            if day_proposed <= 5:
                day = 5