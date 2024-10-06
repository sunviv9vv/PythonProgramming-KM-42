def letter(words):
    return set(char.lower() for char in words if char.isalpha())


word1 = input("Будь ласка, введіть перший фраз: ")
word2 = input("Будь ласка, введіть другий фраз: ")

basket1 = set(letter(word1))
basket2 = set(letter(word2))

mixchar = basket2 <= basket1

print("Літер в першої фрази: ", f'{letter(basket1)}')
print("Літер в другу фразу: ", f'{letter(basket2)}')

if mixchar:
    print("Ми можемо скласти з літер першої фрази другу фразу.")
else:
    print("Ми не можемо скласти з літер першої фрази другу фразу.")


