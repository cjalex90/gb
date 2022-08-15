class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self) -> None:
        print(f"{self.title}: Запуск отрисовки")


class Pen(Stationery):
    def draw(self) -> None:
        super().draw()
        print("Рисуем круг")


class Pencil(Stationery):
    def draw(self) -> None:
        super().draw()
        print("Рисуем треугольник")


class Handle(Stationery):
    def draw(self) -> None:
        super().draw()
        print("Рисуем квадрат")


if __name__ == "__main__":
    pen = Pen("parker")
    pen.draw()

    pencil = Pencil("bic")
    pencil.draw()

    handle = Handle("brauberg")
    handle.draw()
