R, C = map(int, input().split())

grid = []

for i in range(R):
    row = list(map(int, input().split()))
    grid.append(row)

P = int(input())

for i in range(P):
    r, c, bonus = map(int, input().split())
    grid[r][c] += bonus

# Calculate maximum energy path
for i in range(R):
    for j in range(C):
        if i == 0 and j == 0:
            continue

        if i == 0:
            grid[i][j] += grid[i][j - 1]

        elif j == 0:
            grid[i][j] += grid[i - 1][j]

        else:
            grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])

print(grid[R - 1][C - 1])