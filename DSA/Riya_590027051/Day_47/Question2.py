def kth_smallest(A, B, k):
    # Ensure A is the smaller array
    if len(A) > len(B):
        return kth_smallest(B, A, k)

    n, m = len(A), len(B)

    # Search range for partition
    low = max(0, k - m)
    high = min(k, n)

    while low <= high:
        cutA = (low + high) // 2
        cutB = k - cutA

        leftA = float('-inf') if cutA == 0 else A[cutA - 1]
        leftB = float('-inf') if cutB == 0 else B[cutB - 1]

        rightA = float('inf') if cutA == n else A[cutA]
        rightB = float('inf') if cutB == m else B[cutB]

        if leftA <= rightB and leftB <= rightA:
            return max(leftA, leftB)
        elif leftA > rightB:
            high = cutA - 1
        else:
            low = cutA + 1

    return -1


# Input
A = list(map(int, input("Enter elements of first sorted array: ").split()))
B = list(map(int, input("Enter elements of second sorted array: ").split()))
k = int(input("Enter k: "))

# Output
print("K-th smallest element:", kth_smallest(A, B, k))