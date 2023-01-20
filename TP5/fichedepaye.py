def calculate_salary(hours_worked, hourly_wage):
    base_salary = hours_worked * hourly_wage
    if hours_worked > 200:
        extra_hours = hours_worked - 200
        extra_salary = extra_hours * hourly_wage * 1.5
        base_salary += extra_salary
    elif hours_worked > 160:
        extra_hours = hours_worked - 160
        extra_salary = extra_hours * hourly_wage * 1.25
        base_salary += extra_salary
    return base_salary

print(f"le salarié devra etre payer {calculate_salary(int(input('quel est le nom : ')), int(input('quel est son taux horaire : ')))}")


