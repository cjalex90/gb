class Worker:
    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def get_total_income(self) -> int:
        return sum(self._income.values())


if __name__ == "__main__":
    person_1 = Position("Иван", "Иванов", "Слесарь", wage=25000, bonus=5000)
    print(person_1.get_full_name())
    print(person_1.get_total_income())

    person_2 = Position("Петр", "Петров", "Сантехник", wage=30000, bonus=7000)
    print(person_2.get_full_name())
    print(person_2.get_total_income())
