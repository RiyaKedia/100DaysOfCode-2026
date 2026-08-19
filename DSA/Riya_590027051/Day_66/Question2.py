# The Corporate Merger
# Combine two BSTs and return all unique employee IDs in sorted order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Inorder traversal
def inorder(root, result):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)


# Function to combine two BSTs
def get_all_elements(root1, root2):
    list1 = []
    list2 = []

    # Get sorted elements from both BSTs
    inorder(root1, list1)
    inorder(root2, list2)

    # Merge the two sorted lists
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            value = list1[i]
            i += 1

        elif list1[i] > list2[j]:
            value = list2[j]
            j += 1

        else:
            # Same value exists in both trees
            value = list1[i]
            i += 1
            j += 1

        # Add only unique values
        if not result or result[-1] != value:
            result.append(value)

    # Add remaining elements from list1
    while i < len(list1):
        value = list1[i]

        if not result or result[-1] != value:
            result.append(value)

        i += 1

    # Add remaining elements from list2
    while j < len(list2):
        value = list2[j]

        if not result or result[-1] != value:
            result.append(value)

        j += 1

    return result


# -----------------------------
# Create Tree 1
# -----------------------------

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)


# -----------------------------
# Create Tree 2
# -----------------------------

root2 = TreeNode(4)
root2.right = TreeNode(5)


# Get combined sorted unique elements
answer = get_all_elements(root1, root2)

print("Sorted unique employee IDs:")
print(answer)