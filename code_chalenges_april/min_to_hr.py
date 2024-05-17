def min_to_hr(min):
    if min < 60:
        return(f" 0 hr and {min}min")
    elif min == 60:
        return("1hr and 0 min")
    elif min > 60:
        hr = 0
        while True:
            if min >= 60:
                min -= 60
                hr += 1
            elif min < 60:
                break
        return (f"{hr}hours and {min} min")

while True:
    try:
        min = int(input("what is the number in minutes:>"))
    except ValueError:
        print ("ERROR: ensure its only numbers no commas no spaces")
    else:
        print(min_to_hr(min))