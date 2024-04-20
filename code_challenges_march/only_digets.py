def only_digets (digit_list):
    for i in digit_list:
        if isinstance(i, int):
            continue
        else:
            return False
    return True

max_number = 10
digit_list = []

for i in range(max_number):
    new_input = input("what would you like to add to the list:>")
    if new_input.isdigit():
        new_digit = int(new_input)
        digit_list.append(new_digit)
        continue
    else:
        digit_list.append(new_input)
print(only_digets(digit_list))