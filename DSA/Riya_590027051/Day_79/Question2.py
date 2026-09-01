def find_single_number(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


# Taking input from user
nums = list(map(int, input("Enter the array elements: ").split()))

# Find the element that appears only once
answer = find_single_number(nums)

print("The element that appears only once is:", answer)