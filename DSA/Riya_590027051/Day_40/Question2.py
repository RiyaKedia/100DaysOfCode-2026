from collections import deque


def max_temperatures(temperatures, k):
    result = []
    dq = deque()

    for i in range(len(temperatures)):

        # Remove indices that are outside the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller temperatures from the back
        while dq and temperatures[dq[-1]] <= temperatures[i]:
            dq.pop()

        # Add current temperature index
        dq.append(i)

        # Start adding answers after the first complete window
        if i >= k - 1:
            result.append(temperatures[dq[0]])

    return result


# Input
temperatures = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# Output
answer = max_temperatures(temperatures, k)

print("Highest temperature in every window:", answer)