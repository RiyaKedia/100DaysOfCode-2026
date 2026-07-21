from collections import deque

def printer_queue(priorities, location):
    # Store (priority, original index)
    queue = deque((priority, index) for index, priority in enumerate(priorities))

    printed_count = 0

    while queue:
        priority, index = queue.popleft()

        # Check if any document has higher priority
        if any(p > priority for p, _ in queue):
            # Move the document to the back
            queue.append((priority, index))
        else:
            # Print the document
            printed_count += 1

            # Check if this is the target document
            if index == location:
                return printed_count

# Input
priorities = list(map(int, input("Enter priorities: ").split()))
location = int(input("Enter location: "))

# Output
result = printer_queue(priorities, location)
print("Minutes taken:", result)