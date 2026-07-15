def final_prices(prices):
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            idx = stack.pop()
            prices[idx] -= prices[i]
        stack.append(i)

    return prices


# Driver Code
prices = list(map(int, input("Enter prices: ").split()))

result = final_prices(prices)

print("Final prices:", *result)