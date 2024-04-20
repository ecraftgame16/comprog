def median(number_list):
    if len(number_list) % 2 == 0:
        even = True
    elif len(number_list) % 2 != 0:
        even = False
    sort_list = sorted(number_list)
    if even:
        index_num1 = len(sort_list) // 2
        index_num2 = index_num1
        index_num1 -= 1
        even_avrage = (sort_list[index_num1] + sort_list[index_num2]) / 2
        return even_avrage
    elif not even:
        index_num = len(sort_list) // 2
        return sort_list[index_num]


max_numbers = 10
number_list = []

print(
    f"""welcome to the median calculator please insert the numbers 1 per pront up to {max_numbers} if you dont want to put a number in the slot use 0 and if you want to stop entering 
    numbers enter 00"""
)
for i in range(max_numbers):
    try:
        added_number = int(
            input(
                "give me a number nothing elase (use 0 if you dont want a number to go into that slot):>"
            )
        )
    except ValueError:
        print(
            "please ensure the input is just a number nothing elase no letters no spaces etc"
        )
    else:
        if added_number == 0:
            continue
        elif added_number == 00:
            break
        else:
            number_list.append(added_number)
