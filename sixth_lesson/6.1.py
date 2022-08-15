import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self) -> str:
        rules = {
            "red": {
                "color": "\033[91m",
                "lag": 1
            },
            "yellow": {
                "color": "\033[93m",
                "lag": 1
            },
            "green": {
                "color": "\033[92m",
                "lag": 1
            }
        }
        while True:
            for color in rules:
                self.__color = color
                time.sleep(rules[self.__color]["lag"])
                yield f"{rules[self.__color]['color']}{self.__color}"
                if self.__color == "green":
                    self.__color = "yellow"
                    time.sleep(rules[self.__color]["lag"])
                    yield f"{rules[self.__color]['color']}{self.__color}"


if __name__ == "__main__":
    trafficlight = TrafficLight()
    for light in trafficlight.running():
        print(light)
