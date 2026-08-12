# Secret Passcodes

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Build binary tree from heap-array format
def build_tree(arr):
    if not arr or arr[0] == -1:
        return None

    nodes = []

    # Create nodes
    for value in arr:
        if value == -1:
            nodes.append(None)
        else:
            nodes.append(TreeNode(value))

    # Connect nodes
    for i in range(len(arr)):
        if nodes[i] is not None:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(arr):
                nodes[i].left = nodes[left]

            if right < len(arr):
                nodes[i].right = nodes[right]

    return nodes[0]


# Check if the path can be rearranged into a palindrome
def can_form_palindrome(mask):
    # A number with at most one bit set
    # means at most one digit has an odd frequency
    return mask == 0 or (mask & (mask - 1)) == 0


# DFS function
def count_paths(node, mask):
    if node is None:
        return 0

    # Toggle the bit corresponding to this digit
    mask ^= (1 << node.val)

    # If this is a leaf node
    if node.left is None and node.right is None:
        if can_form_palindrome(mask):
            return 1
        return 0

    # Continue to left and right
    return count_paths(node.left, mask) + count_paths(node.right, mask)


# Input
tree = list(map(int, input("Enter tree in heap-array format: ").split()))

root = build_tree(tree)

answer = count_paths(root, 0)

print("Number of valid paths:", answer)