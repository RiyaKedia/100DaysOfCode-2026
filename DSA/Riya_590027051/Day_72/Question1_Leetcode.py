# Find the center of a star graph

def findCenter(edges):
    # Take the first two edges
    a, b = edges[0]
    c, d = edges[1]

    # The center must be common to both edges
    if a == c or a == d:
        return a
    else:
        return b


# Input
edges = [[1, 2], [2, 3], [4, 2]]

# Find and print the center
center = findCenter(edges)

print("Center of the star graph:", center)