num1 = int(input("give me a number. "))
num2 = int(input("give me another number. "))
operator = int(input("""and finaly whitch operator do you want? 
          1 addition
          2 subtraction
          3 multipication
          4 division. """))

#the individual functions
def addiotion(num1,num2):
    print(f"the answer is", num1 + num2)

def subtraction(num1, num2):
    print(f"the answer is", num1-num2)

def multiplicaton(num1,num2):
    print(f"the answer is", num1*num2)

def divison(num1,num2):
    print(f"the answer is", num1/num2)

#calling the functons
if operator == 1:
    addiotion (num1,num2)

elif operator  == 2:
    subtraction (num1,num2)

elif operator == 3:
    multiplicaton(num1,num2)

elif operator == 4:
    divison (num1,num2)

else:
    print("error please enter a number 1-4 depending on the operator")
