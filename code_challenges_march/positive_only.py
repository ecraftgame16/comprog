def positive_only(numbers):
    qualifying_num = []
    total = 0
    for num in numbers:
        if num >= 0:
            qualifying_num.append(num)
    for num in qualifying_num:
        total += num
    return total // len(qualifying_num)

loops = 0
numbers = []
while loops < 10:
    try:
        num = int(input("Give me 10 numbers, feel free to include both positives and negatives: "))
        loops += 1
    except ValueError:
        print("Please enter a valid integer.")
    else:
        numbers.append(num)
print(f"your numebrs are {numbers}")

print(f"the avrage is {positive_only(numbers)}")
