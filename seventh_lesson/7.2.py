from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_costs(self):
        pass


class Coat(Clothes):
    def __init__(self, v: int):
        self.__v = v

    def fabric_costs(self) -> float:
        return round(self.__v/6.5 + 0.5, 2)

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, new_v):
        if isinstance(new_v, int):
            self.__v = new_v


class Suit(Clothes):
    def __init__(self, h: int):
        self.__h = h

    def fabric_costs(self) -> float:
        return 2 * self.__h + 0.3

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, new_h):
        if isinstance(new_h, int):
            self.__h = new_h


if __name__ == "__main__":
    coat = Coat(42)
    coat.v = 42
    print(coat.fabric_costs())

    suit = Suit(164)
    suit.h = 170
    print(suit.fabric_costs())

