import unittest
import Matrix


class TestMatrix(unittest.TestCase):

    def test_CreateMatrix(self):
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


if __name__ == "__main__":
    unittest.main()
