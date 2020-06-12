import unittest
import Matrix


class TestMatrix(unittest.TestCase):
    def test_MatrixCreation(self):
        matrix = Matrix.Matrix(2, 3)

        self.assertEqual(
            matrix.m, 2, "Matrix does not have the good amount of lines.")
        self.assertEqual(
            matrix.n, 3, "Matrix does not have the good amount of rows.")

        for value in [0, -1, 10, 3.141592, 2.718281828]:
            matrix = Matrix.Matrix(2, 3, init_value=value)

            for i in range(2):
                for j in range(3):
                    self.assertEqual(
                        matrix[i][j], value, "Matrix init_value is not respected."
                    )

    def test_MatrixGetItemOperator(self):
        matrix = Matrix.Matrix(1, 1)

        self.assertEqual(matrix[0][0], None)

        for value in [-203.56, -1, 0, 2, 35.27, 2358.111]:
            matrix[0][0] = value
            self.assertEqual(
                matrix[0][0],
                value,
                "Matrix __getitem__ operator does not work properly.",
            )

    def test_MatrixSetData(self):
        m, n = 2, 2

        matrix = Matrix.Matrix(m, n)

        for data in [[1, 2, 3, 4], [0.1, 2.3, 1.4, -1.2]]:
            matrix.set_data(data)
            for i in range(matrix.m):
                for j in range(matrix.n):
                    self.assertEqual(matrix[i][j], data[j + i * n])

        self.assertRaises(Matrix.InvalidDataLengthError,
                          lambda: matrix.set_data([1, 2, 3]))
        self.assertRaises(Matrix.InvalidDataLengthError,
                          lambda: matrix.set_data([1, 2, 3, 4, 5]))

    def test_MatrixMultiplication(self):
        matrix1 = Matrix.Matrix(2, 2, init_value=0)
        matrix2 = Matrix.Matrix(3, 2, init_value=0)

        self.assertRaises(Matrix.BadMatrixMultiplication,
                          lambda: matrix1 @ matrix2)

        matrix1 = Matrix.Matrix(2, 2, init_value=0)
        matrix2 = Matrix.Matrix(3, 2, init_value=0)

        matrix2 @= matrix1

        # The result of the multiplication is all zeros
        result_matrix = Matrix.Matrix(3, 2, init_value=0)

        self.assertEqual(matrix2, result_matrix)

        matrix1 = Matrix.Matrix(3, 3)
        matrix2 = Matrix.Matrix(3, 2)

        matrix1.set_data([2, -4.1, 10, -6, 1, 3, 3, 7, -30])
        matrix2.set_data([3, -7, 6, 8, -5, 1])

        # The expected result
        result_matrix = Matrix.Matrix(3, 2)

        result_matrix.set_data([-68.6, -36.8, -27, 53, 201, 5])

        matrix_multiplied = matrix1 @ matrix2

        self.assertEqual(matrix_multiplied, result_matrix)

    def test_MatrixScalarMultiplication(self):
        pass


if __name__ == "__main__":
    unittest.main()
