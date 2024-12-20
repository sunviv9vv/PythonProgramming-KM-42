import numpy as np

years = np.arange(1900, 2024, 1).tolist()

def leapyears(years):
    return [year for year in years if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))]

def month_leap(month, year, leap_years):
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if month == 2 and year in leap_years:
        return 29

    return month_days[month]

try:

    month = int(input("Please enter the number of month (1-12): "))
    year = int(input("Please enter the year (between 1900 and 2024): "))

    if 1 <= month <= 12 and 1900 <= year <= 2024:
        leap_years = leapyears(years)  
        print(f"The number of days in {year}.{month} is: {month_leap(month, year, leap_years)}")
    else:
        if month < 1 or month > 12:
            print("Invalid month")
        if not (1900 <= year <= 2024):
            print("Invalid year")
            
except ValueError:
    print('Error, please enter a valid number!')