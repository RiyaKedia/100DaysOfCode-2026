def pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


# Input
arr = list(map(int, input("Enter the sorted array elements separated by spaces: ").split()))
target = int(input("Enter the target sum: "))

# Output
print(pair_with_target_sum(arr, target))