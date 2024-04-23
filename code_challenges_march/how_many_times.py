def how_many_times (original_list, cheack_acruance):
    acurance_number = 0
    for i in original_list:
        if cheack_acruance == i:
            acurance_number += 1
    return acurance_number

list_count = 10
original_list = []
for i in range(list_count):
    while True:
        try:
            number_added = int(input(f"give me {list_count} numbers which will all be difrent prompts"))
            break
        except ValueError:
            print("please ensure you only input an integer (no decimal points no spaces etc)")
    original_list.append(number_added)
while True:
    try:
        cheack_acurance = int(input("what would you like to cheack for in the list?"))
        break
    except ValueError:
        print("please ensure you only input an integer (no decimal points no spaces etc)")
print(how_many_times(original_list, cheack_acurance))