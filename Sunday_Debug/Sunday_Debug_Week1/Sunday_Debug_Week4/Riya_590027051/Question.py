def min_boats(weights, limit):
    # Sort weights in ascending order
    weights.sort()

    left = 0
    right = len(weights) - 1
    boats = 0

    while left <= right:
        # Pair the lightest and heaviest soldier if possible
        if weights[left] + weights[right] <= limit:
            left += 1

        # Heaviest soldier always boards
        right -= 1
        boats += 1

    return boats


# Input
weights = list(map(int, input("Enter soldier weights: ").split()))
limit = int(input("Enter boat weight limit: "))

# Output
print(min_boats(weights, limit))