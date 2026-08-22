class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, val):
    """Insert a value into the BST."""
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def splitBST(root, k):
    """Split BST into values < k and values >= k."""

    if root is None:
        return None, None

    if root.val < k:
        # Root belongs to the first tree
        left_tree, right_tree = splitBST(root.right, k)

        root.right = left_tree

        return root, right_tree

    else:
        # Root belongs to the second tree
        left_tree, right_tree = splitBST(root.left, k)

        root.left = right_tree

        return left_tree, root


def preorder(root):
    """Return preorder traversal as a list."""
    if root is None:
        return []

    return [root.val] + preorder(root.left) + preorder(root.right)


def format_tree(root):
    """Return preorder traversal as a space-separated string."""
    values = preorder(root)

    if not values:
        return "EMPTY"

    return " ".join(map(str, values))


# -----------------------------
# Main Program
# -----------------------------

tree = [10, 5, 15, 2, 7, 12, 20]
k = 10

# Build the BST
root = None

for value in tree:
    root = insert(root, value)

# Split the BST
tree1, tree2 = splitBST(root, k)

# Get preorder traversals
result1 = format_tree(tree1)
result2 = format_tree(tree2)

# Print result
print('["' + result1 + '", "' + result2 + '"]')