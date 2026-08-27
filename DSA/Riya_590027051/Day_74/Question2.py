def max_crab_vertices(C, N, T, M, edges):
    # Build adjacency list
    graph = [[] for _ in range(N + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Match each possible foot to a head.
    # head_used[h] = number of feet currently assigned to head h
    head_used = [0] * (N + 1)

    # foot_head[f] = head currently assigned to foot f
    foot_head = [-1] * (N + 1)

    def can_assign(foot, visited):
        for head in graph[foot]:
            if visited[head]:
                continue

            visited[head] = True

            # If this head still has capacity, assign this foot
            if head_used[head] < T:
                head_used[head] += 1
                foot_head[foot] = head
                return True

            # Try to move one of the head's existing feet
            for other_foot in range(1, N + 1):
                if foot_head[other_foot] == head:
                    if can_assign(other_foot, visited):
                        foot_head[foot] = head
                        return True

        return False

    # Find maximum number of head-foot pairs
    matched = 0

    for foot in range(1, N + 1):
        visited = [False] * (N + 1)

        if can_assign(foot, visited):
            matched += 1

    # Every crab contains:
    # 1 head + number of feet
    #
    # However, a head must be used at least once.
    # The maximum covered vertices are 2 * matched
    # when each matched edge can form a separate head-foot assignment.
    return 2 * matched


# -----------------------------
# Input
# -----------------------------

C = int(input())
N = int(input())
T = int(input())
M = int(input())

edges = []

for _ in range(M):
    u, v = map(int, input().split())
    edges.append([u, v])

# -----------------------------
# Output
# -----------------------------

answer = max_crab_vertices(C, N, T, M, edges)

print(answer)