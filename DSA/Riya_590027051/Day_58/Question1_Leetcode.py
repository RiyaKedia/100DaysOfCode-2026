class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(values):
    if not values:
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


def count_nodes(root):
    if root is None:
        return 0

    # Find height from the left side
    def left_height(node):
        height = 0

        while node:
            height += 1
            node = node.left

        return height

    # Find height from the right side
    def right_height(node):
        height = 0

        while node:
            height += 1
            node = node.right

        return height

    left = left_height(root)
    right = right_height(root)

    # If both heights are equal,
    # the tree is a complete full tree
    if left == right:
        return (2 ** left) - 1

    # Otherwise, count recursively
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Take input
values = list(map(int, input("Enter tree values: ").split()))

# Build tree
root = build_tree(values)

# Count nodes
answer = count_nodes(root)

print("Number of nodes:", answer)