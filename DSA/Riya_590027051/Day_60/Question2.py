class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values or values[0] == -1:
        return None

    nodes = []

    for value in values:
        if value == -1:
            nodes.append(None)
        else:
            nodes.append(TreeNode(value))

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


def count_safe_campsites(root):
    if root is None:
        return 0

    def dfs(node, max_value):
        if node is None:
            return 0

        # Check if the current node is safe
        if node.val >= max_value:
            safe = 1
            new_max = node.val
        else:
            safe = 0
            new_max = max_value

        # Check left and right subtrees
        safe += dfs(node.left, new_max)
        safe += dfs(node.right, new_max)

        return safe

    return dfs(root, root.val)


# Input
n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter tree elements: ").split()))

# Build the binary tree
root = build_tree(values)

# Count safe campsites
answer = count_safe_campsites(root)

# Output
print("Number of safe campsites:", answer)