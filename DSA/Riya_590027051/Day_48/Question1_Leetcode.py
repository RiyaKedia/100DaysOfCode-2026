# Sort the Students by Their K-th Exam Score
# VS Code Python Solution

m, n = map(int, input().split())

score = []
for _ in range(m):
    score.append(list(map(int, input().split())))

k = int(input())

score.sort(key=lambda row: row[k], reverse=True)

for row in score:
    print(*row)