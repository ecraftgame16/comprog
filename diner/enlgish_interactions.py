from menu import *
from common_things import *
import time
def english(great_man, language_selection):
    print ("follow me to your table")
    time.sleep(2)
    menu_select(great_man, language_selection)
    
def menu_select(great_man, language_selection):
    total_price = 0
    orderd_items = []
    while True:
        try:
            which_menu = int(input("""which menue would you like to look at
                                        1 entree
                                        2 sides
                                        3 desserts
                                        4 drinks
                                        5 cheack price
                                        6 leave:>"""))
        except ValueError:
            print("Input Error, please ensure that you only use a number")
            continue
        if which_menu == 1:
            total_price, menu_item = entree_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(english_menu.entree[menu_item]["price"])
        elif which_menu == 2:
            total_price, menu_item = sides_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(english_menu.sides[menu_item]["price"])
        elif which_menu == 3:
            total_price, menu_item = desserts_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(english_menu.desserts[menu_item]["price"])
        elif which_menu == 4:
            total_price, menu_item = drinks_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(english_menu.drinks[menu_item]["price"])
        elif which_menu == 5:
            print(f"your current total price is {total_price}")
        elif which_menu == 6:
            end(total_price, orderd_items, great_man, language_selection)
            break
        else:
            print("Input Error: Please ensure you only enter a number 1-5")

def entree_menu(total_price):
    menu_item = ""
    print("Alright hear is the entree menu")
    number = 0
    for item in english_menu.entree:
        description = english_menu.entree[item]["description"]
        price = "{:,}".format(english_menu.entree[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("would you like to make an order?y/n:>").lower()
        if order == "y":
            try:
                order_num = int(input("which entree would you like to order (please use the number next to your entree):>"))
            except ValueError:
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.lentree)} ")
                return total_price, menu_item
            if 0 < order_num <= len(english_menu.lentree):
                menu_num = order_num - 1
                menu_item = english_menu.lentree[menu_num]
                while True:
                    confirmation  = input(f"so you would like {menu_item}?y/n:>").lower()
                    if confirmation  == "y":
                        total_price_question = total_price + english_menu.entree[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"this will bring your total price up to {total_price_question} would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                print("this will be out soon")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"hear is your {menu_item}")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                print ("allrigt this will not be added to your bill")
                                return total_price, menu_item
                    elif confirmation == "n":
                        print("allright i will not add that to your total")
                        return total_price, menu_item
                    
            else:
                print(f"please ensure that you enter a number from 1-{len(english_menu.lentree)}")
                return total_price, menu_item
            break

        elif order == "n":
            return total_price, menu_item
        else:
            print("please ensure yo use y for yes or n for no")


def sides_menu(total_price):
    menu_item = ""
    print("Alright, here is the sides menu:")
    number = 0
    for item in english_menu.sides:
        description = english_menu.sides[item]["description"]
        price = "{:,}".format(english_menu.sides[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("Would you like to make an order? y/n:>").lower()
        if order == "y":
            try:
                order_num = int(input("Which side would you like to order (please use the number next to your side):>"))
            except ValueError:
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.lsides)} ")
                return total_price, menu_item
            if 0 < order_num <= len(english_menu.lsides):
                menu_num = order_num - 1
                menu_item = english_menu.lsides[menu_num]
                while True:
                    confirmation = input(f"So you would like {menu_item}? y/n:>").lower()
                    if confirmation == "y":
                        total_price_question = total_price + english_menu.sides[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"This will bring your total price up to {total_price_question}. Would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                print("This will be out soon.")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"Here is your {menu_item}.")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                print("Alright, this will not be added to your bill.")
                                return total_price, menu_item
                    elif confirmation == "n":
                        print("Alright, I will not add that to your total.")
                        return total_price, menu_item
            else:
                print(f"Please ensure that you enter a number from 1-{len(english_menu.lsides)}")
                return total_price, menu_item
            break

        elif order == "n":
            return total_price, menu_item
        else:
            print("Please ensure you use 'y' for yes or 'n' for no.")

def desserts_menu(total_price):
    menu_item = ""
    print("Alright, here is the desserts menu:")
    number = 0
    for item in english_menu.desserts:
        description = english_menu.desserts[item]["description"]
        price = "{:,}".format(english_menu.desserts[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("Would you like to make an order? y/n:>").lower()
        if order == "y":
            try:
                order_num = int(input("Which dessert would you like to order (please use the number next to your dessert):>"))
            except ValueError:
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.ldesserts)} ")
                return total_price, menu_item
            if 0 < order_num <= len(english_menu.ldesserts):
                menu_num = order_num - 1
                menu_item = english_menu.ldesserts[menu_num]
                while True:
                    confirmation = input(f"So you would like {menu_item}? y/n:>").lower()
                    if confirmation == "y":
                        total_price_question = total_price + english_menu.desserts[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"This will bring your total price up to {total_price_question}. Would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                print("This will be out soon.")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"Here is your {menu_item}.")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                print("Alright, this will not be added to your bill.")
                                return total_price, menu_item
                    elif confirmation == "n":
                        print("Alright, I will not add that to your total.")
                        return total_price, menu_item
            else:
                print(f"Please ensure that you enter a number from 1-{len(english_menu.ldesserts)}")
                return total_price, menu_item
            break

        elif order == "n":
            return total_price, menu_item
        else:
            print("Please ensure you use 'y' for yes or 'n' for no.")


def drinks_menu(total_price):
    menu_item = ""
    print("Alright, here is the drinks menu:")
    number = 0
    for item in english_menu.drinks:
        description = english_menu.drinks[item]["description"]
        price = "{:,}".format(english_menu.drinks[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("Would you like to make an order? y/n:>").lower()
        if order == "y":
            try:
                order_num = int(input("Which drink would you like to order (please use the number next to your drink):>"))
            except ValueError:
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.ldrinks)} ")
                return total_price, menu_item
            if 0 < order_num <= len(english_menu.ldrinks):
                menu_num = order_num - 1
                menu_item = english_menu.ldrinks[menu_num]
                while True:
                    confirmation = input(f"So you would like {menu_item}? y/n:>").lower()
                    if confirmation == "y":
                        total_price_question = total_price + english_menu.drinks[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"This will bring your total price up to {total_price_question}. Would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                print("This will be out soon.")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"Here is your {menu_item}.")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                print("Alright, this will not be added to your bill.")
                                return total_price, menu_item
                    elif confirmation == "n":
                        print("Alright, I will not add that to your total.")
                        return total_price, menu_item
            else:
                print(f"Please ensure that you enter a number from 1-{len(english_menu.ldrinks)}")
                return total_price, menu_item
            break

        elif order == "n":
            return total_price, menu_item
        else:
            print("Please ensure you use 'y' for yes or 'n' for no.")


def end(total_price, orderd_items, great_man, language_selection):
    print("allright hear is your bill")
    print("hear is your itdiomised bill")
    print(f"hear is what you orderd {orderd_items}")
    print(f"hear is your total price {total_price}")
    while True:
        try:
            payment_method = int(input("how would you like to pay card or cash? 1 for cash 2 for card:>"))
            break
        except ValueError:
            print("Imput Error: please ensure that you only imput 1 for cash 2 for card")
            continue
    while True:
        if payment_method == 1:
            tip_question = input("would you like to tip?y/n:>")
            if tip_question == "y":
                try:
                    amount = int(input("how much would you like to tip?")) 
                except ValueError:
                    print("please ensure you use numbers and nothing ealse")
                    continue
                print(f"""you leave the diner when a waiter starts to chase you down with the tip you left
                          he catches up to you and tells you, you overpayed sir hear is your change
                          you take your change back in amount of {amount}""")
                break
            elif tip_question == "n":
                print("you pay and leave")
                break
        elif payment_method == 2:
            if tip_question == "y":
                try:
                    amount = int(input("how much would you like to tip?"))    
                except ValueError:
                    print("please ensure you use numbers and nothing ealse")
                    continue
                print("""you wave down the waiter saying there is no option to tip
                         the waiter calmly informs you that in japan tiping is not 
                         common and to some is considerd rude""")
                break
            elif tip_question == "n":
                print("you pay and leave")
                break
    print(great_man())

    exit()