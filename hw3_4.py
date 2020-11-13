def my_func(x, y):
    return 1/x**y


def my_func1(x, y):
    i = 1
    c = x
    while i < y:
        c = c*x
        i = i+1
    return 1/c


a = input("Enter number1:")
b = input("Enter number2 :")
b = abs((int(b)))
if a.isdigit():
    print(my_func(int(a), b))
    print(my_func1(int(a), b))