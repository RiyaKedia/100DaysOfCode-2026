# Buy Two Chocolates

# Take input
prices = list(map(int, input("Enter chocolate prices: ").split()))
money = int(input("Enter money: "))

# Find the two cheapest chocolates
prices.sort()

# Cost of the two cheapest chocolates
cost = prices[0] + prices[1]

# Check if we have enough money
if cost <= money:
    remaining = money - cost
else:
    remaining = money

# Print the remaining money
print("Remaining money:", remaining)