def move_zeroes(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

# Input
n = int(input())
nums = list(map(int, input().split()))

# Move zeroes
move_zeroes(nums)

# Output
print(*nums)