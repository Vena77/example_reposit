from sys import argv

def func_r(var1,var2,var3) :
    return var1*var2+var3

_,a,b,c = argv
print(argv)
print(func_r(int(a),int(b),int(c)))
print(func_r(int(argv[1]),int(argv[2]),int(argv[3])))