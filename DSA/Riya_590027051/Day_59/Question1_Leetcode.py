from collections import deque


# Create a node of the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to check if tree is complete
def isCompleteTree(root):
    queue = deque([root])
    found_none = False

    while queue:
        node = queue.popleft()

        if node is None:
            found_none = True

        else:
            # If we already found None,
            # but now find a real node
            if found_none:
                return False

            queue.append(node.left)
            queue.append(node.right)

    return True


# Build tree from level-order input
def buildTree(values):
    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if values[i] != -1:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        # Right child
        if i < len(values) and values[i] != -1:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root


# Input
values = list(map(int, input("Enter tree in level order: ").split()))

root = buildTree(values)

# Check complete binary tree
if isCompleteTree(root):
    print("True")
else:
    print("False")