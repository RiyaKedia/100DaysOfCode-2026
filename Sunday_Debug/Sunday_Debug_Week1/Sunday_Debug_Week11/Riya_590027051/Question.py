# iWeek 11 — The Nether Portal Network
# Kruskal's Algorithm + Disjoint Set Union (DSU)

n, m = map(int, input().split())

edges = []

for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))

# Consider cheaper connections first
edges.sort()

parent = list(range(n + 1))
rank = [0] * (n + 1)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


total_cost = 0
connections = 0

for cost, u, v in edges:
    root_u = find(u)
    root_v = find(v)

    # Add edge only if it connects two separate groups
    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        total_cost += cost
        connections += 1

        # MST is complete
        if connections == n - 1:
            break

# If all portals cannot be connected
if connections == n - 1:
    print(total_cost)
else:
    print(-1)