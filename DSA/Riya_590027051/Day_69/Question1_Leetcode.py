class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstFromPreorder(preorder):
    index = 0

    def build(bound):
        nonlocal index

        # No more nodes or current value exceeds the allowed bound
        if index == len(preorder) or preorder[index] > bound:
            return None

        # Create the current node
        root = TreeNode(preorder[index])
        index += 1

        # Build left subtree
        root.left = build(root.val)

        # Build right subtree
        root.right = build(bound)

        return root

    return build(float('inf'))


# Print tree in level-order
def printTree(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove unnecessary None values at the end
    while result and result[-1] is None:
        result.pop()

    return result


# Test case 1
preorder = [8, 5, 1, 7, 10, 12]

root = bstFromPreorder(preorder)

print("Input:", preorder)
print("Output:", printTree(root))


# Test case 2
preorder = [1, 3]

root = bstFromPreorder(preorder)

print("Input:", preorder)
print("Output:", printTree(root))