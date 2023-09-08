#scope where a variable falls (golbal or local)

hello_world = "true" # this is a golbal varial aka evrywhere

def give_a_name():
    a_name = "william"#local variable only in the function
    print (a_name)
#print (a_name) wont work

usser_input = input("what are you doing? ")#input
print (f"why are you doing {usser_input}!")

what_is_this = "this thing" #the quotes are a string
what_about_this = 18 #this is an int
is_it_true = True #this is a boolean
and_finaly_this = 18.5 #this is a float

print (what_about_this + and_finaly_this)#will be float

print (what_about_this + what_about_this)#will be float

my_declaration = "" #making a decloration (making a variable with no value)
my_intilataion = "Hello World" #initlasiation is making the variable and giving it a value

#math = aritmitic operators
print (3+6)#math
print (3/6)#math
print (3-6)#math
print (3*6)#math
print (3%6)#math

x = 3
y = 6

if x>y: #comparasion operator
    pass
if x<y :
    pass
if x == y:
    pass
if x<=y:
    pass
#etc

x = True
y = True

#logic cpmparator
if x or y:
    pass
if x and y:
    pass
if x and not y:
    pass
#etc

#order of operations (pemmdas) paretheses exponest multipilcation modulud division addition subtraction

b = 10 #initislation statment
u = b + 10 #exsprestion beacuse it can change

print (3 // 5)#int div
print (3 / 5) #float div

#function
def function():
    print ("this is a function")

function()

#readablity
thisisnotreadable=True
this_is_readable = True

#resuibility
def add(num1, num2):
    print(num1 + num2)
    #can reuse this function 

#modularity reusibility and limits duplication

#usser defined function
ussernum1 = int(input("give me a number"))
ussernum2 = int(input("give me another one"))

def usser_add(ussernum1, ussernum2): #thease () are the paramiters
    print(ussernum1 + ussernum2) #also () are the paramiters
usser_add(ussernum1, ussernum2) #the () are the agurment

#bult in function
my_name = "tacocat"
words = my_name.split("o")
print (words)

#return
def subtract(num3,num4):
    return num3 - num4

print(subtract(4,2))
#or
diffrence = subtract (5,3)

#simple data type charater string integer float double boolean
#complex data type enumeration, array, list, object