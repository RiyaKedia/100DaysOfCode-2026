def triangle_number(nums):
    nums.sort()
    count = 0
    n = len(nums)

    for k in range(n - 1, 1, -1):
        left = 0
        right = k - 1

        while left < right:
            if nums[left] + nums[right] > nums[k]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count


# Input from user
nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Output
print("Number of valid triangles:", triangle_number(nums))