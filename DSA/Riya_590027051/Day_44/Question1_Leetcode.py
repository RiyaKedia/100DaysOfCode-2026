def can_make_arithmetic_progression(arr):
    arr.sort()

    diff = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return False

    return True


# Input
arr = list(map(int, input("Enter array elements: ").split()))

# Output
if can_make_arithmetic_progression(arr):
    print("true")
else:
    print("false")