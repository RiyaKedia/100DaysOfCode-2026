# Minimum Path Sum using Dynamic Programming

# Taking input
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

grid = []

print("Enter the grid:")
for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# First row
for j in range(1, n):
    grid[0][j] = grid[0][j] + grid[0][j - 1]

# First column
for i in range(1, m):
    grid[i][0] = grid[i][0] + grid[i - 1][0]

# Calculate minimum path sum
for i in range(1, m):
    for j in range(1, n):
        grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])

# Final answer
print("Minimum Path Sum:", grid[m - 1][n - 1])