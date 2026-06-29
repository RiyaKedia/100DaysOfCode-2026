class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# Function to merge two sorted linked lists
def mergeTwoLists(list1, list2):
    dummy = ListNode()   # Temporary node
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Add remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# Function to create linked list from array
def createList(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# Function to print linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# Input
arr1 = list(map(int, input("Enter first sorted list: ").split()))
arr2 = list(map(int, input("Enter second sorted list: ").split()))

list1 = createList(arr1)
list2 = createList(arr2)

# Merge and print result
merged = mergeTwoLists(list1, list2)

print("Merged List:")
printList(merged)