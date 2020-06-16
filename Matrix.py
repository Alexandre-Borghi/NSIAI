from operator import __getitem__


def is_number(n):
    return str(n).replace(".", "", 1).replace("-", "", 1).isdigit()


class BadMatrixMultiplication(ArithmeticError):
    """
    A class representing the error that happens when
    trying to multiply 2 matrices that cannot be multiplied.
    """

    pass


class InvalidDataSizeError(ValueError):
    """
    A class representing the error occuring when using
    set_data() and putting too much or not enough data
    in a matrix.
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
        if type(b) != Matrix:
            raise ArithmeticError("Trying to matrix multiply with a non-matrix object")

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
        """
        This function returns matrix "a" multiplied by scalar "b"
        """

        if not is_number(b):
            raise ArithmeticError(
                "* operator is for scalar multiplication. If trying to matrix multiply, use the @ operator."
            )

        new_matrix = Matrix(a.m, a.n)
        new_matrix.set_data_2d(a.data)

        for i in range(new_matrix.m):
            for j in range(new_matrix.n):
                new_matrix[i][j] *= b

        return new_matrix

    @classmethod
    def element_multiply(cls, a, b):
        """
        This function returns matrix "a" element-wise multiplied by matrix "b"
        """

        if a.m != b.m or a.n != b.n:
            raise ArithmeticError()

        new_matrix = Matrix(a.m, a.n)
        new_matrix.set_data_2d(a.data)

        for i in range(new_matrix.m):
            for j in range(new_matrix.n):
                new_matrix[i][j] *= b[i][j]

        return new_matrix

    @classmethod
    def addition(cls, a, b):
        """
        "a" and "b" are matrices. Returns a + b.
        """

        if a.m != b.m or a.n != b.n:
            raise ArithmeticError()

        result_mat = Matrix(a.m, a.n)
        result_mat.set_data_2d(a.data)

        for i in range(result_mat.m):
            for j in range(result_mat.n):
                result_mat[i][j] += b[i][j]

        return result_mat

    @classmethod
    def subtract(cls, a, b):
        return a + (-b)

    @classmethod
    def negate(cls, matrix):
        """
        This method negates matrix "matrix"
        """

        return Matrix.scalar_multiply(matrix, -1)

    @classmethod
    def matrix_transpose(cls, matrix):
        transposed_matrix = Matrix(matrix.n, matrix.m)

        for i in range(transposed_matrix.m):
            for j in range(transposed_matrix.n):
                transposed_matrix[i][j] = matrix.data[j][i]

        return transposed_matrix

    def set_data(self, new_data):
        """
        This function helps to set the data of the entire
        matrix.

        new_data is the 1D array with the new data, with rows
        one after the other
        """

        if self.m * self.n < len(new_data):
            print(
                f"Error : Too much data in array, for a {self.m}x{self.n} matrix, the length of the array should be {self.m*self.n}, but was {len(new_data)}."
            )
            raise InvalidDataSizeError()
        elif self.m * self.n > len(new_data):
            print(
                f"Error : Not enough data in array, for a {self.m}x{self.n} matrix, the length of the array should be {self.m*self.n}, but was {len(new_data)}"
            )
            raise InvalidDataSizeError()

        for i in range(self.m):
            for j in range(self.n):
                self.data[i][j] = new_data[j + i * self.n]

    def set_data_2d(self, new_data):
        """
        This function helps to set the data of the entire
        matrix.

        new_data is the 2D array with the new data, with
        columns in rows.
        """

        if self.m * self.n < len(new_data) * len(new_data[0]):
            print(
                f"Error : Too much data in array, for a {self.m}x{self.n} matrix, the  array should be {self.m}x{self.n}, but was {len(new_data)}x{len(new_data[0])}."
            )
            raise InvalidDataSizeError()
        elif self.m * self.n > len(new_data) * len(new_data[0]):
            print(
                f"Error : Not enough data in array, for a {self.m}x{self.n} matrix, the  array should be {self.m}x{self.n}, but was {len(new_data)}x{len(new_data[0])}."
            )
            raise InvalidDataSizeError()

        for i in range(self.m):
            for j in range(self.n):
                self.data[i][j] = new_data[i][j]

    def __getitem__(self, offset):
        return self.data[offset]

    def __add__(self, other):
        return Matrix.addition(self, other)

    def __iadd__(self, other):
        return Matrix.addition(self, other)

    def __sub__(self, other):
        return Matrix.subtract(self, other)

    def __isub__(self, other):
        return Matrix.subtract(self, other)

    def __mul__(self, other):
        return Matrix.scalar_multiply(self, other)

    def __imul__(self, other):
        return Matrix.scalar_multiply(self, other)

    def __matmul__(self, other):
        return Matrix.matrix_multiply(self, other)

    def __imatmul__(self, other):
        return Matrix.matrix_multiply(self, other)

    def __neg__(self):
        return Matrix.negate(self)

    def __eq__(self, other):
        if type(other) != Matrix:
            raise ArithmeticError("Trying to compare matrix with a non-matrix object")

        return (self.m == other.m) and (self.n == other.n) and (self.data == other.data)

    def __ne__(self, other):
        if type(other) != Matrix:
            raise ArithmeticError("Trying to compare matrix with a non-matrix object")

        return self.m != other.m or self.n != other.n or self.data != other.data
