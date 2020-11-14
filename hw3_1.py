def my_f(var1, var2):
    if var2 != 0:
        return var1 / var2

a = input("Enter number1:")
b = input("Enter number2:")
if a.isdigit() & b.isdigit():
    print(my_f(int(a), int(b)))