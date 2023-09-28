word = "paradigm"
for i in range(0, len(word)):
	print(word[i])
	
for x in range(0,5):
	print(x)

AnimalList = ['Cat','Dog','Tiger','Cow']
for z in range(0, len(AnimalList)):
	print(AnimalList[z])

flowers = ['Jasmine','Lotus','Rose','Sunflower']
run_time = 0
for x in range(0,len(flowers)):
	print(flowers[x])
	run_time = run_time + 1
	if run_time >= len(flowers):
		print("done")
	else:
		pass

list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
for x in list1:
	for y in list2:
		print(x, y)
	
vehicles = ['Car','Cycle','Bus','Tempo']
vehicles_ran = 0
for x in vehicles:
    vehicles_ran = vehicles_ran+1
    print (vehicles[x])
    if vehicles_ran <= 2:
	    break

vehicles = ['Car','Cycle','Bus','Tempo']
for x in vehicles:
	if x == "bus":
		continue
	else:
		print (vehicles[x])

numbers = [12,3,56,67,89,90]
count = 0
for x in numbers:
	count = count +1

print(count)

numbers = [12,3,56,67,89,90]
sum = 0
for x in numbers:
	sum  = sum + x
print(sum)

numbers = [2,5,6,10,15,20,25]
for x in numbers:
	if x%5 == 0:
		print(x)
		
list1 = ['Mango','Banana','Orange']
list2 = []
for x in list1:
	list2.append(x)
print(list2)

numbers = [1,4,50,80,12]
max = 0
length = 0
for x in numbers:
    if x > max:
        max = x
    length = length + 1
    if length >= len(numbers):
        print(max)

numbers = [1,4,50,80,12]
min = 1
length = 0
for x in numbers:
    if x < min:
        min = x
    length = length + 1
    if length >= len(numbers):
        print(min)

numbers = [1,4,50,80,12]
numbers.sort()
list1 = []
for x in numbers:
    list1.append(x)
print(list1)

numbers = [1,4,50,80,12]
numbers.sort()
numbers.reverse()
list2[]
for x in numbers:
    list2.append(x)
print(list1)

for x in range(1,7):
    print(x * 3)

for x in range(1,4):
    print(x * 5)

y = 11
for x in range (1,11):
    y = y-1
    print(y)