

class Cell:
    def __init__(self, element_count: int):
        self.element_count = element_count

    def __add__(self, other):
        return Cell(self.element_count + other.element_count)

    def __sub__(self, other):
        subtraction = self.element_count - other.element_count
        if subtraction > 0:
            return Cell(subtraction)
        else:
            print("Разность количества ячеек двух клеток должна быть больше нуля")

    def __mul__(self, other):
        return Cell(self.element_count * other.element_count)

    def __truediv__(self, other):
        return Cell(self.element_count // other.element_count)

    @staticmethod
    def make_order(cell, count: int):
        lines, rest = divmod(cell.element_count, count)
        return "".join(["*" * count + "\n" for _ in range(lines)]) + "*" * rest


if __name__ == "__main__":
    cell1 = Cell(15)
    cell2 = Cell(10)
    cell3 = Cell(5)
    cell4 = Cell(12)

    print((cell1 - cell2).element_count)
    print((cell1 + cell2).element_count)
    print((cell1 * cell2).element_count)
    print((cell1 / cell3).element_count)
    print(Cell.make_order(cell4, 5))
