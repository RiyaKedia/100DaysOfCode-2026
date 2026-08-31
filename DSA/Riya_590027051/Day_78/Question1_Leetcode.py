def single_number(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


# Input
nums = list(map(int, input("Enter the array elements: ").split()))

# Find the single number
answer = single_number(nums)

# Output
print("The single number is:", answer)