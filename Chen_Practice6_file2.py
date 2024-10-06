postcode = {"A":"Newfoundland",
"B":"Nova Scotia",
"C":"Prince Edward Island",
"E":"New Brunswick",
"G":"Quebec", "H":"Quebec", "J":"Quebec",
"K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario",
"R":"Manitoba",
"S":"Saskatchewan",
"T":"Alberta",
"V":"British Columbia",
"X":"Nunavut",
"X":"Northwest Territories",
"Y":"Yukon"}

def letter(code):
    if len(code) != 3:
        return"Помилка: Формат введення має складатися з трьох цифр" 
    
    code = code.upper()

    if not (code[0].isalpha() and code[1].isdigit() and code[2].isalpha()):
        return'Помилка: формат введення має бути літерами, цифрами, літерами.'

    if code[0] not in postcode:
        return'Помилка, перша літера не відповідає жодній провінції Канади'
    
    region = 'сільській місцевості' if code[1] == '0' else 'міській місцевості'
    location = postcode[code[0]]

    result = f"Поштовий індекс {code} вказує на {region} у {location}."
    return result

user = input('Будь ласка, введіть поштовий індекс: ')
print(letter(user))