from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Build a binary tree from level-order representation.
    -1 represents a missing node.
    """

    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] != -1:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] != -1:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def are_mirror(root1, root2):
    """
    Check whether two binary trees are mirror images.
    """

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False

    # Left subtree of first must match
    # right subtree of second.
    # Right subtree of first must match
    # left subtree of second.
    return (
        are_mirror(root1.left, root2.right)
        and are_mirror(root1.right, root2.left)
    )


# Example input
warehouse1 = [1, 2, 3]
warehouse2 = [1, 3, 2]

# Build both trees
root1 = build_tree(warehouse1)
root2 = build_tree(warehouse2)

# Check if they are mirrors
if are_mirror(root1, root2):
    print("YES")
else:
    print("NO")