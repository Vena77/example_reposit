class ComplexChislo:

    def __init__(self, c_chislo):
        self.c_chislo = c_chislo

    def __str__(self):
        return f"{self.c_chislo}"

    def __add__(self, other):
        return ComplexChislo(self.c_chislo + other.c_chislo)

    def __mul__(self, other):
        return ComplexChislo(self.c_chislo * self.c_chislo)

a = input("Enter complex number: ")
b = input("Enter another complex number: ")
c_chis = ComplexChislo(complex(a))
c_chis1 = ComplexChislo(complex(b))
print(c_chis+c_chis1)
print(c_chis*c_chis1)