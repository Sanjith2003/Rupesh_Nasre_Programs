import math

# Total number of cards in a standard deck
total_cards = 52

# Number of spades in a standard deck
spades = 13

# Number of colored cards (Jack, Queen, King) in a standard deck
colored_cards = 12

# Number of spades that are also colored cards
spades_colored = 3

# Number of cards that are neither spades nor colored cards
neither = total_cards - spades - colored_cards + spades_colored

# Probability of drawing a card that is neither a spade nor a colored card
probability = neither / total_cards

# Print the result
print("The probability of drawing a card that is neither a spade nor a colored card is:", probability)
