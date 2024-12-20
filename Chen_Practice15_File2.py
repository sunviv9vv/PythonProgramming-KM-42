def card_deck():
    """Генератор колоди карт (52 штуки)."""
    suits = ("diamonds", "clubs", "hearts", "spades") 
    values = ('A',) + tuple(str(x) for x in range(2, 11)) + ('J', 'Q', 'K') 

    for suit in suits:
        for value in values:
            yield f"{value} {suit}"

deck = card_deck()

while True:
    try:
        print(next(deck)) 
    except StopIteration:
        print("Колода завершена.")
        break