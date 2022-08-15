class Car:
    def __init__(self, name: str, color: str, speed: int, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self) -> None:
        print(f"{self.name} поехала")

    def stop(self) -> None:
        print(f"{self.name} остановилась")

    def turn(self, direction: str) -> None:
        print(f"{self.name} повернула {direction}")

    def show_speed(self) -> None:
        print(f"Текущая скорость {self.name}: {self.speed}")


class TownCar(Car):
    def show_speed(self) -> None:
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self) -> None:
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):
    pass


if __name__ == "__main__":
    town_car = TownCar("Toyota", "blue", 100)
    town_car.go()
    town_car.turn("направо")
    town_car.show_speed()
    town_car.stop()

    sport_car = SportCar("Dodge", "red", 200)
    sport_car.go()
    sport_car.turn("налево")
    sport_car.show_speed()
    sport_car.stop()

    work_car = WorkCar("Renault", "white", 40)
    work_car.go()
    work_car.turn("налево")
    work_car.show_speed()
    work_car.stop()

    police_car = PoliceCar("Mazda", "black", 120, True)
    police_car.go()
    police_car.turn("направо")
    police_car.show_speed()
    police_car.stop()
