
class Matrix:
    def __init__(self, matrix: list):
        if isinstance(matrix, list) and len(matrix) in range(2, 4):
            for m_list in matrix:
                if len(m_list) in range(2, 5) and all(isinstance(i, int) for i in m_list):
                    self.matrix = matrix
                else:
                    print("Каждый вложенный список должен содержать от 2 до 4 чисел")
        else:
            print("Конструктор принимает только список списков!")
            print("Основной список должен содержать от 2 до 3 вложенных списков")

    def __str__(self):
        return "\n".join([" ".join(list(map(str, i))) for i in self.matrix])

    def __add__(self, other):
        try:
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(
                len(self.matrix[0]))] for i in range(len(self.matrix))])
        except IndexError:
            print("Можно складывать только матрицы с одинаковой длинной")


if __name__ == "__main__":
    matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
    matrix2 = Matrix([[31, 32], [37, 43], [51, 86]])
    matrix3 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(matrix1 + matrix2)
    print(matrix3)





