my_list = [7, 5, 3, 3, 2]

new_item = int(input(f"Текущий рейтинг: {my_list}\nВведите новый элемент в рейтинг: "))

min_element = new_item
element_index = 0

for index, element in enumerate(my_list):
    if element < min_element:
        min_element = element
    if element == new_item:
        element_index = index

if new_item == min_element:
    element_index = len(my_list)
if element_index:
    element_index += 1

my_list.insert(element_index, new_item)

print(f"Итоговый рейтинг: {my_list}")
