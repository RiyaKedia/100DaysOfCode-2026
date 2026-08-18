class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(root, target):
    closest = root.val

    while root:
        # Check if current value is closer
        if abs(root.val - target) < abs(closest - target):
            closest = root.val

        # If equally close, choose the smaller value
        elif abs(root.val - target) == abs(closest - target):
            closest = min(closest, root.val)

        # Use BST property to decide where to go
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            # Exact match
            return root.val

    return closest


# Example
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

target = 3

print("Closest temperature:", closest_value(root, target))