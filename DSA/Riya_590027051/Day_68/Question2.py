class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root):
        self.max_size = 0

        def dfs(node):
            # Empty tree is a valid BST
            if node is None:
                return True, 0, float('inf'), float('-inf')

            # Check left and right subtrees
            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)

            # Check if current subtree is a valid BST
            if (left_is_bst and right_is_bst and
                    left_max < node.val < right_min):

                size = left_size + right_size + 1

                # Update largest BST
                self.max_size = max(self.max_size, size)

                minimum = min(left_min, node.val)
                maximum = max(right_max, node.val)

                return True, size, minimum, maximum

            # Current subtree is not a BST
            return False, 0, 0, 0

        dfs(root)

        return self.max_size


# -----------------------------
# Create the binary tree
# -----------------------------

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(1)
root.left.right = TreeNode(8)

root.right.left = TreeNode(-1)
root.right.right = TreeNode(7)


# -----------------------------
# Solve
# -----------------------------

solution = Solution()

answer = solution.largestBSTSubtree(root)

print("Size of largest BST subtree:", answer)