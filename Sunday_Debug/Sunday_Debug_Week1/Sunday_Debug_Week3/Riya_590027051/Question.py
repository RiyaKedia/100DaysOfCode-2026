class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    # Find middle node (returns second middle if even)
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Detect and remove loop
    def detect_and_remove_loop(self):
        slow = self.head
        fast = self.head

        # Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return False

        # Remove loop
        slow = self.head

        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
            return True

        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = None
        return True


# ---------------- Main ----------------

ll = LinkedList()

# Insert heroes (IDs)
for value in [1, 2, 3, 4, 5]:
    ll.insert(value)

# Create a loop for testing
tail = ll.head
while tail.next:
    tail = tail.next

tail.next = ll.head.next  # 5 -> 2 (creates loop)

# Detect and fix loop
ll.detect_and_remove_loop()

# Print full roster
ll.print_list()

# Delete hero 3
ll.delete(3)

# Print updated roster
ll.print_list()

# Find backup leader (middle)
middle = ll.find_middle()
if middle:
    print("Backup Leader:", middle.data)