class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0

        total = 0

        # Check if the left child is a leaf
        if root.left:
            if root.left.left is None and root.left.right is None:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        # Check the right subtree
        if root.right:
            total += self.sumOfLeftLeaves(root.right)

        return total


# Creating the binary tree:
#
#         3
#        / \
#       9   20
#          /  \
#         15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the sum of left leaves
solution = Solution()
result = solution.sumOfLeftLeaves(root)

print("Sum of left leaves:", result)