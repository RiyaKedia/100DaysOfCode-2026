# The Signal Relay
# 0/1 Knapsack using Dynamic Programming

# Taking input
T = int(input("Enter available time: "))

n = int(input("Enter number of activities: "))

duration = list(map(int, input("Enter duration of activities: ").split()))
happiness = list(map(int, input("Enter happiness points: ").split()))

# DP array
dp = [0] * (T + 1)

# Process each activity
for i in range(n):
    for t in range(T, duration[i] - 1, -1):

        # Choose the maximum between:
        # 1. Skipping the activity
        # 2. Taking the activity
        dp[t] = max(dp[t], dp[t - duration[i]] + happiness[i])

# Final answer
print("Maximum Happiness:", dp[T])