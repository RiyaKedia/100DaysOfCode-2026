def max_subsequence(nums, k):
    # Store value and its original index
    arr = [(value, index) for index, value in enumerate(nums)]

    # Sort by value in descending order
    arr.sort(reverse=True)

    # Select the k largest elements
    selected = arr[:k]

    # Sort selected elements by their original index
    selected.sort(key=lambda x: x[1])

    # Return only the values
    return [value for value, index in selected]


# Input
nums = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter k: "))

# Find and print the answer
answer = max_subsequence(nums, k)

print("Maximum sum subsequence:", answer)