class Calculator(object):
    """Класс калькулятора """

    def addition(self, x, y):

        types_numbers = (int, float, complex)
        if isinstance(x, types_numbers) and isinstance(y, types_numbers):
            return x + y
        else:
            return ValueError

    def subtraction(self, x, y):

        types_numbers = (int, float, complex)
        if isinstance(x, types_numbers) and isinstance(y, types_numbers):
            return x - y
        else:
            return ValueError

    def multiplication(self, x, y):

        types_numbers = (int, float, complex)
        if isinstance(x, types_numbers) and isinstance(y, types_numbers):
            return x * y
        else:
            return ValueError

    def division(self, x, y):

        types_numbers = (int, float, complex)
        if isinstance(x, types_numbers) and isinstance(y, types_numbers):
            try:
                return x / y
            except ZeroDivisionError:
                return "На ноль делить нельзя"
        else:
            return ValueError


print(Calculator.addition(Calculator, 7, 6))
print(Calculator.subtraction(Calculator, 10, 2))
print(Calculator.multiplication(Calculator, 10, ' '))
print(Calculator.division(Calculator, 10, 0))
