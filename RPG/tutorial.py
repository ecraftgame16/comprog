import time
from seting import *
def tutorial(name):
    print(f"hello {name} welcome to the tutorial evrything done hear will not affect your game play")
    print ("starting tutorial")
    print ("...")
    time.sleep(3)
    print ("tutorial started")
    print ("in the actual game items dammage and such are randomised here they are going to be the same evry time")
    print ("every new day you will get a new task and then a random fairness of payment")
    print ("the villager will come to you and ask you to do somthing here is an example")
    print (f"""villager:
           {name} Will you please go into the peeks and resuce my Daughter she went up there and got stuck  you will be payed fairly of course:>""")
    print ("then the game will ask you if you will acept this task this time lets accept the task")
    task = True
    while task == True:
        task_aceptence = input (f"{name} will you accept this task y/n:>")
        if task_aceptence == "y":
            print ("allright lets go on our adventure")
            task = False
        else:
            print("please accept the task")
    print ("allright we have accepted the task next up is to start going")
    print ("once you accept the task we must leave the villa")
    print ("that game will ask if you would like to walk -w or cheack inventory -i in the promt following this lets open our inventory")
    inventory = True
    while inventory == True:
        inventoryPromt = input("what would you like to do w - walk i - inventory:>")
        if inventoryPromt == "i":
            print("you have [] in your inventory")
            print("you have 0 curent money")
            print("your health is 100/100")
            inventory = False
        elif inventoryPromt == "w":
            print ("please slect i")
        else:
            print ("make sure you only slect i nothing else")
    print ("now lets go on our task this time lets press w in the promt")
    print("every time you press w you will be promted to chose again uless ofcourse somthing happens")
    walk = True
    walkTime = 0
    while walk == True and walkTime <= 6:
        walkpromt= input("what would you like to do w - walk i - inventory:>")
        if walkpromt == "w":
            walkTime += 1
        elif walkpromt == "i":
            print ("please slect w")
        else:
            print ("make sure you only slect w nothing else")
    print ("oh no we came across a Bandet gang here is a discription")
    print(seting.enimies["Bandit Gang"]['discription'])
    print ("we have 2 options 1 atack with is a and 2 run which is r when you run you have a 50 percent chance of geting away")
    print("lets run this time i dont like are chances 3 agenst 1")
    run1 = True
    while run1 == True:
        run_success = input("would you like to try and run - r or atack - a:>")
        if run_success == "r":
            print("yay we got away that was close")
            run1 = False
        elif run_success == "a":
            print ("please input r which stands for run for this one")
        else:
            print ("make sure you only have the r nothing else")
    walk = True
    walktime = 0
    while walk == True and walkTime <= 6:
        walkpromt= input("what would you like to do w - walk i - inventory:>")
        if walkpromt == "w":
            walkTime += 1
        elif walkpromt == "i":
            print ("please slect w")
        else:
            print ("make sure you only slect w nothing else")
    print ("ohh no another emany this time it is a Forest Yokai hear is a discription")
    print (seting.enimies["Forest Yokai"]["discription"])
    print ("lets run again")
    run2 = True
    while run2 == True:
        run_fail = input("would you like to try and run - r or atack - a:>")
        if run_fail == "r":
            run2 = False
        elif run_fail == "a":
            print ("please input r which stands for run for this one")
        else:
            print ("make sure you only have the r nothing else")
    print ("dang we couldent get away this time")
    print ("you took 50 damage")
    print ("im mad lets fight this")
    atackvar = True
    while atackvar == True:
        atack = input("would you like to atack or runaway? a - atack r - run:>")
        if atack == "a":
            print ("you do 150 damage and defeat the Yokai")
            print ("you gain 50 coins")
            print("you gain 30 HP leaving 80/100")
            atackvar = False
        elif atack == "r":
            print ("please slect a for atack")
        else:
            print ("make sure you only input a nothing else")
    print ("hey 50 coins thats cool anyway lets continue")
    walk = True
    walktime = 0
    while walk == True and walkTime <= 6:
        walkpromt= input("what would you like to do w - walk i - inventory:>")
        if walkpromt == "w":
            walkTime += 1
        elif walkpromt == "i":
            print ("please slect w")
        else:
            print ("make sure you only slect w nothing else")
    print("ohh no not another emany this time it is a Mountain Tengu hear is a discription")
    print (seting.enimies['Mountain Tengu']['discription'])
    print ("im felling confident this time lets fight isted of runing")
    fight = True
    while fight == True:
        fightpromt = input("would you like to atack or runaway? a - atack r - run:>")
        if fightpromt == "a":
            print ("you do 150 damage and defeat the Yokai")
            print ("you gain 50 coins")
            print("you gain 20 HP leaving 100/100")
            fight = False
        elif fightpromt == "r":
            print ("please slect a for atack")
        else:
            print ("make sure you only input a nothing else")
    print ("and finaly we made it we saved the person lets go home")
    print (f"you are now ready to play the game {name} good luck")
    print ("shuting down tutorial")
    print ("...")
    time.sleep(3)