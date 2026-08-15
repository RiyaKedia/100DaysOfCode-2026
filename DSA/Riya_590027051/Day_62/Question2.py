class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rob(self, root):
        def dfs(node):
            # Empty node
            if node is None:
                return (0, 0)

            # Get results from left and right children
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # If we rob current house,
            # we cannot rob its children
            rob_current = node.val + left_skip + right_skip

            # If we skip current house,
            # we can either rob or skip each child
            skip_current = max(left_rob, left_skip) + \
                           max(right_rob, right_skip)

            return (rob_current, skip_current)

        rob_root, skip_root = dfs(root)

        return max(rob_root, skip_root)


# Build binary tree from level-order array
def build_tree(values):
    if not values:
        return None

    nodes = []

    for value in values:
        if value == -1:
            nodes.append(None)
        else:
            nodes.append(TreeNode(value))

    child_index = 1

    for i in range(len(nodes)):
        if nodes[i] is not None:

            if child_index < len(nodes):
                nodes[i].left = nodes[child_index]
                child_index += 1

            if child_index < len(nodes):
                nodes[i].right = nodes[child_index]
                child_index += 1

    return nodes[0]


# Example
tree = [3, 2, 3, -1, 3, -1, 1]

root = build_tree(tree)

solution = Solution()

answer = solution.rob(root)

print("Maximum amount of money:", answer)