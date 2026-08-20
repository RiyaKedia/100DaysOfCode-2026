class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Insert a node into BST
def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Find the smallest node in a subtree
def find_min(root):
    while root.left is not None:
        root = root.left
    return root


# Delete a node from BST
def delete_node(root, key):
    # Key not found
    if root is None:
        return None

    # Search in left subtree
    if key < root.val:
        root.left = delete_node(root.left, key)

    # Search in right subtree
    elif key > root.val:
        root.right = delete_node(root.right, key)

    # Node found
    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: Only right child
        if root.left is None:
            return root.right

        # Case 3: Only left child
        if root.right is None:
            return root.left

        # Case 4: Two children
        successor = find_min(root.right)

        root.val = successor.val

        root.right = delete_node(root.right, successor.val)

    return root


# Inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# Main program
root = None

values = [5, 3, 6, 2, 4, 7]

for value in values:
    root = insert(root, value)

print("BST before deletion:")
inorder(root)

key = 3

root = delete_node(root, key)

print("\nBST after deleting", key, ":")
inorder(root)