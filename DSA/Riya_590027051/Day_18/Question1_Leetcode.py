class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Function to rotate linked list
def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Reduce k
    k = k % length
    if k == 0:
        return head

    # Make circular
    tail.next = head

    # Find new tail
    steps = length - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next

    # Set new head
    new_head = new_tail.next

    # Break circle
    new_tail.next = None

    return new_head


# Function to create linked list
def createList(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head
    for num in arr[1:]:
        temp.next = Node(num)
        temp = temp.next
    return head


# Function to print linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))
k = int(input("Enter k: "))

# Create list
head = createList(arr)

# Rotate list
head = rotateRight(head, k)

# Output
print("Rotated Linked List:")
printList(head)