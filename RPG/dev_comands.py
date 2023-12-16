from seting import *
import sys
def dev_comands(inventory, day, do_combat, money, password_got):
    print ("hello and welcome to the testing termanal")
    exit = False
    while exit == False:
        try:
            comand = int(input ("""what varable would you like to change
                    1 exit dev commands
                    2 helth
                    3 max helth
                    4 inventory
                    5 disable combat
                    6 re enable combat
                    7 day
                    8 money
                    9 end
                    10 lock dev consol behind password again:>"""))
        except ValueError:
            print("please insert a intager with nothing ealse")
        if comand == 1:
            exit = True
            print ("exiting dev commands")
        elif comand == 2:
            # old_health = 0
            # setting.current_health = old_health
            try:
                new_health = int(input(f"what is the new health must be below max_health which is {setting.max_health}:> "))
                if new_health > setting.max_health:
                    print(f"Unable must be below max health which is {setting.max_health}")
                else:
                    setting.current_health = new_health
            except ValueError:
                print("Please insert an integer nothing else")
        elif comand == 3:
            try:
                setting.max_health = int(input("what would you like the max health to be:>"))
            except ValueError:
                print("please insert a integer nothing ealse")
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
                day = day_proposed
            else:
                print("no days past 5 days")
        elif comand == 8:
            try:
                money = int(input("what will the players new money be (what ever number you enter is the total)"))
            except ValueError:
                print("please insert a integer nothing ealse")
        elif comand == 9:
            end_confermation = input("are you sure you want to end the program y/n:>")
            if end_confermation == "y":
                sys.exit()
        elif comand == 10:
            password_got = False
        else:
            print("please insert a valid number")
    return inventory, day, do_combat, money, password_got