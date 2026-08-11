class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Build binary tree from level-order input
def build_tree(values):
    if not values or values[0] == -1:
        return None

    nodes = []

    for value in values:
        if value == -1:
            nodes.append(None)
        else:
            nodes.append(Node(value))

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]

            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]

    return nodes[0]


# Find Lowest Common Ancestor
def lowest_common_ancestor(root, a, b):

    if root is None:
        return None

    # If current node is a or b
    if root.value == a or root.value == b:
        return root

    # Search in left subtree
    left = lowest_common_ancestor(root.left, a, b)

    # Search in right subtree
    right = lowest_common_ancestor(root.right, a, b)

    # a and b are on different sides
    if left is not None and right is not None:
        return root

    # Return whichever side contains a or b
    if left is not None:
        return left

    return right


# Check whether a value exists in the tree
def exists(root, value):

    if root is None:
        return False

    if root.value == value:
        return True

    return exists(root.left, value) or exists(root.right, value)


# Input tree
values = list(map(int, input("Enter tree values: ").split()))

# Input employee IDs
a, b = map(int, input("Enter two employee IDs: ").split())

# Build tree
root = build_tree(values)

# Check if both employees exist
if not exists(root, a) or not exists(root, b):
    print(-1)
else:
    # Find LCA
    lca = lowest_common_ancestor(root, a, b)

    if lca is not None:
        print(lca.value)
    else:
        print(-1)