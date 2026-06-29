class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Function to swap nodes in pairs
def swapPairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        # Swap
        first.next = second.next
        second.next = first
        prev.next = second

        # Move to next pair
        prev = first

    return dummy.next


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
        print(head.val, end=" ")
        head = head.next
    print()


# Main
arr = list(map(int, input("Enter elements: ").split()))

head = createLinkedList(arr)

print("Original Linked List:")
printLinkedList(head)

head = swapPairs(head)

print("After Swapping Pairs:")
printLinkedList(head)