class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root, low, high):
    if root is None:
        return 0

    # If current node is smaller than low,
    # we only need to search the right subtree.
    if root.val < low:
        return range_sum_bst(root.right, low, high)

    # If current node is greater than high,
    # we only need to search the left subtree.
    if root.val > high:
        return range_sum_bst(root.left, low, high)

    # Current value is within the range.
    return (
        root.val
        + range_sum_bst(root.left, low, high)
        + range_sum_bst(root.right, low, high)
    )


# Example 1
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

low = 7
high = 15

result = range_sum_bst(root, low, high)

print("Range Sum:", result)