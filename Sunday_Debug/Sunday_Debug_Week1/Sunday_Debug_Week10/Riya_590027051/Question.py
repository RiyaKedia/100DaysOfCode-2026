class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Recursive insertion
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)

        elif value > root.value:
            root.right = self.insert(root.right, value)

        # If value == root.value, do nothing
        # This prevents duplicate nodes

        return root

    # Recursive search
    def search(self, root, value):
        if root is None:
            return False

        if value == root.value:
            return True

        if value < root.value:
            return self.search(root.left, value)

        return self.search(root.right, value)


# Create BST
tree = BST()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.root = tree.insert(tree.root, value)

# Search
print(tree.search(tree.root, 40))
print(tree.search(tree.root, 90))