import time
from menu import japanese_menu
def japanese(great_man, language_selection):
    """
    This function initiates the restaurant ordering process in Japanese. It welcomes the user and guides them
    to their virtual table. After a brief pause, it proceeds to the menu selection phase, allowing the user
    to interact with the menu in Japanese.a

    Parameters:
    great_man (function): A function reference that displays the initial greeting message.
    language_selection (function): A function reference for selecting the language, allowing for potential 
    re-selection or change of language at the end of the ordering process.

    The function prints a welcome message in Japanese, pauses briefly, and then calls the menu_select
    function, passing along the great_man and language_selection functions for continuity in the user experience.
    """
    print("あなたのテーブルについてきてください")
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
    # Initialize variables to store the total price and ordered items
    total_price = 0
    ordered_items = []

    # Loop to handle user menu selection
    while True:
        try:
            # Prompt user to select a menu category in Japanese
            which_menu = int(input("""どのメニューを見ますか：
                                        1 エントリー
                                        2 サイド
                                        3 デザート
                                        4 ドリンク
                                        5 価格をチェック
                                        6 退出:>"""))
        except ValueError:
            # Handle invalid input (non-integer)
            print("入力エラーです。数字のみを使用してください")
            continue

        # Handle user's menu choice
        if which_menu == 1:
            # Process entree menu selection
            total_price, menu_item = entree_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(japanese_menu.entree[menu_item]["price"])
        elif which_menu == 2:
            # Process sides menu selection
            total_price, menu_item = sides_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(japanese_menu.sides[menu_item]["price"])
        elif which_menu == 3:
            # Process desserts menu selection
            total_price, menu_item = desserts_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(japanese_menu.desserts[menu_item]["price"])
        elif which_menu == 4:
            # Process drinks menu selection
            total_price, menu_item = drinks_menu(total_price)
            if menu_item != "":
                ordered_items.append(menu_item)
                ordered_items.append(japanese_menu.drinks[menu_item]["price"])
        elif which_menu == 5:
            # Print the current total price in Japanese
            print(f"現在の合計価格は ¥{total_price}です")
        elif which_menu == 6:
            # Call the end function to complete the order and handle payment
            end(total_price, ordered_items, great_man, language_selection)
            break
        else:
            # Handle invalid menu choice
            print("入力エラー: 数字1〜5を入力してください")

def entree_menu(total_price):
    """
    This function manages the ordering process for the entree menu category in a Japanese restaurant ordering system.
    It displays the entree menu, allows the user to select an item, and calculates the total price after adding the selected item.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                       price after adding the selected entree.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
           order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the entree menu in Japanese
    print("それでは、エントリーメニューをご紹介します")
    number = 0
    for item in japanese_menu.entree:
        # Fetch each item's description and price from the dictionary
        description = japanese_menu.entree[item]["description"]
        price = "{:,}".format(japanese_menu.entree[item]["price"])
        number += 1
        # Display the menu item, description, and price in Japanese
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired entree in Japanese
                order_num = int(input("どのエントリーを注文しますか？番号を入力してください:＞"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"入力エラー: 1-{len(japanese_menu.entree)}の数字を入力してください")
                return total_price, menu_item

            if 0 < order_num <= len(japanese_menu.entree):
                # Convert user input to zero-based index for list access
                menu_num = order_num - 1
                menu_item = list(japanese_menu.entree.keys())[menu_num]
                while True:
                    # Confirm the selected menu item with the user in Japanese
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + japanese_menu.entree[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user in Japanese
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                # Confirm the order and update the total price
                                print("まもなくお持ちします")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                # Handle user's decision not to proceed with the order
                                print("了解しました、請求には追加しません")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        # Handle user's decision not to order the selected item
                        print("了解しました、追加しません")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"1-{len(japanese_menu.entree)}の数字を入力してください")
                return total_price, menu_item
        elif order == "いいえ":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'はい' or 'いいえ')
            print("はいかいいえで回答してください")

def sides_menu(total_price):
    """
    This function manages the ordering process for the sides menu category in a Japanese restaurant ordering system.
    It displays the sides menu, allows the user to select an item, and calculates the total price after adding the selected item.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                       price after adding the selected side.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
           order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the sides menu in Japanese
    print("それでは、サイドメニューをご紹介します：")
    number = 0
    for item in japanese_menu.sides:
        # Fetch each item's description and price from the dictionary
        description = japanese_menu.sides[item]["description"]
        price = "{:,}".format(japanese_menu.sides[item]["price"])
        number += 1
        # Display the menu item, description, and price in Japanese
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired side in Japanese
                order_num = int(input("どのサイドを注文しますか？番号を入力してください:＞"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"入力エラー: 1-{len(japanese_menu.sides)}の数字を入力してください")
                return total_price, menu_item

            if 0 < order_num <= len(japanese_menu.sides):
                # Convert user input to zero-based index for array access
                menu_num = order_num - 1
                menu_item = list(japanese_menu.sides.keys())[menu_num]
                while True:
                    # Confirm the selected menu item with the user in Japanese
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + japanese_menu.sides[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user in Japanese
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                # Confirm the order and update the total price
                                print("まもなくお持ちします。")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました。")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                # Handle user's decision not to proceed with the order
                                print("了解しました、請求には追加しません。")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        # Handle user's decision not to order the selected item
                        print("了解しました、追加しません。")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"1-{len(japanese_menu.sides)}の数字を入力してください")
                return total_price, menu_item
            break

        elif order == "いいえ":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'はい' or 'いいえ')
            print("はいかいいえで回答してください")


def desserts_menu(total_price):
    """
    This function manages the ordering process for the desserts menu category in a Japanese restaurant ordering system.
    It displays the desserts menu, allows the user to select an item, and calculates the total price after adding the selected item.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                       price after adding the selected dessert.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
           order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the desserts menu in Japanese
    print("それでは、デザートメニューをご紹介します：")
    number = 0
    for item in japanese_menu.desserts:
        # Fetch each item's description and price from the dictionary
        description = japanese_menu.desserts[item]["description"]
        price = "{:,}".format(japanese_menu.desserts[item]["price"])
        number += 1
        # Display the menu item, description, and price in Japanese
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired dessert in Japanese
                order_num = int(input("どのデザートを注文しますか？番号を入力してください:＞"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"入力エラー: 1-{len(japanese_menu.desserts)}の数字を入力してください")
                return total_price, menu_item

            if 0 < order_num <= len(japanese_menu.desserts):
                # Convert user input to zero-based index for array access
                menu_num = order_num - 1
                menu_item = list(japanese_menu.desserts.keys())[menu_num]
                while True:
                    # Confirm the selected menu item with the user in Japanese
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + japanese_menu.desserts[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user in Japanese
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                # Confirm the order and update the total price
                                print("まもなくお持ちします。")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました。")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                # Handle user's decision not to proceed with the order
                                print("了解しました、請求には追加しません。")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        # Handle user's decision not to order the selected item
                        print("了解しました、追加しません。")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"1-{len(japanese_menu.desserts)}の数字を入力してください")
                return total_price, menu_item
            break

        elif order == "いいえ":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'はい' or 'いいえ')
            print("はいかいいえで回答してください")

def drinks_menu(total_price):
    """
    This function manages the ordering process for the drinks menu category in a Japanese restaurant ordering system.
    It displays the drinks menu, allows the user to select an item, and calculates the total price after adding the selected item.

    Parameters:
    total_price (int): The current total price of the order. This parameter is used to calculate the new total
                       price after adding the selected drink.

    Returns:
    tuple: A tuple consisting of the updated total_price (which may be unchanged if the user decides not to
           order) and the ordered menu item (which is empty if nothing is ordered).
    """
    # Initialize the menu item selection to an empty string
    menu_item = ""
    
    # Print the drinks menu in Japanese
    print("それでは、ドリンクメニューをご紹介します：")
    number = 0
    for item in japanese_menu.drinks:
        # Fetch each item's description and price from the dictionary
        description = japanese_menu.drinks[item]["description"]
        price = "{:,}".format(japanese_menu.drinks[item]["price"])
        number += 1
        # Display the menu item, description, and price in Japanese
        print(f"{number} - {item}: {description} - ¥{price}")

    # Loop to handle user's decision to order or not
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            # Handle user's choice to order
            try:
                # Prompt for the number corresponding to the desired drink in Japanese
                order_num = int(input("どのドリンクを注文しますか？番号を入力してください:＞"))
            except ValueError:
                # Handle invalid input (non-integer)
                print(f"入力エラー: 1-{len(japanese_menu.drinks)}の数字を入力してください")
                return total_price, menu_item

            if 0 < order_num <= len(japanese_menu.drinks):
                # Convert user input to zero-based index for array access
                menu_num = order_num - 1
                menu_item = list(japanese_menu.drinks.keys())[menu_num]
                while True:
                    # Confirm the selected menu item with the user in Japanese
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        # Calculate the new total price with the selected item
                        total_price_question = total_price + japanese_menu.drinks[menu_item]["price"]
                        while True:
                            # Confirm the new total price with the user in Japanese
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                # Confirm the order and update the total price
                                print("まもなくお持ちします。")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました。")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                # Handle user's decision not to proceed with the order
                                print("了解しました、請求には追加しません。")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        # Handle user's decision not to order the selected item
                        print("了解しました、追加しません。")
                        return total_price, menu_item
            else:
                # Handle invalid selection (out of range)
                print(f"1-{len(japanese_menu.drinks)}の数字を入力してください")
                return total_price, menu_item
            break

        elif order == "いいえ":
            # Handle user's decision not to order anything
            return total_price, menu_item
        else:
            # Handle invalid response (other than 'はい' or 'いいえ')
            print("はいかいいえで回答してください")

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
    # Print the itemized bill and total price in Japanese
    print("それでは、お会計です")
    print("こちらが項目別の請求書です")
    print(f"注文したもの：{ordered_items}")
    print(f"合計金額：{total_price}")

    # Loop to handle payment method selection
    while True:
        try:
            # Prompt user for payment method in Japanese, ensuring input is a number
            payment_method = int(input("支払い方法は現金、またはカードですか? 1:現金、2:カード：＞"))
        except ValueError:
            # Handle invalid input (non-integer)
            print("入力エラー：現金は1、カードは2と入力してください")
            continue

        # Loop to handle tipping decision based on payment method
        while True:
            if payment_method == 1:
                # Prompt for tip decision for cash payment in Japanese
                tip_question = input("チップを残しますか？はい/いいえ：＞")
                if tip_question == "はい":
                    # Handle cash payment and tip amount
                    try:
                        # Ensure tip amount is a valid integer
                        amount = int(input("チップの金額はいくらにしますか？"))
                    except ValueError:
                        print("数字のみを入力してください")
                        continue
                    # Describe cultural practice regarding tipping in Japan
                    print(f"""食事を終えて店を出ると、ウェイターがチップを持って追いかけてきます。
                              彼はあなたに追いつき、「お客様、多くお支払いいただきました。おつりをどうぞ」と言います。
                              あなたは{amount}円のおつりを受け取ります。""")
                    time.sleep(8)
                    break
                elif tip_question == "いいえ":
                    # Handle no tip decision
                    print("支払いを済ませて店を出ます。")
                    break
            elif payment_method == 2:
                # Prompt for tip decision for card payment in Japanese
                tip_question = input("チップを残しますか？はい/いいえ：＞")
                if tip_question == "はい":
                    # Describe cultural practice regarding tipping in Japan for card payments
                    print("""チップを残す方法がないとウェイターを呼び止めます。
                             ウェイターは落ち着いて、「日本ではチップは一般的ではなく、場合によっては失礼とされます」と説明します。""")
                    time.sleep(8)
                    break
                elif tip_question == "いいえ":
                    # Handle no tip decision
                    print("支払いを済ませて店を出ます。")
                    break
            break

        # Restart the loop by calling great_man and continue with language_selection
        time.sleep(2)
        print(great_man()) 
        language_selection()
        break

