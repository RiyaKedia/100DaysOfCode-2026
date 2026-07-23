from collections import deque

# Take input
n = int(input("Enter n: "))

deck = deque()

# Build the deck in reverse order
for card in range(n, 0, -1):
    if deck:
        deck.appendleft(deck.pop())

    deck.appendleft(card)

print("Initial deck arrangement:", list(deck))