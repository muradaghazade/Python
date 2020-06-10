for i in range(1, 101):
    if i%3 == 0:
        if i%5 == 0:
            print(i, "fuzzbuzz")
    elif i%3==0:
        print (i, "fuzz")
    elif i%5== 0:
        print(i, "buzz")
    else:
        print(i, "nothing")