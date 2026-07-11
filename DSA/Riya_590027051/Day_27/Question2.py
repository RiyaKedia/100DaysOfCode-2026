def count_subarrays(arr, limit):
    count = 0
    length = 0

    for num in arr:
        if num <= limit:
            length += 1
        else:
            length = 0

        count += length

    return count


def bounded_max_subarrays(arr, l, r):
    return count_subarrays(arr, r) - count_subarrays(arr, l - 1)


# Driver Code
arr = list(map(int, input("Enter array elements: ").split()))
l = int(input("Enter l: "))
r = int(input("Enter r: "))

result = bounded_max_subarrays(arr, l, r)

print("Number of subarrays:", result)