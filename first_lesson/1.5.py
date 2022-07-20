earnings = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))

result_text = "Финансовый результат"
if earnings > costs:
    profit = earnings / costs
    print(f"{result_text}: прибыль. Рентабельность: {profit:.2f} или {profit * 100:.2f}%")
    employees_number = int(input("Введите число сотрудников: "))
    profit_per_employee = profit / employees_number
    print(f"Прибыль на одного сотрудника: {profit_per_employee:.2f} или {profit_per_employee * 100:.2f}%")
else:
    print(f"{result_text}: убыток")
