a = int(input("Enter the lenght:\t"))
b = input("Enter symbol:\t")

def triangle_maker(x, y):
    for i in range(0, x):
        print(" "*(x-i) + y*i + y*(i+1))


triangle_maker(a, b)