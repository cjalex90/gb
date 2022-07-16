seconds = int(input("Введите время в секундах: "))

seconds_in_hour = 3600
seconds_in_minute = 60

calculate_hours = seconds // seconds_in_hour
calculate_minutes = seconds % seconds_in_hour // seconds_in_minute
calculate_seconds = seconds % seconds_in_hour % seconds_in_minute


print(f"Время: {calculate_hours:02d}:{calculate_minutes:02d}:{calculate_seconds:02d}")