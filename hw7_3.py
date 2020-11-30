class Cell:
    def __init__(self,sum_cell):
        self.sum_cell = sum_cell

    def __str__(self):
        return f"New Cell with cell = {self.sum_cell}"

    def __add__(self, other):
        return Cell(self.sum_cell+other.sum_cell)

    def __sub__(self, other):
        if abs(self.sum_cell - other.sum_cell) != 0:
            return Cell(abs(self.sum_cell - other.sum_cell))
        else:
            return "Разность ячеек клеток равна 0"

    def __mul__(self, other):
        return Cell(self.sum_cell*other.sum_cell)

    def __truediv__(self, other):
        if self.sum_cell > other.sum_cell:
            return Cell(self.sum_cell//other.sum_cell)
        else:
            return Cell(other.sum_cell//self.sum_cell)

    def make_order(self,kol_cell):
       if kol_cell != 0:
        res = self.sum_cell // kol_cell
        str = ""
        for j in range(0,res):
           for i in range(0,kol_cell):
             str = str + "*"
           str = str +r"\n"
        if self.sum_cell % kol_cell != 0:
           for i in range(0,self.sum_cell % kol_cell):
               str = str + "*"
        else:
            str = str[:-2]
        return str
       raise ZeroDivisionError

cell = Cell(15)
print(cell+cell)
print(cell-cell)
print(cell*cell)
print(cell/cell)
print(cell.make_order(14))
print(cell.make_order(5))
print(cell.make_order(4))