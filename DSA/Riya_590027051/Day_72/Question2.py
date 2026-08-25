# Really Special SubTree
# Kruskal's Algorithm

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    # Find the parent of a node
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Join two sets
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # Already connected -> adding this edge creates a cycle
        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n, edges):
    # Sort edges according to weight
    edges.sort(key=lambda edge: edge[2])

    dsu = DSU(n)

    total_weight = 0
    edges_used = 0

    # Process edges from smallest weight to largest
    for u, v, weight in edges:

        # Add edge only if it doesn't create a cycle
        if dsu.union(u, v):
            total_weight += weight
            edges_used += 1

            # MST needs exactly n - 1 edges
            if edges_used == n - 1:
                break

    return total_weight


# -----------------------------
# Input
# -----------------------------

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter each edge as: u v weight")

for _ in range(m):
    u, v, weight = map(int, input().split())
    edges.append([u, v, weight])


# Find MST weight
answer = kruskal(n, edges)

print("Minimum Spanning Tree weight:", answer)