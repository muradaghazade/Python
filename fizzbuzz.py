list  = []

for i in range(1, 101):
    if i%3 ==0 :
        if i%5 == 0:
            list.append("fizzbuzz")
            else:
                list.append("fizz")
        list.append("buzz")
    else:
        list.append("nothing")

list_two = list.count("fizz")
list_three = list.count("buzz")
list_four = list.count("FizzBuzz")
print(list_two, "fizz")
print(list_three, "buzz")
print(list_four, "FizzBuzz")