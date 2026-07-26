class CircularQueue:
    def __init__(self, size):
        self.SIZE = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Add a review to the queue
    def enqueue(self, review_id):
        # Queue is full
        if (self.rear + 1) % self.SIZE == self.front:
            print("Queue Overflow")
            return

        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.SIZE

        self.queue[self.rear] = review_id

    # Process/remove the oldest review
    def dequeue(self):
        # Queue is empty
        if self.front == -1:
            print("Queue Underflow")
            return None

        review_id = self.queue[self.front]

        # Only one element was present
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.SIZE

        return review_id

    # Display all pending reviews
    def display(self):
        if self.front == -1:
            print("Pending Reviews: Queue is Empty")
            return

        print("Pending Reviews:", end=" ")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.SIZE

        print()


# Driver Code
SIZE = 5
drs_queue = CircularQueue(SIZE)

drs_queue.enqueue(101)
drs_queue.enqueue(102)
drs_queue.enqueue(103)
drs_queue.enqueue(104)
drs_queue.enqueue(105)

processed = drs_queue.dequeue()
print("Processed Review:", processed)

drs_queue.display()