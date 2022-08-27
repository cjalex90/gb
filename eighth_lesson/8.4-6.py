from abc import ABC

# TODO
"""
1. Добавить возможность завести новый склад
2. Добавить возможность передачи товара в магазин
3. Устранить все warnings из PyCharm
4. Сделать нижеописанные TODO
"""


class Stock:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self._products = dict()
        self.capacity = capacity

    def __str__(self):
        return f"{self.name}. Количество свободных мест: {self.capacity}"

    def accept(self, product, count):
        if self.capacity > count:
            if product not in self.products:
                self.products[product] = count
            else:
                self.products[product] += count
            self.capacity -= count
        else:
            raise ChooseEx(count)

    def send2shop(self, product, count):
        if self.products[product] and self.products[count] >= count:
            self.products[count] += count
        else:
            self.products[count] = count
            self.capacity -= count

    @property
    def products(self):
        return self._products


class OfficeEquipment(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Printer(OfficeEquipment):
    print_name = "Принтер"
    terms = "Бренд, модель и тип печати"

    def __init__(self, brand, model, print_type):
        super().__init__(brand, model)
        self.print_type = print_type

    def __str__(self):
        return "Принтер"


class Scanner(OfficeEquipment):
    print_name = "Сканер"
    terms = "Бренд, модель и тип сканера"

    def __init__(self, brand, model, scan_type):
        super().__init__(brand, model)
        self.scan_type = scan_type


class Xerox(OfficeEquipment):
    print_name = "Ксерокс"
    terms = "Бренд, модель и тип ксерокопирования"

    def __init__(self, brand, model, xerox_type):
        super().__init__(brand, model)
        self.xerox_type = xerox_type


class ChooseEx(Exception):
    def __init__(self, variant):
        self.variant = variant

    def __str__(self):
        error = f"\033[91mВведено недопустимое значение: {self.variant}"
        error += "\nПовторите ввод!\033[0m"
        return error


def choice(_user_text: str, _input_text: str, _objects: dict):
    # TODO Использование этой функции кажется кривым решением. Придумать другой вариант
    while True:
        try:
            print(_user_text)
            for num_, element in _objects.items():
                if hasattr(element, "print_name"):
                    element = element.print_name
                print(f"{num_}: {element}")
            choice_number = input(f"\n{_input_text}: ")
            if choice_number.isdigit():
                current_number = int(choice_number)
                if current_number in _objects:
                    _current_choice = _objects[current_number]
                    return _current_choice
                else:
                    raise ChooseEx(choice_number)
            else:
                raise ChooseEx(choice_number)
        except ChooseEx:
            print(ChooseEx(choice_number))
            continue


if __name__ == "__main__":
    stocks = {
        1: Stock(name="Основной склад", capacity=10),  # Как бы берем данные из бд
    }
    current_choice = dict()
    # TODO Добавить выход из главного цикла программы по спец.символу
    while True:
        text = "Введите номер склада и нажмите Enter. Список складов:"
        input_text = "Номер склада"
        current_stock = choice(text, input_text, stocks)
        if current_stock:
            text = "Выберите технику, которую нужно завести на складе: "
            input_text = "Номер продукта"
            for num, value in enumerate([name for name in [Printer, Scanner, Xerox]], 1):
                current_choice[num] = value
            current_product = choice(text, input_text, current_choice)
            if current_product:
                text = "Требуется ввести через пробел."
                # TODO Перевести блок в отдельную функцию
                while True:
                    try:
                        product_data = input(f"{text} {current_product.terms}:\n").split()
                        new_product = current_product(*product_data)
                        text = "Введите количество техники: "

                        # TODO проверять в отдельном цикле
                        count_product = int(input(text))
                        current_stock.accept(new_product, count_product)
                        break
                    except:
                        print(ChooseEx(" ".join(product_data)))
                        continue

