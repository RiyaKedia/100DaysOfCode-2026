class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, a, b):
    current = root

    while current:
        # Both values are smaller than current
        if a < current.val and b < current.val:
            current = current.left

        # Both values are greater than current
        elif a > current.val and b > current.val:
            current = current.right

        # They are on different sides, or one is the current node
        else:
            return current.val

    return None


# Creating the Binary Search Tree
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9

root = TreeNode(6)

root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


# Given room numbers
a = 2
b = 8

# Find Lowest Common Ancestor
result = lowest_common_ancestor(root, a, b)

print("Lowest Common Ancestor:", result)