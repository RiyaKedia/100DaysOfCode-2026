def count_landmasses(grid):
    rows = len(grid)
    cols = len(grid[0])

    count = 0

    def dfs(r, c):
        # Check boundaries
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        # If it is water, stop
        if grid[r][c] == '0':
            return

        # Mark land as visited
        grid[r][c] = '0'

        # Move up
        dfs(r - 1, c)

        # Move down
        dfs(r + 1, c)

        # Move left
        dfs(r, c - 1)

        # Move right
        dfs(r, c + 1)

    # Visit every cell
    for i in range(rows):
        for j in range(cols):

            # Found a new landmass
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count


# Input
grid = [
    list("11000"),
    list("11000"),
    list("00100"),
    list("00011")
]

# Output
print(count_landmasses(grid))