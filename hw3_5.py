def f():
    sum1 = 0
    for i in l2:
        if i != "!":
            sum1 = sum1 + int (i)
        else:
            break
    print (sum1)

n = input("Enter number:")
l2 = n.split()
f()
n = input("Enter number:")
l2 = l2+ n.split()
f()