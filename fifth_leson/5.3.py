with open("5.3_source.txt", "r", encoding="utf-8") as f:
    employees_salary = [l.rstrip().split() for l in f.readlines()]
    total_salary = 0
    print("Сотрудники с окладом меньше 20000: ")
    for last_name, salary in employees_salary:
        salary = float(salary)
        total_salary += salary
        if salary < 20000:
            print(last_name)
    print(f"\nCредняя величина дохода сотрудников: {round(total_salary / len(employees_salary))}")

