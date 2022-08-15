class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def get_asphalt_mass(self) -> int:
        return self._length * self._width * 25 * 5


if __name__ == "__main__":
    road = Road(100, 2)
    result = road.get_asphalt_mass()

    print(result)
