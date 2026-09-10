def array_pair_sum(nums):
    # Sort the array
    nums.sort()

    total = 0

    # Add elements at index 0, 2, 4, ...
    for i in range(0, len(nums), 2):
        total += nums[i]

    return total


# Take input from the user
nums = list(map(int, input("Enter the elements: ").split()))

# Find and display the maximum sum
result = array_pair_sum(nums)

print("Maximum sum:", result)