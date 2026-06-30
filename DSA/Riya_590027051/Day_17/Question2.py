class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create linked list and cycle
def create_linked_list(arr, pos):
    if not arr:
        return None
    
    head = Node(arr[0])
    temp = head
    nodes = [head]

    for num in arr[1:]:
        new_node = Node(num)
        temp.next = new_node
        temp = new_node
        nodes.append(new_node)

    # Create cycle if pos != -1
    if pos != -1:
        temp.next = nodes[pos]

    return head


# Detect cycle
def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))
pos = int(input("Enter cycle position (-1 for no cycle): "))

# Create linked list
head = create_linked_list(arr, pos)

# Check cycle
if has_cycle(head):
    print("True")
else:
    print("False")