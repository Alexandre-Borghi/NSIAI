from operator import __getitem__


class BadMatrixMultiplication(ArithmeticError):
    """
    A class representing the error that happens when trying to multiply 2 matrices that cannot be multiplied.
    """

    pass


class Matrix:
    """
    This class represents a matrix of any size.

    self.m is the number of rows and self.n is the number of columns.
    """

    def __init__(self, rows, columns, init_value=None):
        self.m = rows
        self.n = columns

        self.data = [[init_value for n in range(
            self.n)] for _ in range(self.m)]

    def display(self):
        for row in range(self.m):
            line = ""
            for column in range(self.n):
                line += f"{self[row][column]} "

            print(line)

    def matrix_multiply(self, other):
        self = Matrix.multiply(self, other)

    @classmethod
    def multiply(cls, a, b):
        if a.n != b.m:
            raise BadMatrixMultiplication(
                f"Trying to multiply a {a.m}x{a.n} matrix with a {b.m}x{b.n} matrix."
            )

        result_mat = Matrix(a.m, b.n, 0)

        for i in range(result_mat.m):
            for j in range(result_mat.n):
                for n in range(a.n):
                    result_mat[i][j] += a[i][n] * b[n][j]

        return result_mat

    def _scalar_multiply(self, other):
        raise NotImplementedError(
            "Matrix scalar multiplication not defined yet.")

    def __getitem__(self, offset):
        return self.data[offset]

    def __mul__(self, other):
        if type(other) == Matrix:
            Matrix.matrix_multiply(self, other)
        else:
            self._scalar_multiply(other)
