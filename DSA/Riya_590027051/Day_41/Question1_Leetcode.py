class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k
        self.capacity = k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return True

    def Front(self):
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1

        last_index = (self.rear - 1 + self.capacity) % self.capacity
        return self.queue[last_index]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


# Driver Code
if __name__ == "__main__":

    circularQueue = MyCircularQueue(3)

    print(circularQueue.enQueue(1))  # True
    print(circularQueue.enQueue(2))  # True
    print(circularQueue.enQueue(3))  # True
    print(circularQueue.enQueue(4))  # False

    print(circularQueue.Rear())      # 3
    print(circularQueue.isFull())    # True

    print(circularQueue.deQueue())   # True
    print(circularQueue.enQueue(4))  # True

    print(circularQueue.Rear())      # 4