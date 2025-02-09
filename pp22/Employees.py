from Employee import Employee

employees = []

employees.append(Employee('Jan', 'Kowalski', 20, 4500))
employees.append(Employee('Piort', 'Wiewiura', 20, 2500))
employees.append(Employee('Łukasz', 'Foks', 20, 9500))
employees.append(Employee('Ola', 'Niewiadoma', 20, 41500))
employees.append(Employee('Ania', 'Nowak', 20, 14500))

print("lista płac:")
print("-" * 30)
for employee in employees:
    print(employee.get_full_name(), "wiek:", employee.get_age(), "lat, pensja:", employee.get_salary())