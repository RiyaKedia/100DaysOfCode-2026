def closestMeetingNode(edges, node1, node2):
    n = len(edges)

    # Distance from node1
    dist1 = [-1] * n
    curr = node1
    distance = 0

    while curr != -1 and dist1[curr] == -1:
        dist1[curr] = distance
        distance += 1
        curr = edges[curr]

    # Distance from node2
    dist2 = [-1] * n
    curr = node2
    distance = 0

    while curr != -1 and dist2[curr] == -1:
        dist2[curr] = distance
        distance += 1
        curr = edges[curr]

    # Find the closest common node
    answer = -1
    min_distance = float('inf')

    for i in range(n):
        if dist1[i] != -1 and dist2[i] != -1:
            maximum = max(dist1[i], dist2[i])

            if maximum < min_distance:
                min_distance = maximum
                answer = i

    return answer


# -------------------------------
# Main Program
# -------------------------------

n = int(input("Enter number of nodes: "))

edges = list(map(int, input("Enter edges: ").split()))

node1 = int(input("Enter node1: "))
node2 = int(input("Enter node2: "))

result = closestMeetingNode(edges, node1, node2)

print("Closest meeting node:", result)