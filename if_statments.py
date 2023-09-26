# percentage functioin
def percentiage(percent, whole):
    return (percent * whole) // 100.0

# #first one
years_of_service = int(input("how long have you worked heare? "))
salary = int(input("what is your curent sallery? "))

if years_of_service>= 5:
    print("yes you are elligable")
    extra_sallery = percentiage(salary, 5)
    new_sallery = extra_sallery + salary
    print(f"your new sallery is {new_sallery}")
else:
    print(f"you are not eligible for a raise your sally will remain {salary}")

#secont one
width = int(input("what is the width"))
langth = int(input("what is the length"))
if width == langth:
    print("yes it is a square")
else:
    print("no it is not a square")

#third one
num1 = int(input("give me an integer "))
num2 = int(input("give me another integer "))
if num1 > num2:
    print(num1)
elif num2 >  num1:
    print(num2)
elif num1 == num2:
    print("this is a trick question they are equal")
else:
    print("there was an unknown error please try again or contact teh develpor")

#fourth one
list1 = []
age_1 = int(input("how old is the first person "))
age_2 = int(input("how old is the secont person "))
age_3= int(input("how old is the third person "))
list1.append (age_1)
list1.append (age_2)
list1.append (age_3)
list1.sort()
print("Smallest element is:", list1[0])
print("Largest element is:", list1[2])

#fith one
print("hello testie and welcome to the exam before i can let you in I have a question for you dummy")
classes_held = int(input("hey how may calsses were there "))
classes_atended = int(input("now how many classes did you ateded "))

def how_much_did_you_atend(part, wohle):
    return 100 * part/wohle

percentage = how_much_did_you_atend(classes_atended, classes_held)

if percentage >= 75:
    print (f"you are allowed to sit the exam congrats you atended {percentage}% of your classes")
else:
    print(f"hey dummy you do not get to atend the exam get out of here and atend class next time you faild btw ohh you atended {percentage}% of your classes you needed at least 75%")