class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Build a height-balanced BST
def build_bst(arr, left, right):
    if left > right:
        return None

    # Choose left-middle element
    mid = (left + right) // 2

    root = TreeNode(arr[mid])

    root.left = build_bst(arr, left, mid - 1)
    root.right = build_bst(arr, mid + 1, right)

    return root


# Returns height and updates balance-factor counts
def calculate_balance(root, counts):
    if root is None:
        return 0

    left_height = calculate_balance(root.left, counts)
    right_height = calculate_balance(root.right, counts)

    balance_factor = left_height - right_height

    if balance_factor == -1:
        counts[0] += 1
    elif balance_factor == 0:
        counts[1] += 1
    elif balance_factor == 1:
        counts[2] += 1

    return 1 + max(left_height, right_height)


# Main function
def balance_spectrum(arr):
    if not arr:
        return [0, 0, 0]

    # Build balanced BST
    root = build_bst(arr, 0, len(arr) - 1)

    # counts = [-1, 0, +1]
    counts = [0, 0, 0]

    calculate_balance(root, counts)

    return counts


# -----------------------------
# Test the program
# -----------------------------

arr = [1, 2, 3, 4, 5, 6, 7]

result = balance_spectrum(arr)

print("Array:", arr)
print("Balance Spectrum:", result)