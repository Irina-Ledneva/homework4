from sys import argv

name, output_hour, rate_hour, bonus = argv

print("Выработка в часах: ", output_hour)
print("Ставка в час: ", rate_hour)
print("Премия: ", bonus)
print(f"Зарплата сотрудника: {float(output_hour) * float(rate_hour) + float(bonus)}")
