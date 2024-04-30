import math
def introduction(num1, num2, operator):
    anser = 0
    if operator == 1:
        return add(num1, num2)
    elif operator == 2:
        return subtract(num1, num2)
    elif operator == 3:
        return multiply(num1, num2)
    elif operator == 4:
        return divide(num1, num2)
    elif operator == 5:
        return exponent(num1, num2)
    elif operator == 6:
        return square_root(num1)
    

def add (num1, num2):
    return(num1 + num2)

def subtract(num1, num2):
    return(num1-num2)

def multiply(num1, num2):
    return(num1*num2)

def divide(num1, num2):
    while True:    
        anser = input("do you want to have a more percice anser (decimal place) or a simpliler anser (no decimal place) p = percice or s = simple:>")
        try:    
            if anser == "p":
                return (num1/num2)
            elif anser == "s":
                return (num1//num2)
        except ZeroDivisionError:
            return("are you kiding me dumby")

def exponent(num1, num2):
    if num2 == 1:
        return(num1)
    elif num2 == 0:
        return(0)
    else:
        return(num1**num2)

def square_root(num1):
    if num1 == 0:
        return(0)
    elif num1 == -1:
        return("i")
    elif num1 < -1:
        return("i dont get payed enough for this")
    else:
        return(math.sqrt(num1))

while True:
    try:
        operator = int(input("""which operator would you like to use
                        1, addition
                        2, subtraction
                        3, multiply
                        4 divide
                        5 exponent
                        6 square_root:>"""))
        if operator not in range(1, 7):
            raise ValueError("Invalid operator selected.")
        if operator == 6:
            num1 = int(input("what number would you like to square root"))
            num2 = 0
        else:
            num1 =int(input("what would you like the first number be:>"))
            num2 =int(input("what would you like the second number to be:>"))
    except ValueError:
        print("PUT ONLY NUMBERS NO SPACE NO DASH NO DECIMLS AND MAKE SURE IT IS 1-6, im not mad im just disapointed")
        continue
    else:
        print(introduction(num1, num2, operator))
        break