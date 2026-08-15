from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Leaf node
        if root.left is None and root.right is None:
            return root.val == 1

        # Evaluate left and right subtrees
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        # 2 = OR
        if root.val == 2:
            return left or right

        # 3 = AND
        return left and right


# Create tree from level-order array
def build_tree(values):
    if not values:
        return None

    nodes = [
        TreeNode(value) if value is not None else None
        for value in values
    ]

    j = 1

    for i in range(len(nodes)):
        if nodes[i] is not None:
            if j < len(nodes):
                nodes[i].left = nodes[j]
                j += 1

            if j < len(nodes):
                nodes[i].right = nodes[j]
                j += 1

    return nodes[0]


# Example 1
values = [2, 1, 3, None, None, 0, 1]

root = build_tree(values)

solution = Solution()
answer = solution.evaluateTree(root)

print("Result:", answer)