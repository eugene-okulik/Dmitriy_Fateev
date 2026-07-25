import random

salary = int(input("Enter your Salary: "))
bonus = random.choice([True, False])

if bonus:
    final_salary = salary + random.randrange(1000, 20000, 500)
else:
    final_salary = salary

print(f"{salary}, {bonus} - '${final_salary}'")
