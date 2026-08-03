import heapq

# Input
nums = list(map(int, input().split()))
k = int(input())
multiplier = int(input())

# Build min-heap (value, index)
heap = []
for i, val in enumerate(nums):
    heapq.heappush(heap, (val, i))

# Perform k operations
for _ in range(k):
    val, idx = heapq.heappop(heap)
    val *= multiplier
    nums[idx] = val
    heapq.heappush(heap, (val, idx))

# Output
print(*nums)