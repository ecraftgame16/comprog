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

print(3/5)#int div
print(3.0/5.0) #float div

def function():
    print ("this is a function")
#readablity
thisisnotreadable=True
this_is_readable = True

#bultin function
x = "this will be a list"
A = list(x)
print (A)
