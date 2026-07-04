class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to segregate even and odd nodes
def segregateEvenOdd(head):
    if head is None:
        return None

    evenStart = evenEnd = None
    oddStart = oddEnd = None
    current = head

    while current:
        if current.data % 2 == 0:   # Even node
            if evenStart is None:
                evenStart = evenEnd = current
            else:
                evenEnd.next = current
                evenEnd = evenEnd.next
        else:   # Odd node
            if oddStart is None:
                oddStart = oddEnd = current
            else:
                oddEnd.next = current
                oddEnd = oddEnd.next

        current = current.next

    # If no even or no odd nodes
    if evenStart is None:
        return oddStart
    if oddStart is None:
        return evenStart

    # Connect even list with odd list
    evenEnd.next = oddStart
    oddEnd.next = None

    return evenStart


# Create linked list from input
def createLinkedList(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head
    for num in arr[1:]:
        temp.next = Node(num)
        temp = temp.next

    return head


# Print linked list
def printLinkedList(head):
    while head:
        print(head.data, end="")
        if head.next:
            print(" -> ", end="")
        head = head.next
    print()


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))

# Create linked list
head = createLinkedList(arr)

# Segregate even and odd
head = segregateEvenOdd(head)

# Output
print("Modified Linked List:")
printLinkedList(head)