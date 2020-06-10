list  = []

for i in range(1, 101):
    if i%3==0:
        if i%5==0:
            list.append('FizzBuzz')
        else:
            list.append('Fizz')
    elif i%5==0:
        list.append('Buzz')
    else:
        list.append('Nothing')

list_two = list.count("fizz")
list_three = list.count("buzz")
list_four = list.count("FizzBuzz")
print(list_two, "fizz")
print(list_three, "buzz")
print(list_four, "FizzBuzz")