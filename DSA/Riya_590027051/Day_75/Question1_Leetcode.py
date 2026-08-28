from collections import deque


def largest_path_value(colors, edges):
    n = len(colors)

    # Create adjacency list
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    # Build the graph
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # dp[node][color]
    # Maximum number of times a color appears
    # in a path ending at this node
    dp = [[0] * 26 for _ in range(n)]

    # Queue for Topological Sort
    queue = deque()

    # Add nodes with no incoming edges
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    processed = 0
    answer = 0

    # Topological Sort
    while queue:
        node = queue.popleft()
        processed += 1

        # Get the color index of current node
        color_index = ord(colors[node]) - ord('a')

        # Include current node's color
        dp[node][color_index] += 1

        # Update answer
        answer = max(answer, dp[node][color_index])

        # Visit neighbors
        for neighbor in graph[node]:

            # Update color counts for neighbor
            for color in range(26):
                dp[neighbor][color] = max(
                    dp[neighbor][color],
                    dp[node][color]
                )

            # Remove the edge
            indegree[neighbor] -= 1

            # If no incoming edges remain
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If some nodes were not processed,
    # the graph contains a cycle
    if processed != n:
        return -1

    return answer


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

if __name__ == "__main__":

    # Example 1
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]

    result = largest_path_value(colors, edges)

    print("Example 1")
    print("Colors:", colors)
    print("Edges:", edges)
    print("Largest Color Value:", result)

    print()

    # Example 2
    colors = "a"
    edges = [[0, 0]]

    result = largest_path_value(colors, edges)

    print("Example 2")
    print("Colors:", colors)
    print("Edges:", edges)
    print("Largest Color Value:", result)