class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Function to remove duplicates from sorted linked list
def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


# Function to create linked list
def createLinkedList(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for num in arr[1:]:
        temp.next = Node(num)
        temp = temp.next

    return head


# Function to print linked list
def printLinkedList(head):
    temp = head
    result = []

    while temp:
        result.append(str(temp.val))
        temp = temp.next

    print(" -> ".join(result))


# Input
arr = list(map(int, input("Enter sorted linked list elements: ").split()))

# Create linked list
head = createLinkedList(arr)

# Remove duplicates
head = deleteDuplicates(head)

# Output
print("Linked list after removing duplicates:")
printLinkedList(head)