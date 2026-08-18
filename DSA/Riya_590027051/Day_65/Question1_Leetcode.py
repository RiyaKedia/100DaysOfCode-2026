class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_mode(root):
    count = {}

    def dfs(node):
        if node is None:
            return

        count[node.val] = count.get(node.val, 0) + 1

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    max_frequency = max(count.values())

    modes = []

    for value, frequency in count.items():
        if frequency == max_frequency:
            modes.append(value)

    return modes


# Example 1
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

print("Mode:", find_mode(root))


# Example 2
root2 = TreeNode(0)

print("Mode:", find_mode(root2))