import unittest
import Matrix


class TestMatrix(unittest.TestCase):
    def test_MatrixCreation(self):
        matrix = Matrix.Matrix(2, 3)

        self.assertEqual(matrix.m, 2, "Matrix does not have the good amount of lines.")
        self.assertEqual(matrix.n, 3, "Matrix does not have the good amount of rows.")

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

        self.assertRaises(
            Matrix.InvalidDataSizeError, lambda: matrix.set_data([1, 2, 3])
        )
        self.assertRaises(
            Matrix.InvalidDataSizeError, lambda: matrix.set_data([1, 2, 3, 4, 5])
        )

    def test_MatrixMultiplication(self):
        matrix1 = Matrix.Matrix(2, 2, init_value=0)
        matrix2 = Matrix.Matrix(3, 2, init_value=0)

        self.assertRaises(Matrix.BadMatrixMultiplication, lambda: matrix1 @ matrix2)

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
        matrix = Matrix.Matrix(2, 2)
        result_matrix = Matrix.Matrix(2, 2)

        for data in [[1, 2, 3, 4], [-1, -2, -3, -4], [0.1, -5.2, 4.3, -0.5]]:
            for scalar in [0.1, -1, 1, 2, 3, 0]:
                matrix.set_data(data)
                matrix *= scalar

                result_matrix.set_data([n * scalar for n in data])

                self.assertEqual(
                    matrix, result_matrix, "Failed scalar multiplication test."
                )

    def test_MatrixAdd(self):
        matrix1 = Matrix.Matrix(2, 2, init_value=1)
        matrix2 = Matrix.Matrix(3, 2, init_value=1)

        self.assertRaises(ArithmeticError, lambda: matrix1 + matrix2)

        matrix2 = Matrix.Matrix(2, 2)
        result_mat = Matrix.Matrix(2, 2)

        matrix1.set_data([2.7, 1, 5.6, 3])
        matrix2.set_data([4, 1.2, 5, 3.7])
        result_mat.set_data([6.7, 2.2, 10.6, 6.7])

        added_matrix = Matrix.Matrix(2, 2)

        added_matrix = matrix1 + matrix2

        self.assertEqual(added_matrix, result_mat)

        matrix1 += matrix2

        self.assertEqual(matrix1, result_mat)

    def test_MatrixNeg(self):
        matrix = Matrix.Matrix(2, 2)
        result_matrix = Matrix.Matrix(2, 2)

        matrix.set_data([1, 2, -3, -4])
        result_matrix.set_data([-1, -2, 3, 4])

        self.assertEqual(-matrix, result_matrix)

    def test_MatrixSub(self):
        matrix1 = Matrix.Matrix(2, 2)
        matrix2 = Matrix.Matrix(2, 2)

        matrix1.set_data([-1, 2, -3, 4])
        matrix2.set_data([-5, 6, 7, -8])

        result_mat = Matrix.Matrix(2, 2)

        result_mat.set_data([4, -4, -10, 12])

        self.assertEqual(matrix1 - matrix2, result_mat)

        matrix1 -= matrix2

        self.assertEqual(matrix1, result_mat)

    def test_MatrixTranspose(self):
        matrix = Matrix.Matrix(2, 3)
        matrix.set_data([1, 2, 3, 0, -6, 7])

        transposed_matrix = Matrix.Matrix(3, 2)
        transposed_matrix.set_data([1, 0, 2, -6, 3, 7])

        self.assertEqual(Matrix.Matrix.matrix_transpose(matrix), transposed_matrix)


if __name__ == "__main__":
    unittest.main()
