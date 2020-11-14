def my_func(var1, var2, var3):
    b = max(var1, var2, var3)
    if b == var1:
        b = b + max(var2, var3)
    elif b == var2:
        b = b + max(var1, var3)
    else:
        b = b + max(var1, var2)
    return b

aa = input("Enter  3 number:")
a = aa.split()
if len(a) == 3:
    if a[0].isdigit() & a[1].isdigit() & a[2].isdigit():
        print(my_func(int(a[0]), int(a[1]), int(a[2])))
    else:
        print("Enter number")
else:
    print("Enter 3 number")