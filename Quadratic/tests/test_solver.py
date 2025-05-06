import unittest
from src.quadratic import solve_quadratic


class TestQuadraticSolver(unittest.TestCase):
    def test_deux_racines(self):
        self.assertEqual(set(solve_quadratic(1, -3, 2)), {1.0, 2.0})

    def test_une_racine(self):
        self.assertEqual(solve_quadratic(1, 2, 1), (-1.0,))

    def test_pas_de_solution(self):
        self.assertEqual(solve_quadratic(1, 0, 1), "Pas de solution réelle")

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 1)


if __name__ == "__main__":
    unittest.main()
