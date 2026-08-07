def max_frequency_elements(nums):
    frequency = {}

    # Count the frequency of each element
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Find the maximum frequency
    max_freq = max(frequency.values())

    # Calculate total frequencies of elements
    # having the maximum frequency
    total = 0
    for freq in frequency.values():
        if freq == max_freq:
            total += freq

    return total


# Input
nums = list(map(int, input("Enter the elements: ").split()))

# Output
print("Output:", max_frequency_elements(nums))