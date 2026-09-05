def single_number(nums):
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones


# Input
nums = list(map(int, input("Enter the elements: ").split()))

# Output
print("The single number is:", single_number(nums))