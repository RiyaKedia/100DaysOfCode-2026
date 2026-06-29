class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create Doubly Linked List
def createDLL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for num in arr[1:]:
        newNode = Node(num)
        temp.next = newNode
        newNode.prev = temp
        temp = newNode

    return head


# Delete last node
def deleteLast(head):
    if head is None:
        return None

    # If only one node exists
    if head.next is None:
        return None

    temp = head

    # Traverse to last node
    while temp.next:
        temp = temp.next

    # Remove last node
    temp.prev.next = None

    return head


# Print Doubly Linked List
def printDLL(head):
    if head is None:
        print("NULL")
        return

    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Main
arr = list(map(int, input("Enter elements: ").split()))

head = createDLL(arr)

print("Original Doubly Linked List:")
printDLL(head)

head = deleteLast(head)

print("After Deleting Last Node:")
printDLL(head)