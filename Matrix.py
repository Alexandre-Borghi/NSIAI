from operator import __getitem__


def is_number(n):
    return str(n).replace(".", "", 1).isdigit()


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

        self.data = [[init_value for n in range(self.n)] for _ in range(self.m)]

    def display(self):
        for row in range(self.m):
            line = ""
            for column in range(self.n):
                line += f"{self[row][column]} "

            print(line)

    @classmethod
    def matrix_multiply(cls, a, b):
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

    @classmethod
    def scalar_multiply(cls, a, b):
        raise NotImplementedError("Matrix scalar multiplication not defined yet.")

    def __getitem__(self, offset):
        return self.data[offset]

    def __mul__(self, other):
        if not is_number(other):
            raise ArithmeticError(
                "* operator is for scalar multiplication. If trying to matrix multiply, use the @ operator."
            )

        return Matrix.scalar_multiply(self, other)

    def __imul__(self, other):
        if is_number(other):
            raise ArithmeticError(
                "*= operator is for scalar multiplication. If trying to matrix multiply, use the @= operator."
            )

        return Matrix.scalar_multiply(self, other)

    def __matmul__(self, other):
        if type(other) != Matrix:
            raise ArithmeticError("Trying to matrix multiply with a non-matrix object")

        return Matrix.matrix_multiply(self, other)

    def __imatmul__(self, other):
        if type(other) != Matrix:
            raise ArithmeticError("Trying to matrix multiply with a non-matrix object")

        return Matrix.matrix_multiply(self, other)

    def __eq__(self, other):
        if type(other) != Matrix:
            raise ArithmeticError("Trying to compare matrix with a non-matrix object")

        return self.m == other.m and self.n == other.n and self.data == other.data

    def __ne__(self, other):
        if type(other) != Matrix:
            raise ArithmeticError("Trying to compare matrix with a non-matrix object")

        return self.m != other.m or self.n != other.n or self.data != other.data
