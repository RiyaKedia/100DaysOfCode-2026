def favorite_number(nums, favorite_index, k):
    # Favorite element (1-based index)
    favorite = nums[favorite_index - 1]

    greater = 0
    equal = 0

    for num in nums:
        if num > favorite:
            greater += 1
        elif num == favorite:
            equal += 1

    if greater >= k:
        return "NO"
    elif greater + equal <= k:
        return "YES"
    else:
        return "MAYBE"


# Input
nums = list(map(int, input("Enter array elements: ").split()))
favorite_index = int(input("Enter favorite index (1-based): "))
k = int(input("Enter k: "))

# Output
print(favorite_number(nums, favorite_index, k))