for i in range(1, 101):
    var1 = ""
    if i % 3 == 0:
        var1 += "fizz"
    if i % 5 == 0:
        var1 += "buzz"
    
    if var1 == "":
        print(i)
    else:
        print (var1)