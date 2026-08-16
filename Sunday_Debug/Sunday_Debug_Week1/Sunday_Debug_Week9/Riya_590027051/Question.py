# Week 9 — The Tree of Souls

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Build the binary tree
root = TreeNode("Tree")
root.left = TreeNode("Clan")
root.right = TreeNode("Eywa")

root.left.left = TreeNode("Forest")
root.left.right = TreeNode("Mountains")

root.right.left = TreeNode("Spirit")
root.right.right = TreeNode("Ocean")

root.right.right.right = TreeNode("Tulkun")


# Recursive inorder traversal: Left -> Root -> Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


# Recursive height calculation
def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


# Main
print("Neural Connections:")
inorder(root)

print()
print("Height:", height(root))