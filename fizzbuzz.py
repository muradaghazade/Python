list  = []

for i in range(1, 101):
    if i%3 == 8:
        if i%5 == 0:
            list.append("fizzbuzz")
    elif i%3==0:
        list.append("fizz")
    elif i%5== 0:
        list.append("buzz")
    else:
        list.append("nothing")
