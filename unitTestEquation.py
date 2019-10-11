import unittest
from Practica3 import EquationSolver


class TestEquacio(unittest.TestCase):

    def test_positiu(self):
        eq = EquationSolver("2x + 3 = 7")
        self.assertEqual(eq.resolve(), 2.0)

    def test_buit(self):
        eq = EquationSolver("2x +   = 7")
        self.assertEqual(eq.resolve(), "Operador invalido")


    def test_negatiu(self):
        eq = EquationSolver("2x - 3 = 7")
        self.assertEqual(eq.resolve(), 5)

    def test_float(self):
        eq = EquationSolver("2.3x - 8.4 = 9.8")
        self.assertEqual(eq.resolve(), 7.913043478260872)

    def test_caracterErroni(self):
        eq = EquationSolver("2x - p = 7")
        self.assertEqual(
            eq.resolve(), "Valores no admitidos")

    def test_fromat_erroni(self):
        eq = EquationSolver("3 - 2x = 7")
        self.assertEqual(
            eq.resolve(), "Operador invalido")


if __name__ == '__main__':
    unittest.main()
