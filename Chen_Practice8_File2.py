import math

try:
    a = float(input("Будь ласка, введіть перший коефіцієт a:"))
    b = float(input("Будь ласка, введіть другий коефіцієт b:"))
    c = float(input("Будь ласка, введіть третій коефіцієт c:"))

    d = b ** 2 - 4 * a * c
    
    if a == 0:
       raise ZeroDivisionError("Коефіцієнт a не може бути дорівнює 0, це не квадратне рівняння.")
    
    if d < 0:
        raise ValueError("Дискримінант менший за 0, неможливо знайти дійсні корені.")
    
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")


except ZeroDivisionError as e:
    print(f"Помилка: {e}")
    print("Спробуйте ввести ненульове значення для коефіцієнта 'a'.")

except ValueError as e:
    print(f"Помилка: {e}")
    print("Перевірте, чи є дискримінант додатним для можливості обчислення коренів.")

except Exception as e:
    print(f"Невідома помилка: {e}")
    print("Щось пішло не так. Перевірте введені значення і спробуйте знову.")
