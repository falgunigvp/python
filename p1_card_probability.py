#1 a card is drawn at random from a deck of a well-shuffled cards, find probabilty of it being nether a king nor a spade.

total_cards = 52

c_of_spades=13

c_of_kings_excluding_sk=3

not_k_not_s=(total_cards - c_of_spades - c_of_kings_excluding_sk )


probability = not_k_not_s / total_cards

print("Probability is :", probability) 