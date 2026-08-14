def findJudge(n, trust):
    score = [0] * (n + 1)

    for a, b in trust:
        score[a] -= 1
        score[b] += 1

    for person in range(1, n + 1):
        if score[person] == n - 1:
            return person

    return -1


# Input
n = int(input("Enter number of people: "))
m = int(input("Enter number of trust relationships: "))

trust = []

for i in range(m):
    a, b = map(int, input("Enter trust pair: ").split())
    trust.append([a, b])

# Find and print the judge
result = findJudge(n, trust)

print("Town Judge:", result)