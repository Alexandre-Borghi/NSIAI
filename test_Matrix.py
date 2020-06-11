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


if __name__ == "__main__":
    unittest.main()
