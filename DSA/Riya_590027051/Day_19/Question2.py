class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Function to find middle node
def findMiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


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


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))

# Create linked list
head = createLinkedList(arr)

# Find middle
middle = findMiddle(head)

# Output
print("Middle node is:", middle.val)