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
                        matrix[i][j], value, "Matrix init_value is not respected.")

    def test_MatrixGetItemOperator(self):
        matrix = Matrix.Matrix(1, 1)

        self.assertEqual(matrix[0][0], None)

        for value in [-203.56, -1, 0, 2, 35.27, 2358.111]:
            matrix[0][0] = value
            self.assertEqual(
                matrix[0][0], value, "Matrix __getitem__ operator does not work properly.")

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

        matrix1[0][0] = 2.3
        matrix1[0][1] = -4.12
        matrix1[0][2] = 10
        matrix1[1][0] = -6
        matrix1[1][1] = 0.1
        matrix1[1][2] = 3.14
        matrix1[2][0] = 2.7
        matrix1[2][1] = 7.77
        matrix1[2][2] = -30

        matrix1[0][0] = 3.33
        matrix1[0][1] = -7.1
        matrix1[1][0] = 6
        matrix1[1][1] = 8.23
        matrix1[2][0] = -5
        matrix1[2][1] = 1.2

        # The expected result
        result_matrix = Matrix.Matrix(3, 2)

        matrix2[0][0] = -67.06
        matrix2[0][1] = -38.24
        matrix2[1][0] = -35.08
        matrix2[1][1] = 47.19
        matrix2[2][0] = 205.61
        matrix2[2][1] = 8.78

        matrix_multiplied = matrix1 @ matrix2

        matrix_multiplied.display()

        self.assertEqual(matrix_multiplied, result_matrix)


if __name__ == "__main__":
    unittest.main()
