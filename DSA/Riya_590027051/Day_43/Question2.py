def maximize_pair_minimum_sum(nums):
    # Sort the array
    nums.sort()

    # Sum every alternate element (minimum of each pair)
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]

    return total


# Input
nums = list(map(int, input("Enter the integers: ").split()))

# Check if the number of integers is even
if len(nums) % 2 != 0:
    print("Error: Please enter an even number of integers.")
else:
    result = maximize_pair_minimum_sum(nums)
    print("Maximum Sum of Pair Minimums:", result)