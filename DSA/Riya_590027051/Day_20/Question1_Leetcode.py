class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# Function to remove elements
def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


# Function to create linked list from list
def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    temp = head
    for num in arr[1:]:
        temp.next = ListNode(num)
        temp = temp.next

    return head


# Function to print linked list
def printLinkedList(head):
    if not head:
        print("[]")
        return

    result = []
    while head:
        result.append(head.val)
        head = head.next

    print(result)


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))
val = int(input("Enter value to remove: "))

# Create linked list
head = createLinkedList(arr)

# Remove elements
head = removeElements(head, val)

# Print result
print("Updated Linked List:")
printLinkedList(head)