def merge_arrays(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge from the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Copy remaining elements of nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


# Input
m = int(input("Enter number of valid elements in nums1 (m): "))
nums1 = list(map(int, input(f"Enter {m} sorted elements of nums1: ").split()))

n = int(input("Enter number of elements in nums2 (n): "))
if n > 0:
    nums2 = list(map(int, input(f"Enter {n} sorted elements of nums2: ").split()))
else:
    nums2 = []

# Add extra space to nums1
nums1.extend([0] * n)

# Merge and display result
result = merge_arrays(nums1, m, nums2, n)

print("Merged Array:")
print(result)