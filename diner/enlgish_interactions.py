from menu import *
import time
def english(great_man, language_selection):
    print ("follow me to your table")
    time.sleep(2)
    menu_select(great_man, language_selection)
    
def menu_select(great_man, language_selection):
    """
    This function guides the user through the menu selection process in a restaurant ordering system.
    It allows the user to view and choose from different menu categories (entree, sides, desserts, drinks),
    and to check the total price or leave the menu.

    Parameters:
    great_man (function): A function reference for displaying the greeting message.
    language_selection (function): A function reference for selecting the language of the interface.

    The function prompts the user to select a menu category and calls the respective function for the menu type.
    This function stores the total price and what has been ordered for when the end function is called.
    If the user decides to leave, it calls the `end` function to complete the order and handle the payment process.
    """
    # Initialize the total price and the list of ordered items
    total_price = 0
    ordered_items = []

    # Loop to handle user menu selection
    while True:
        try:
            # Prompt user to select a menu category
            which_menu = int(input("""which menu would you like to look at
                                        1 entree
                                        2 sides
                                        3 desserts
                                        4 drinks
                                        5 check price
                                        6 leave:>"""))
        except ValueError:
            # Handle invalid input (non-integer)
            print("Input Error, please ensure that you only use a number")
            continue

        # Handle user's menu choice
        if which_menu == 1:
            # Process entree menu selection
            total_price, menu_item = entree_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(english_menu.entree[menu_item]["price"])
        elif which_menu == 2:
            # Process sides menu selection
            total_price, menu_item = sides_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(english_menu.sides[menu_item]["price"])
        elif which_menu == 3:
            # Process desserts menu selection
            total_price, menu_item = desserts_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(english_menu.desserts[menu_item]["price"])
        elif which_menu == 4:
            # Process drinks menu selection
            total_price, menu_item = drinks_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(english_menu.drinks[menu_item]["price"])
        elif which_menu == 5:
            # Print the current total price
            print(f"your current total price is ¥{total_price}")
        elif which_menu == 6:
            # Call the end function to complete the order and handle payment
            end(total_price, ordered_items, great_man, language_selection)
            break
        else:
            # Handle invalid menu choice
            print("Input Error: Please ensure you only enter a number 1-5")


def entree_menu(total_price):
    """
    This function manages the ordering process for a specific menu category entree.
    It initially sets the selected menu item to an empty value. The menu items are then listed, with each item
    and its details fetched from the respective dictionary using a for loop.

    The user is prompted to confirm if they want to make an order. If the user chooses to order, the function
    accepts the order based on the numbers printed alongside each menu item. It then confirms the selected item
    and recalculates the total price. The process of confirmation and price calculation involves while loops to
    ensure correct user input.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                        price after a purchase.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
            order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the entree menu to the user
    print("Alright, here is the entree menu")
    number = 0
    for item in english_menu.entree:
        # Fetch each item's description and price from the dictionary
        description = english_menu.entree[item]["description"]
        price = "{:,}".format(english_menu.entree[item]["price"])
        number += 1
        # Display the menu item, description, and price
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("Would you like to make an order? y/n:>").lower()
        if order == "y":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired entree
                order_num = int(input("Which entree would you like to order (please use the number next to your entree):>"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.lentree)} ")
                return total_price, menu_item

            if 0 < order_num <= len(english_menu.lentree):
                # Fetch the selected menu item based on the user's input
                menu_num = order_num - 1 #sets the index to base 0 from base 1 for the input
                menu_item = english_menu.lentree[menu_num]
                while True:
                    # Confirm the selected menu item with the user
                    confirmation = input(f"So you would like {menu_item}? y/n:>").lower()
                    if confirmation == "y":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + english_menu.entree[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user
                            price_confirmation = input(f"This will bring your total price up to {total_price_question}. Would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                # Confirm the order and update the total price
                                print("This will be out soon.")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"Here is your {menu_item}.")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                # Handle user's decision not to proceed with the order
                                print("Alright, this will not be added to your bill.")
                                return total_price, menu_item
                    elif confirmation == "n":
                        # Handle user's decision not to order the selected item
                        print("Alright, I will not add that to your total.")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"Please ensure that you enter a number from 1-{len(english_menu.lentree)}")
                return total_price, menu_item
            break

        elif order == "n":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'y' or 'n')
            print("Please ensure you use 'y' for yes or 'n' for no.")


def sides_menu(total_price):
    """
    This function manages the ordering process for a specific menu category sides.
    It initially sets the selected menu item to an empty value. The menu items are then listed, with each item
    and its details fetched from the respective dictionary using a for loop.

    The user is prompted to confirm if they want to make an order. If the user chooses to order, the function
    accepts the order based on the numbers printed alongside each menu item. It then confirms the selected item
    and recalculates the total price. The process of confirmation and price calculation involves while loops to
    ensure correct user input.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                        price after a purchase.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
            order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the sides menu to the user
    print("Alright, here is the sides menu:")
    number = 0
    for item in english_menu.sides:
        # Fetch each item's description and price from the dictionary
        description = english_menu.sides[item]["description"]
        price = "{:,}".format(english_menu.sides[item]["price"])
        number += 1
        # Display the menu item, description, and price
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("Would you like to make an order? y/n:>").lower()
        if order == "y":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired side
                order_num = int(input("Which side would you like to order (please use the number next to your side):>"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.lsides)} ")
                return total_price, menu_item

            if 0 < order_num <= len(english_menu.lsides):
                # Fetch the selected menu item based on the user's input
                menu_num = order_num - 1 #sets the index to base 0 from base 1 for the input
                menu_item = english_menu.lsides[menu_num]
                while True:
                    # Confirm the selected menu item with the user
                    confirmation = input(f"So you would like {menu_item}? y/n:>").lower()
                    if confirmation == "y":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + english_menu.sides[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user
                            price_confirmation = input(f"This will bring your total price up to {total_price_question}. Would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                # Confirm the order and update the total price
                                print("This will be out soon.")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"Here is your {menu_item}.")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                # Handle user's decision not to proceed with the order
                                print("Alright, this will not be added to your bill.")
                                return total_price, menu_item
                    elif confirmation == "n":
                        # Handle user's decision not to order the selected item
                        print("Alright, I will not add that to your total.")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"Please ensure that you enter a number from 1-{len(english_menu.lsides)}")
                return total_price, menu_item
            break

        elif order == "n":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'y' or 'n')
            print("Please ensure you use 'y' for yes or 'n' for no.")


def desserts_menu(total_price):
    """
    This function manages the ordering process for a specific menu category desserts.
    It initially sets the selected menu item to an empty value. The menu items are then listed, with each item
    and its details fetched from the respective dictionary using a for loop.

    The user is prompted to confirm if they want to make an order. If the user chooses to order, the function
    accepts the order based on the numbers printed alongside each menu item. It then confirms the selected item
    and recalculates the total price. The process of confirmation and price calculation involves while loops to
    ensure correct user input.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                        price after a purchase.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
            order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the desserts menu to the user
    print("Alright, here is the desserts menu:")
    number = 0
    for item in english_menu.desserts:
        # Fetch each item's description and price from the dictionary
        description = english_menu.desserts[item]["description"]
        price = "{:,}".format(english_menu.desserts[item]["price"])
        number += 1
        # Display the menu item, description, and price
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("Would you like to make an order? y/n:>").lower()
        if order == "y":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired dessert
                order_num = int(input("Which dessert would you like to order (please use the number next to your dessert):>"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.ldesserts)} ")
                return total_price, menu_item

            if 0 < order_num <= len(english_menu.ldesserts):
                # Fetch the selected menu item based on the user's input
                menu_num = order_num - 1  # Sets the index to base 0 from base 1 for the input
                menu_item = english_menu.ldesserts[menu_num]
                while True:
                    # Confirm the selected menu item with the user
                    confirmation = input(f"So you would like {menu_item}? y/n:>").lower()
                    if confirmation == "y":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + english_menu.desserts[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user
                            price_confirmation = input(f"This will bring your total price up to {total_price_question}. Would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                # Confirm the order and update the total price
                                print("This will be out soon.")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"Here is your {menu_item}.")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                # Handle user's decision not to proceed with the order
                                print("Alright, this will not be added to your bill.")
                                return total_price, menu_item
                    elif confirmation == "n":
                        # Handle user's decision not to order the selected item
                        print("Alright, I will not add that to your total.")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"Please ensure that you enter a number from 1-{len(english_menu.ldesserts)}")
                return total_price, menu_item
            break

        elif order == "n":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'y' or 'n')
            print("Please ensure you use 'y' for yes or 'n' for no.")


def drinks_menu(total_price):
    """
    This function manages the ordering process for a specific menu category drinks.
    It initially sets the selected menu item to an empty value. The menu items are then listed, with each item
    and its details fetched from the respective dictionary using a for loop.

    The user is prompted to confirm if they want to make an order. If the user chooses to order, the function
    accepts the order based on the numbers printed alongside each menu item. It then confirms the selected item
    and recalculates the total price. The process of confirmation and price calculation involves while loops to
    ensure correct user input.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                        price after a purchase.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
            order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the drinks menu to the user
    print("Alright, here is the drinks menu:")
    number = 0
    for item in english_menu.drinks:
        # Fetch each item's description and price from the dictionary
        description = english_menu.drinks[item]["description"]
        price = "{:,}".format(english_menu.drinks[item]["price"])
        number += 1
        # Display the menu item, description, and price
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("Would you like to make an order? y/n:>").lower()
        if order == "y":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired drink
                order_num = int(input("Which drink would you like to order (please use the number next to your drink):>"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"Input Error: please ensure that you enter a number 1-{len(english_menu.ldrinks)} ")
                return total_price, menu_item

            if 0 < order_num <= len(english_menu.ldrinks):
                # Fetch the selected menu item based on the user's input
                menu_num = order_num - 1  # Sets the index to base 0 from base 1 for the input
                menu_item = english_menu.ldrinks[menu_num]
                while True:
                    # Confirm the selected menu item with the user
                    confirmation = input(f"So you would like {menu_item}? y/n:>").lower()
                    if confirmation == "y":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + english_menu.drinks[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user
                            price_confirmation = input(f"This will bring your total price up to {total_price_question}. Would you like to continue this order? y/n:>").lower()
                            if price_confirmation == "y":
                                # Confirm the order and update the total price
                                print("This will be out soon.")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"Here is your {menu_item}.")
                                return total_price, menu_item
                            elif price_confirmation == "n":
                                # Handle user's decision not to proceed with the order
                                print("Alright, this will not be added to your bill.")
                                return total_price, menu_item
                    elif confirmation == "n":
                        # Handle user's decision not to order the selected item
                        print("Alright, I will not add that to your total.")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"Please ensure that you enter a number from 1-{len(english_menu.ldrinks)}")
                return total_price, menu_item
            break

        elif order == "n":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'y' or 'n')
            print("Please ensure you use 'y' for yes or 'n' for no.")


def end(total_price, ordered_items, great_man, language_selection):
    """
    This function presents the user with an itemized bill, showing each ordered item and its individual price in yen. 
    It then displays the final total price of the meal. Although the option to tip is offered, the server will 
    refuse it due to cultural norms in Japan.

    Parameters:
    total_price (int): The total price of the meal.
    ordered_items (list): A list of all ordered items and their prices.
    great_man (function): The function run at the start of the program, used for looping.
    language_selection (function): Called after great_man because great_man returns this function.
    """
    # Print the itemized bill and total price to the terminal
    print("Alright, here is your bill")
    print("Here is your itemized bill")
    print(f"Here is what you ordered {ordered_items}")
    print(f"Here is your total price {total_price}")

    # Loop to handle payment method selection
    while True:
        try:
            # Prompt user for payment method, ensuring input is a number
            payment_method = int(input("How would you like to pay, card or cash? 1 for cash, 2 for card:>"))
            # Validate payment method choice
            if payment_method == 1 or payment_method == 2:
                break
            else:
                print("Please ensure you only use 1 for cash and 2 for card")
                continue
        except ValueError:
            print("Input Error: Please ensure that you only input 1 for cash, 2 for card")
            continue

    # Loop to handle tipping decision based on payment method
    while True:
        # Check payment method
        if payment_method == 1:
            tip_question = input("Would you like to tip? y/n:>")
            if tip_question == "y":
                # Handle cash payment and tip amount
                try:
                    # Ensure tip amount is a valid integer
                    amount = int(input("How much would you like to tip?")) 
                except ValueError:
                    print("Please ensure you use numbers and nothing else")
                    continue
                # Describe cultural practice regarding tipping in Japan
                print(f"""You leave the diner when a waiter starts to chase you down with the tip you left.
                          He catches up to you and tells you, 'You overpaid, sir. Here is your change.'
                          You take your change back in the amount of {amount}.""")
                time.sleep(8)
                break
            elif tip_question == "n":
                print("You pay and leave.")
                break
        elif payment_method == 2:
            if tip_question == "y":
                # Describe cultural practice regarding tipping in Japan for card payments
                print("""You wave down the waiter, saying there is no option to tip.
                         The waiter calmly informs you that in Japan, tipping is not 
                         common and, to some, is considered rude.""")
                time.sleep(8)
                break
            elif tip_question == "n":
                print("You pay and leave.")
                break

    # Restart the loop by calling great_man and continue with language_selection
    time.sleep(2)
    print(great_man()) 
    language_selection()


