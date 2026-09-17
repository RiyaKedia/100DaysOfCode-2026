T = int(input("Enter available time: "))
duration = list(map(int, input("Enter durations: ").split()))
happiness = list(map(int, input("Enter happiness points: ").split()))

n = len(duration)

dp = [0] * (T + 1)

for i in range(n):
    for t in range(T, duration[i] - 1, -1):
        dp[t] = max(dp[t], dp[t - duration[i]] + happiness[i])

print("Maximum happiness:", dp[T])