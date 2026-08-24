def findJudge(n, trust):
    degree = [0] * (n + 1)

    for a, b in trust:
        degree[a] -= 1
        degree[b] += 1

    for person in range(1, n + 1):
        if degree[person] == n - 1:
            return person

    return -1


# Input
n = int(input("Enter number of people: "))

m = int(input("Enter number of trust relationships: "))

trust = []

for _ in range(m):
    a, b = map(int, input().split())
    trust.append([a, b])


# Output
print("Town Judge:", findJudge(n, trust))