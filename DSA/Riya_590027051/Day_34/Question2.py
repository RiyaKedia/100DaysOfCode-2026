def visible_left(arr):
    n = len(arr)
    left = [0] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        left[i] = len(stack)

        stack.append(i)

    return left


def visible_right(arr):
    n = len(arr)
    right = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        right[i] = len(stack)

        stack.append(i)

    return right


arr = list(map(int, input("Enter heights: ").split()))

left = visible_left(arr)
right = visible_right(arr)

maximum = 0

for i in range(len(arr)):
    total = left[i] + right[i] + 1   # +1 for the person themselves
    maximum = max(maximum, total)

print("Maximum people visible:", maximum)