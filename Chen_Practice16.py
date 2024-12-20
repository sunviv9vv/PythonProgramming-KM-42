def check(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The sides of a triangle must be positive numbers.")
    return True

def triangle_ineq(func):
    def wrapper(a,b,c):
        if a + b > c and b + c > a and a + c > b:
            return func(a, b, c)
        else:
            raise ValueError("The sum of distance of 2 sides of a triangle must be bigger than the third one.")
    return wrapper

@triangle_ineq

def area_calculation(a, b, c):
    check(a, b, c)
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area

try:
    a = float(input("Please enter the first side of the triangle: "))
    b = float(input("Please enter the second side of the triangle: "))
    c = float(input("Please enter the third side of the triangle: "))
    check(a, b, c)
    s = area_calculation(a, b, c)

    print(f"The area of triangle is:{s:.2f}")

except ValueError as e:
    print(f"Input error: {e}")
