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


def diameter_of_binary_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter

        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        # Diameter passing through this node
        diameter = max(diameter, left_height + right_height)

        # Return height of this subtree
        return 1 + max(left_height, right_height)

    height(root)

    return diameter


# Input
values = list(map(int, input("Enter tree elements: ").split()))

# Build tree
root = build_tree(values)

# Find diameter
answer = diameter_of_binary_tree(root)

# Output
print("Diameter of the binary tree:", answer)