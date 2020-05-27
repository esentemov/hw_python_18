import unittest
from calculator import Calculator


class CalculatorTextCase(unittest.TestCase):
    """Тесты класса Calculator """

    def setUp(self):
        self.test_calculator = Calculator()

    def test_addition(self):
        """Тест на ввод цифр и результат """

        self.assertEqual(self.test_calculator.addition(10.5, 5), 15.5)
        self.assertEqual(self.test_calculator.subtraction(10, 5), 5)
        self.assertEqual(self.test_calculator.multiplication(-10, 7), -70.0)
        self.assertEqual(self.test_calculator.division(10, 0), "На ноль делить нельзя")

    def test_only_numbers(self):
        """Тест на ввод букв """

        self.assertEqual(self.test_calculator.addition(5, 5), 10)
        self.assertEqual(self.test_calculator.subtraction("chislo", 5), ValueError)
        self.assertEqual(self.test_calculator.multiplication(10, "umnozhit"), ValueError)
        self.assertEqual(self.test_calculator.division(4.0, "privet"), ValueError)

    def test_empty(self):
        """Тест на ввод пустых символов """

        self.assertEqual(self.test_calculator.addition(5, 0), 5)
        self.assertEqual(self.test_calculator.subtraction(5, 0), 5)
        self.assertEqual(self.test_calculator.multiplication(5, ""), ValueError)
        self.assertEqual(self.test_calculator.division(10, ""), ValueError)


if __name__ == "__main__":
    unittest.main()
