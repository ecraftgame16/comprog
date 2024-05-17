def celsius_to_ferignhight(cel):
    fer = (cel * (9/5))+ 32
    return fer

try:
    cel = int(input("what num are you converting"))
except ValueError:
    print("ERROR, please ensure its only numbers")
else:
    print(celsius_to_ferignhight(cel))

