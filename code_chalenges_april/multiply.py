def multiply(num_list, num):
    anser = []
    for i in num_list:
        anser_num = i * num
        anser.append(anser_num)
    return anser_num

num_list = []
for i in range (5):
    num = int(input("what number would you like to add if you want to leave it blank put 0:>"))
    if num == 0:
        continue
    else:
        num_list.append(num)
print(multiply(num_list, num))