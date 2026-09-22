# Koko Eating Bananas

# Taking input
piles = list(map(int, input("Enter the banana piles: ").split()))
h = int(input("Enter the number of hours: "))

# Minimum and maximum possible eating speed
low = 1
high = max(piles)

# Binary Search
while low < high:

    # Find middle speed
    k = (low + high) // 2

    # Calculate total hours needed
    hours = 0

    for pile in piles:
        # Ceiling division
        hours += (pile + k - 1) // k

    # If Koko can finish within h hours,
    # try a smaller speed
    if hours <= h:
        high = k

    # If Koko needs more than h hours,
    # increase the speed
    else:
        low = k + 1

# Minimum eating speed
print("Minimum eating speed:", low)