from collections import deque

n = int(input("Enter n: "))

# Store positions of the cards
queue = deque(range(n))

deck = [0] * n

# Place cards in the order 1 to n
for card in range(1, n + 1):
    # Move the top position to the back
    if queue:
        queue.append(queue.popleft())

    # Place the current card in the next available position
    position = queue.popleft()
    deck[position] = card

print("Initial deck arrangement:", deck)