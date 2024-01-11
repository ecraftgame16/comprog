#variables

text = ""
number = 10
bool = True

#lists

my_fun_lists = [text, number, bool, 45, "asdf"]
two_list = [1,2,3,4]

my_fun_lists.pop()

print(my_fun_lists + two_list)

#dictinaries
example = {"key" : "Values"}

student = {
    "name" : "Crash Bandicoot",
    "list" : my_fun_lists
}

#condintianals

if bool:
    print("I True")
elif 10 > 5:
    pass
else:
    print("i mistake")


#loops

numbers = [1,2,3,4,5]    

for key in student:
    print(student[key])

while