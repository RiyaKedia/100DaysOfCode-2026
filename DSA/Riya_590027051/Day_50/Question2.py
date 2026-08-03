import heapq

# Input
rocks = list(map(int, input().split()))

# Create a max-heap using negative values
heap = [-rock for rock in rocks]
heapq.heapify(heap)

# Smash rocks until at most one remains
while len(heap) > 1:
    first = -heapq.heappop(heap)   # Heaviest
    second = -heapq.heappop(heap)  # Second heaviest

    if first != second:
        heapq.heappush(heap, -(first - second))

# Output
if heap:
    print(-heap[0])
else:
    print(0)