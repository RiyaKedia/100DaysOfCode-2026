MOD = 10**9 + 7


def ways_to_build_rooms(prevRoom):
    n = len(prevRoom)

    # Create the tree
    children = [[] for _ in range(n)]

    for i in range(1, n):
        parent = prevRoom[i]
        children[parent].append(i)

    # Precompute factorials
    fact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    # Precompute inverse factorials
    inv_fact = [1] * (n + 1)

    inv_fact[n] = pow(fact[n], MOD - 2, MOD)

    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    # Combination function
    def combination(a, b):
        return (
            fact[a]
            * inv_fact[b]
            % MOD
            * inv_fact[a - b]
            % MOD
        )

    # Iterative DFS
    order = []
    stack = [0]

    while stack:
        node = stack.pop()
        order.append(node)

        for child in children[node]:
            stack.append(child)

    # Subtree sizes
    subtree_size = [1] * n

    # Number of ways for each subtree
    ways = [1] * n

    # Process children before parents
    for node in reversed(order):
        total = 0
        result = 1

        for child in children[node]:
            size = subtree_size[child]

            # Number of ways to interleave this subtree
            result = result * combination(total + size, size) % MOD

            # Ways to build the child's subtree
            result = result * ways[child] % MOD

            total += size

        subtree_size[node] = total + 1
        ways[node] = result

    return ways[0]


# -------------------------------
# Main Program
# -------------------------------

prevRoom = list(map(int, input("Enter prevRoom: ").split()))

answer = ways_to_build_rooms(prevRoom)

print("Number of possible orders:", answer)