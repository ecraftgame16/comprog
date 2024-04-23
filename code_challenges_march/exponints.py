import math

def exponent(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return "i dont get payed enough for this"
    else:
        return base ** power

base = int(input ("what is the base"))
power = int(input("what is the power"))
print(exponent(base, power))