from sys import argv

try:
    args = argv[1:]
    data = {["time_working", "hour_cost", "bonus"][i]: float(args[i]) for i in range(len(args))}
    print("Расчет заработной платы сотрудника: ", end="")
    print(f"{(data['time_working'] * data['hour_cost']) + data['bonus']:.2f}")
except ValueError:
    print("Требуется вводить аргументы в числах")
except:
    print(f"Использование программы: {argv[0]} 'Выработка в часах' 'Cтавка в час' 'Премия'")