import time
from menu import *
def japanese(great_man, language_selection):
    """
    This function initiates the restaurant ordering process in Japanese. It welcomes the user and guides them
    to their virtual table. After a brief pause, it proceeds to the menu selection phase, allowing the user
    to interact with the menu in Japanese.

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

    The function prompts the user to select a menu category and calles the respective function for the menu type. this function stores the total price and what has
    been orderd for when the end function is called, if the user decides to leave,
    it calls the `end` function to complete the order and handle the payment process.
    """
    total_price = 0
    orderd_items = []
    while True:
        try:
            which_menu = int(input("""どのメニューを見ますか：
                                        1 エントリー
                                        2 サイド
                                        3 デザート
                                        4 ドリンク
                                        5 価格をチェック
                                        6 退出:>"""))
        except ValueError:
            print("入力エラーです。数字のみを使用してください")
            continue
        if which_menu == 1:
            total_price, menu_item = entree_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(japanese_menu.entree[menu_item]["price"])
        elif which_menu == 2:
            total_price, menu_item = sides_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(japanese_menu.sides[menu_item]["price"])
        elif which_menu == 3:
            total_price, menu_item = desserts_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(japanese_menu.desserts[menu_item]["price"])
        elif which_menu == 4:
            total_price, menu_item = drinks_menu(total_price)
            if menu_item != "":
                orderd_items.append(menu_item)
                orderd_items.append(japanese_menu.drinks[menu_item]["price"])
        elif which_menu == 5:
            print(f"現在の合計価格は ¥{total_price}です")
        elif which_menu == 6:
            end(total_price, orderd_items, great_man, language_selection)
            break
        else:
            print("入力エラー: 数字1〜5を入力してください")

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
    menu_item = ""
    print("それでは、エントリーメニューをご紹介します")
    number = 0
    for item in japanese_menu.entree:
        description = japanese_menu.entree[item]["description"]
        price = "{:,}".format(japanese_menu.entree[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            try:
                order_num = int(input("どのエントリーを注文しますか？番号を入力してください:＞"))
            except ValueError:
                print(f"入力エラー: 1-{len(japanese_menu.entree)}の数字を入力してください")
                return total_price, menu_item
            if 0 < order_num <= len(japanese_menu.entree):
                menu_num = order_num - 1
                menu_item = list(japanese_menu.entree.keys())[menu_num]
                while True:
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        total_price_question = total_price + japanese_menu.entree[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                print("まもなくお持ちします")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                print("了解しました、請求には追加しません")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        print("了解しました、追加しません")
                        return total_price, menu_item
            else:
                print(f"1-{len(japanese_menu.entree)}の数字を入力してください")
                return total_price, menu_item
        elif order == "いいえ":
            return total_price, menu_item
        else:
            print("はいかいいえで回答してください")

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
    menu_item = ""
    print("それでは、サイドメニューをご紹介します：")
    number = 0
    for item in japanese_menu.sides:
        description = japanese_menu.sides[item]["description"]
        price = "{:,}".format(japanese_menu.sides[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            try:
                order_num = int(input("どのサイドを注文しますか？番号を入力してください:＞"))
            except ValueError:
                print(f"入力エラー: 1-{len(japanese_menu.sides)}の数字を入力してください")
                return total_price, menu_item
            if 0 < order_num <= len(japanese_menu.sides):
                menu_num = order_num - 1
                menu_item = list(japanese_menu.sides.keys())[menu_num]
                while True:
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        total_price_question = total_price + japanese_menu.sides[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                print("まもなくお持ちします。")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました。")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                print("了解しました、請求には追加しません。")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        print("了解しました、追加しません。")
                        return total_price, menu_item
            else:
                print(f"1-{len(japanese_menu.sides)}の数字を入力してください")
                return total_price, menu_item
            break

        elif order == "いいえ":
            return total_price, menu_item
        else:
            print("はいかいいえで回答してください。")

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
    menu_item = ""
    print("それでは、デザートメニューをご紹介します：")
    number = 0
    for item in japanese_menu.desserts:
        description = japanese_menu.desserts[item]["description"]
        price = "{:,}".format(japanese_menu.desserts[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            try:
                order_num = int(input("どのデザートを注文しますか？番号を入力してください:＞"))
            except ValueError:
                print(f"入力エラー: 1-{len(japanese_menu.desserts)}の数字を入力してください")
                return total_price, menu_item
            if 0 < order_num <= len(japanese_menu.desserts):
                menu_num = order_num - 1
                menu_item = list(japanese_menu.desserts.keys())[menu_num]
                while True:
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        total_price_question = total_price + japanese_menu.desserts[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                print("まもなくお持ちします。")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました。")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                print("了解しました、請求には追加しません。")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        print("了解しました、追加しません。")
                        return total_price, menu_item
            else:
                print(f"1-{len(japanese_menu.desserts)}の数字を入力してください")
                return total_price, menu_item
            break

        elif order == "いいえ":
            return total_price, menu_item
        else:
            print("はいかいいえで回答してください。")

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
    menu_item = ""
    print("それでは、ドリンクメニューをご紹介します：")
    number = 0
    for item in japanese_menu.drinks:
        description = japanese_menu.drinks[item]["description"]
        price = "{:,}".format(japanese_menu.drinks[item]["price"])
        number += 1
        print(f"{number} - {item}: {description} - ¥{price}")
    while True:
        order = input("注文しますか？はい/いいえ:>").lower()
        if order == "はい":
            try:
                order_num = int(input("どのドリンクを注文しますか？番号を入力してください:＞"))
            except ValueError:
                print(f"入力エラー: 1-{len(japanese_menu.drinks)}の数字を入力してください")
                return total_price, menu_item
            if 0 < order_num <= len(japanese_menu.drinks):
                menu_num = order_num - 1
                menu_item = list(japanese_menu.drinks.keys())[menu_num]
                while True:
                    confirmation = input(f"{menu_item}を注文しますか？はい/いいえ:>").lower()
                    if confirmation == "はい":
                        total_price_question = total_price + japanese_menu.drinks[menu_item]["price"]
                        while True:
                            price_confirmation = input(f"合計金額が¥{total_price_question}になります。注文を続けますか？はい/いいえ:>").lower()
                            if price_confirmation == "はい":
                                print("まもなくお持ちします。")
                                total_price = total_price_question
                                time.sleep(5)
                                print(f"{menu_item}をお持ちしました。")
                                return total_price, menu_item
                            elif price_confirmation == "いいえ":
                                print("了解しました、請求には追加しません。")
                                return total_price, menu_item
                    elif confirmation == "いいえ":
                        print("了解しました、追加しません。")
                        return total_price, menu_item
            else:
                print(f"1-{len(japanese_menu.drinks)}の数字を入力してください")
                return total_price, menu_item
            break

        elif order == "いいえ":
            return total_price, menu_item
        else:
            print("はいかいいえで回答してください。")

def end(total_price, orderd_items, great_man, language_selection):
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
    print("それでは、お会計です")
    print("こちらが項目別の請求書です")
    print(f"注文したもの：{orderd_items}")
    print(f"合計金額：{total_price}")
    while True:
        try:
            payment_method = int(input("支払い方法は現金、またはカードですか?1:現金、2:カード：＞"))
            break
        except ValueError:
            print("入力エラー：現金は1、カードは2と入力してください")
            continue
    while True:
        if payment_method == 1:
            tip_question = input("チップを残しますか？はい/いいえ：＞")
            if tip_question == "はい":
                try:
                    amount = int(input("チップの金額はいくらにしますか？"))
                except ValueError:
                    print("数字のみを入力してください")
                    continue
                print(f"""食事を終えて店を出ると、ウェイターがチップを持って追いかけてきます。
                          彼はあなたに追いつき、「お客様、多くお支払いいただきました。おつりをどうぞ」と言います。
                          あなたは{amount}円のおつりを受け取ります。""")
                break
            elif tip_question == "いいえ":
                print("支払いを済ませて店を出ます。")
                break
        elif payment_method == 2:
            if tip_question == "はい":
                try:
                    amount = int(input("チップの金額はいくらにしますか？"))
                except ValueError:
                    print("数字のみを入力してください")
                    continue
                print("""チップを残す方法がないとウェイターを呼び止めます。
                         ウェイターは落ち着いて、「日本ではチップは一般的ではなく、場合によっては失礼とされます」と説明します。""")
                break
            elif tip_question == "いいえ":
                print("支扲いを済ませて店を出ます。")
                break
    print(great_man())
    language_selection()
