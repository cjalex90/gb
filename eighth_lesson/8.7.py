class ComplexNumber:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.character = "+" if num2 > 0 else "-"

    def __str__(self):
        return f"{self.num1}{self.character}{abs(self.num2)}i"

    def __add__(self, other):
        return ComplexNumber(self.num1 + other.num1, self.num2 + other.num2)

    def __mul__(self, other):
        num1 = self.num1 * other.num1 + self.num2 * other.num1
        num2 = self.num1 * other.num2 - self.num2 * other.num2
        return ComplexNumber(num1, num2)


if __name__ == "__main__":
    complex1 = ComplexNumber(2, 3)
    complex2 = ComplexNumber(-1, 1)

    complex3 = complex1 + complex2
    complex4 = complex1 * complex2

    print(complex3)
    print(complex4)
