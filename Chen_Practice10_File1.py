import numpy as np

salarylist = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

newsalary_list = list(map(lambda x: round(x * 1.3, 2), salarylist))

indexation_list = list(map(lambda x: round(x * 0.3, 2), salarylist))

print("Salary table:")
for salary, new_salary, indexation in zip(salarylist, newsalary_list, indexation_list):
    print(f"Original: {salary}\n" f"New: {new_salary}\n" f"Increases: {indexation}" "\n")

print("Salary table:")
for salary, new_salary, indexation in zip(salarylist, newsalary_list, indexation_list):
    print(f"{salary} {new_salary} {indexation}")
    
# Все два працюють, просто може перший виглядає красивіше)