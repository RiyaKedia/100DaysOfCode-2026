# Count Unreachable Pairs of Nodes

def count_unreachable_pairs(n, edges):
    # Create adjacency list
    graph = [[] for _ in range(n)]

    # Add edges
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n

    def dfs(start):
        stack = [start]
        visited[start] = True
        size = 0

        while stack:
            node = stack.pop()
            size += 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return size

    answer = 0
    previous_nodes = 0

    # Find all connected components
    for i in range(n):
        if not visited[i]:
            component_size = dfs(i)

            # Pairs between this component
            # and all previous components
            answer += component_size * previous_nodes

            previous_nodes += component_size

    return answer


# -----------------------------
# Main Program
# -----------------------------

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter the edges (u v):")

for _ in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

result = count_unreachable_pairs(n, edges)

print("Number of unreachable pairs:", result)