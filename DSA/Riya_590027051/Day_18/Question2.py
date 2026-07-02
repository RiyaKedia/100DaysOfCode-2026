class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Function to remove nth node from end
def removeNthFromEnd(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove nth node
    slow.next = slow.next.next

    return dummy.next


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
n = int(input("Enter n: "))

# Create list
head = createList(arr)

# Remove nth node from end
head = removeNthFromEnd(head, n)

# Output
print("Updated Linked List:")
printList(head)