# Insert a value into a Binary Search Tree (BST)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root, val):
    # If tree is empty, create a new node
    if root is None:
        return TreeNode(val)

    # If value is smaller, insert into left subtree
    if val < root.val:
        root.left = insert_into_bst(root.left, val)

    # If value is larger, insert into right subtree
    else:
        root.right = insert_into_bst(root.right, val)

    return root


# Inorder traversal to display the BST
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# Create the BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Value to insert
val = 5

print("BST before insertion:")
inorder(root)

# Insert the value
root = insert_into_bst(root, val)

print("\nBST after insertion:")
inorder(root)