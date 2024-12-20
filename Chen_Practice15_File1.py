def pascal_triangle(n):
    row = [1]
    for _ in range(n + 1):
        yield row
        row = [sum(pair) for pair in zip([0] + row, row + [0])]

while True:
    try:
        question = int(input("Please enter the power of Newton's binomial (non-negative integer): "))

        if question < 0:
            print("The exponent must be a non-negative number. Please try again.")
            continue
        
        print("Pascal's Triangle:")
        for r in pascal_triangle(question):
            print(" ".join(map(str, r)))
            
        break

    except ValueError:
        print("Please enter a valid integer.")