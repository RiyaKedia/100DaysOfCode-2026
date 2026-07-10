def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Input
nums = list(map(int, input("Enter the array elements (0, 1, 2) separated by spaces: ").split()))

# Sort the array
sort_colors(nums)

# Output
print("Sorted array:", nums)