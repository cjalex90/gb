my_list = []

goods_count = 0
while True:  # Actually while not EOF
    try:
        goods = {}
        goods["Название"] = input("Введите название товара: ")
        goods["Цена"] = int(input("Введите цену товара: "))
        goods["Количество"] = int(input("Введите количество товара: "))
        goods["Единица"] = input("Введите единицу измерения: ")
        goods_count += 1
        tuple_goods = (goods_count, goods)
        my_list.append(tuple_goods)
        print("Товар добавлен")
    except EOFError:
        break

my_dict = {}

for goods in my_list:
    goods_params = goods[1]
    for key, value in goods_params.items():
        if key not in my_dict:
            my_dict[key] = []
        my_dict[key].append(value)

my_dict["Единица"] = list(set(my_dict["Единица"]))

print(f"Статистика по товарам:\n{my_dict}")
