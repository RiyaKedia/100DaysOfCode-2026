def dfs(node, graph, visited):
    stack = [node]
    visited[node] = True
    size = 0

    while stack:
        current = stack.pop()
        size += 1

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return size


def solve(n, edges):
    # Create adjacency list
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)

    components = 0
    largest_cluster = 0

    # Find connected components
    for village in range(1, n + 1):
        if not visited[village]:
            components += 1

            cluster_size = dfs(village, graph, visited)

            largest_cluster = max(largest_cluster, cluster_size)

    return components, largest_cluster


# -----------------------------
# Main Program
# -----------------------------

n = int(input("Enter number of villages: "))
m = int(input("Enter number of roads: "))

edges = []

print("Enter the roads:")

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

components, largest_cluster = solve(n, edges)

print("Number of wells needed:", components)
print("Largest cluster size:", largest_cluster)