def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    total = len(left_part) + len(right_part)

    for _ in range(total):
        if i < len(left_part) and (j >= len(right_part) or left_part[i] <= right_part[j]):
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


# Driver Code
incidents = [34, 7, 23, 32, 5, 62, 15]

merge_sort(incidents, 0, len(incidents) - 1)
print("Sorted Reports:", incidents)

index = binary_search(incidents, 23)
print("Record Found At:", index)