def fractional_knapsack(value, weight, capacity):
    n = len(value)

    # Create a list of (value, weight, value/weight ratio)
    items = []

    for i in range(n):
        ratio = value[i] / weight[i]
        items.append((ratio, value[i], weight[i]))

    # Sort items by value/weight ratio in descending order
    items.sort(reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    # Select items greedily
    for ratio, val, wt in items:

        if remaining_capacity == 0:
            break

        if wt <= remaining_capacity:
            # Take the whole item
            total_value += val
            remaining_capacity -= wt

        else:
            # Take only the fraction that fits
            fraction = remaining_capacity / wt
            total_value += val * fraction
            remaining_capacity = 0

    return total_value


# Take input from the user
value = list(map(int, input("Enter values: ").split()))
weight = list(map(int, input("Enter weights: ").split()))
capacity = int(input("Enter knapsack capacity: "))

# Calculate maximum value
result = fractional_knapsack(value, weight, capacity)

print("Maximum value:", result)