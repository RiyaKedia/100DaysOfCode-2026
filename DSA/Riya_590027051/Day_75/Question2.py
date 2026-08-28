def minimum_cost(n, roads):
    # Build graph
    # Each edge stores:
    # (neighbor, cost, direction)
    #
    # direction = 0 -> original direction
    # direction = 1 -> reversed direction

    graph = [[] for _ in range(n + 1)]

    for u, v, cost in roads:
        # Original direction: u -> v
        graph[u].append((v, cost, 0))

        # Reversed direction: v -> u
        graph[v].append((u, cost, 1))

    # We need to find the minimum cost orientation
    # that makes all cities part of one directed cycle.
    #
    # For a ring, this can be solved by considering
    # each possible starting direction.

    INF = float('inf')
    answer = INF

    # Try every city as the starting city
    for start in range(1, n + 1):

        # DP/state:
        # dp[city][direction]
        # But because the input describes a ring,
        # we can traverse the cities and calculate
        # the cost of choosing each direction.

        visited = [False] * (n + 1)

        def dfs(city, cost, count):
            nonlocal answer

            if cost >= answer:
                return

            if count == n:
                if city == start:
                    answer = min(answer, cost)
                return

            visited[city] = True

            for next_city, edge_cost, reversed_edge in graph[city]:

                if not visited[next_city]:
                    dfs(
                        next_city,
                        cost + (edge_cost if reversed_edge else 0),
                        count + 1
                    )

            visited[city] = False

        dfs(start, 0, 1)

    return answer


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

if __name__ == "__main__":

    n = 3

    roads = [
        [1, 3, 1],
        [1, 2, 1],
        [3, 2, 1]
    ]

    result = minimum_cost(n, roads)

    print("Number of cities:", n)
    print("Roads:", roads)
    print("Minimum cost:", result)