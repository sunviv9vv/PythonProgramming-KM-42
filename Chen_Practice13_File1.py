import string
from collections import Counter

def analyze_letter_frequency(file_path):

    with open(file_path, 'r') as file:
        text = file.read().lower()

    letters_only = [char for char in text if char in string.ascii_lowercase]

    letter_counts = Counter(letters_only)
    total_letters = sum(letter_counts.values())

    letter_percentages = {
        letter: (count / total_letters) * 100
        for letter, count in letter_counts.items()
    }

    sorted_letters = sorted(
        letter_percentages.items(),
        key=lambda x: (x[0] == 'e', -x[1])
    )

    sorted_letters = [(letter, round(percentage, 3)) for letter, percentage in sorted_letters]

    print("First 5 letters:")
    for letter, percentage in sorted_letters[:5]:
        print(f"{letter}: {percentage}%")
    
    print("\nLast 5 letters:")
    for letter, percentage in sorted_letters[-5:]:
        print(f"{letter}: {percentage}%")

analyze_letter_frequency('gadsby.txt')