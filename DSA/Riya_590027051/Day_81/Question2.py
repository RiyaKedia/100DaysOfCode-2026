def single_number(nums):
    ones = 0
    twos = 0

    for num in nums:
        # Bits that appear for the first time
        ones = (ones ^ num) & ~twos

        # Bits that appear for the second time
        twos = (twos ^ num) & ~ones

    return ones


# Taking input from the user
nums = list(map(int, input("Enter the numbers: ").split()))

# Find the unique number
result = single_number(nums)

print("The number appearing exactly once is:", result)