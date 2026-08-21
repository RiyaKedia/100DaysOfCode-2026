class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root):
        # Step 1: Inorder traversal
        # This gives the BST values in sorted order
        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Build a balanced BST
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(values[mid])

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(values) - 1)


# Function to print inorder traversal
def print_inorder(root):
    if root is None:
        return

    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)


# Creating an unbalanced BST
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

# Balance the BST
solution = Solution()
balanced_root = solution.balanceBST(root)

# Print the balanced BST in inorder
print("Inorder traversal of balanced BST:")
print_inorder(balanced_root)