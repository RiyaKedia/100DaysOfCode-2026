class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# Function to reverse linked list
def reverseList(head):
    prev = None
    current = head

    while current:
        next_node = current.next   # Save next node
        current.next = prev        # Reverse link
        prev = current             # Move prev forward
        current = next_node        # Move current forward

    return prev


# Function to create linked list from array
def createList(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head


# Function to print linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))

head = createList(arr)

# Reverse the list
reversed_head = reverseList(head)

print("Reversed List:")
printList(reversed_head)