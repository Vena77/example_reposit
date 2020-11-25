class Matrix:

    def __init__(self,matr):
       self.matr = matr

    def __str__(self):
        for i in range (len(self.matr)):
            for j in range (len(self.matr[i])):
                print ("{:4d}".format (self.matr[i][j]), end="")
            print ()

    def __add__(self, other):
        if len(self.matr) == len(other.matr) and len(self.matr[0]) == len((other.matr[0])):
          new_matrix = self.matr
          for i in range (len (self.matr)):
              for j in range (len (self.matr[i])):
                  new_matrix[i][j]= self.matr[i][j] + other.matr[i][j]
          return Matrix(new_matrix)
        raise Exception ("Матрицы разные по длинне не складываются!")

ll = [[1,2,3],[3,6,7],[4,8,9]]
ll1 = [[3,5,32],[2,4,6],[-1,64,-8]]
ll3 = [[31,22,37],[43,51,86]]
ll4 = [[3,5,8,6],[8,3,7,2]]

new_matrix1 = Matrix(ll)
matrix1 = Matrix(ll1)
matrix2 = Matrix(ll)
matrix1.__str__()
print()
(matrix1 + matrix2).__str__()

