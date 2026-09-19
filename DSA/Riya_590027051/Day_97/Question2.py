# The Energy Tower

N = int(input("Enter number of floors: "))
energy = list(map(int, input("Enter energy values: ").split()))

# dp[i] = maximum energy collected up to floor i
dp = [0] * N

dp[0] = energy[0]

if N > 1:
    dp[1] = energy[0] + energy[1]

for i in range(2, N):
    dp[i] = energy[i] + max(dp[i - 1], dp[i - 2])

print("Maximum total energy:", dp[N - 1])