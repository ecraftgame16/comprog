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
        task_aceptence = input (f"{name} will you accept this task y/n")
        if task_aceptence == "y":
            print ("allright lets go on our adventure")
            task = False
        else:
            print("please accept the task")
    print ("got here")
    print ("allright we have accepted the task next up is ")