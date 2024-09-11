#7 to read a card as input and output if the card is lucky or not

print("-----------Find a card is lucky or not---------")

lucky_cards = [ '7', '10', 'Queen', 'King', 'Ace']

# all suits  Hearts, Diamonds, Clubs, Spades

card = input("Enter a card (e.g. 5 of Hearts): ")

if card in lucky_cards:
    print(f"{card} is a lucky card!")
else:
    print(f"{card} is not a lucky card.")