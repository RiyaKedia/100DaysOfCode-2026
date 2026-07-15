def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Remove elements smaller than or equal to current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is not empty, top is the next greater element
        if stack:
            result[i] = stack[-1]

        # Push current element onto the stack
        stack.append(arr[i])

    return result


# Driver Code
arr = list(map(int, input("Enter array elements: ").split()))

result = next_greater_element(arr)

print("Next Greater Elements:", *result)