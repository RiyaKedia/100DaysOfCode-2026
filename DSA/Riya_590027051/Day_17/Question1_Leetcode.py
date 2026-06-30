class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    temp = head
    for num in arr[1:]:
        temp.next = Node(num)
        temp = temp.next
    return head


# Check if linked list is palindrome
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Step 3: Compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))

# Create linked list
head = create_linked_list(arr)

# Check palindrome
if is_palindrome(head):
    print("True")
else:
    print("False")