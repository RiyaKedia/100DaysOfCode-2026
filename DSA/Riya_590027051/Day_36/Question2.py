from collections import deque

# Input
n = int(input("Enter number of people: "))
k = int(input("Enter person number (k): "))

queue = deque(range(1, n + 1))
minute = 0

while queue:
    minute += 1

    # Serve the front person
    person = queue.popleft()

    # Check if person k is served
    if person == k:
        print(minute)
        break

    # After serving, move the new front person to the back if odd
    if queue and queue[0] % 2 == 1:
        queue.append(queue.popleft())