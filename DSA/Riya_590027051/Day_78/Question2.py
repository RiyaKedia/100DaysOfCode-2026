def maximum_xor_pair(nums):
    max_xor = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            current_xor = nums[i] ^ nums[j]
            max_xor = max(max_xor, current_xor)

    return max_xor


# Input
nums = list(map(int, input("Enter the array elements: ").split()))

# Find maximum XOR
answer = maximum_xor_pair(nums)

# Output
print("Maximum XOR pair value:", answer)