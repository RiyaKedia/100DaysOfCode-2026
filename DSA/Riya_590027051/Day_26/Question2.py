def triplet_sum_check(arr):
    n = len(arr)

    # Sort the array
    arr.sort()

    # Check if any two numbers sum to a third number
    for i in range(n - 1, -1, -1):
        left = 0
        right = i - 1

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == arr[i]:
                return True
            elif current_sum < arr[i]:
                left += 1
            else:
                right -= 1

    return False


# Input
arr = list(map(int, input("Enter array elements: ").split()))

# Output
print(triplet_sum_check(arr))