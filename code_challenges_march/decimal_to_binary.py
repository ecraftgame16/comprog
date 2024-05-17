def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

decimal_number = 42
print(decimal_to_binary(decimal_number))