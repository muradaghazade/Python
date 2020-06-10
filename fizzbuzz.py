for i in range(1, 101):
    if i%3==0:
        print (i, "fuzz")
    if i%5== 0:
        print(i, "buzz")
    if i%15==0:
        print(i, "fuzzbuzz")
    else:
        print(i, "nothing")