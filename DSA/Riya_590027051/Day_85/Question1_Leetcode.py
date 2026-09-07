def find_content_children(g, s):
    # Sort greed factors and cookie sizes
    g.sort()
    s.sort()

    child = 0
    cookie = 0

    # Try to satisfy each child with the smallest suitable cookie
    while child < len(g) and cookie < len(s):

        if s[cookie] >= g[child]:
            child += 1

        cookie += 1

    return child


# Take input from user
g = list(map(int, input("Enter greed factors of children: ").split()))
s = list(map(int, input("Enter cookie sizes: ").split()))

# Find maximum number of content children
result = find_content_children(g, s)

print("Maximum number of content children:", result)