def sorted_squares(nums):
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1

        pos -= 1

    return result


# Input
nums = list(map(int, input().split()))

# Output
print(sorted_squares(nums))