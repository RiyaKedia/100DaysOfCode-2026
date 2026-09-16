n = int(input("Enter stick length: "))
cuts = list(map(int, input("Enter cut positions: ").split()))

cuts = [0] + sorted(cuts) + [n]

m = len(cuts)
dp = [[0] * m for _ in range(m)]

for length in range(2, m):
    for left in range(m - length):
        right = left + length
        dp[left][right] = float('inf')

        for cut in range(left + 1, right):
            cost = cuts[right] - cuts[left] + dp[left][cut] + dp[cut][right]
            dp[left][right] = min(dp[left][right], cost)

print("Minimum cost:", dp[0][m - 1])

