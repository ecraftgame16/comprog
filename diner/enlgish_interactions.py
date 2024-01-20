from menu import *
from common_things import *
import time
def english():
    print ("follow me to you table")
    time.sleep(2)
    menu_select()
    
def menu_select():
    total_price = 0
    orderd_items = []
    while True:
        try:
            which_menu = int(input("""which menue would you like to look at
                                        1 entree
                                        2 sides
                                        3 desserts
                                        4 drinks
                                        5 leave:>"""))
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
            end(total_price, orderd_items)
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
    order = input("would you like to make an order?y/n:>")
    if order == "y":
        try:
            order_num = int(input("which entree would you like to order (please use the number next to your entree):>"))
        except ValueError:
            print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.lentree)} ")
            return total_price, menu_item
        if 0 < order_num <= len(english_menu.lentree):
            menu_num = order_num - 1
            menu_item = english_menu.lentree[menu_num]
            confirmation  = input(f"so you would like {menu_item}?y/n:>")
            if confirmation  == "y":
                total_price_question = total_price + english_menu.entree[menu_item]["price"]
                price_confirmation = input(f"this will bring your total price up to {total_price_question} would you like to continue this order? y/n:>")
                if price_confirmation == "y":
                    print("this will be out soon")
                    total_price = total_price_question
                    time.sleep(5)
                    print(f"hear is your {menu_item}")
                    return total_price, menu_item
            elif confirmation == "n":
                print("allright i will not add that to your total")
                return total_price, menu_item

    elif order == "n":
        return total_price, menu_item


def sides_menu(total_price):
    menu_item = ""
    print("Alright hear is the sides menu")
    number = 0
    for item in english_menu.sides:
        description = english_menu.sides[item]["description"]
        price = "{:,}".format(english_menu.sides[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    order = input("would you like to make an order?y/n:>")
    if order == "y":
        try:
            order_num = int(input("which side would you like to order (please use the number next to your side):>"))
        except ValueError:
            print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.lsides)} ")
            return total_price, menu_item
        if 0 < order_num <= len(english_menu.lsides):
            menu_num = order_num - 1
            menu_item = english_menu.lsides[menu_num]
            confirmation  = input(f"so you would like {menu_item}?y/n:>")
            if confirmation  == "y":
                total_price_question = total_price + english_menu.sides[menu_item]["price"]
                price_confirmation = input(f"this will bring your total price up to {total_price_question} would you like to continue this order? y/n:>")
                if price_confirmation == "y":
                    print("this will be out soon")
                    total_price = total_price_question
                    time.sleep(5)
                    print(f"hear is your {menu_item}")
                    return total_price, menu_item
            elif confirmation == "n":
                print("allright i will not add that to your total")
                return total_price, menu_item

    elif order == "n":
        return total_price, menu_item

def desserts_menu(total_price):
    menu_item = ""
    print("Alright hear is the desserts menu")
    number = 0
    for item in english_menu.desserts:
        description = english_menu.desserts[item]["description"]
        price = "{:,}".format(english_menu.desserts[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    order = input("would you like to make an order?y/n:>")
    if order == "y":
        try:
            order_num = int(input("which dessert would you like to order (please use the number next to your dessert):>"))
        except ValueError:
            print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.ldesserts)} ")
            return total_price, menu_item
        if 0 < order_num <= len(english_menu.ldesserts):
            menu_num = order_num - 1
            menu_item = english_menu.ldesserts[menu_num]
            confirmation  = input(f"so you would like {menu_item}?y/n:>")
            if confirmation  == "y":
                total_price_question = total_price + english_menu.desserts[menu_item]["price"]
                price_confirmation = input(f"this will bring your total price up to {total_price_question} would you like to continue this order? y/n:>")
                if price_confirmation == "y":
                    print("this will be out soon")
                    total_price = total_price_question
                    time.sleep(5)
                    print(f"hear is your {menu_item}")
                    return total_price, menu_item
            elif confirmation == "n":
                print("allright i will not add that to your total")
                return total_price, menu_item

    elif order == "n":
        return total_price, menu_item

def drinks_menu(total_price):
    menu_item = ""
    print("Alright hear is the drinks menu")
    number = 0
    for item in english_menu.drinks:
        description = english_menu.drinks[item]["description"]
        price = "{:,}".format(english_menu.drinks[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    order = input("would you like to make an order?y/n:>")
    if order == "y":
        try:
            order_num = int(input("which drink would you like to order (please use the number next to your drink):>"))
        except ValueError:
            print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.ldrinks)} ")
            return total_price, menu_item
        if 0 < order_num <= len(english_menu.ldrinks):
            menu_num = order_num - 1
            menu_item = english_menu.ldrinks[menu_num]
            confirmation  = input(f"so you would like {menu_item}?y/n:>")
            if confirmation  == "y":
                total_price_question = total_price + english_menu.drinks[menu_item]["price"]
                price_confirmation = input(f"this will bring your total price up to {total_price_question} would you like to continue this order? y/n:>")
                if price_confirmation == "y":
                    print("this will be out soon")
                    total_price = total_price_question
                    time.sleep(5)
                    print(f"hear is your {menu_item}")
                    return total_price, menu_item
            elif confirmation == "n":
                print("allright i will not add that to your total")
                return total_price, menu_item

    elif order == "n":
        return total_price, menu_item

def end(total_price):
    # print("allright hear is your bill")
    # print
    exit()#still in development will be made latter