def minimum_coins(coins, amount):
    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        # Take as many of the current coin as possible
        count += amount // coin
        amount = amount % coin

        # If amount becomes 0, we are done
        if amount == 0:
            break

    return count


# Taking input from user
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

# Find minimum number of coins
result = minimum_coins(coins, amount)

# Display result
if amount == 0:
    print("Minimum number of coins:", 0)
else:
    print("Minimum number of coins:", result)