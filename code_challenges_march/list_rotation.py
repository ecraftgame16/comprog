def rotate_right(lst, steps):
    if not lst:  # Check if the list is empty
        return []

    steps = steps % len(lst)  # To handle rotation more than the length of the list
    return lst[-steps:] + lst[:-steps]

my_list = [1, 2, 3, 4, 5]
steps = 2

rotated_list = rotate_right(my_list, steps)
print(rotated_list)
