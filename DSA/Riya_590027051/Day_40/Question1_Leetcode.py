from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque()

    def pushFront(self, val):
        self.queue.appendleft(val)

    def pushMiddle(self, val):
        mid = len(self.queue) // 2

        # Convert to list for middle insertion
        temp = list(self.queue)
        temp.insert(mid, val)

        self.queue = deque(temp)

    def pushBack(self, val):
        self.queue.append(val)

    def popFront(self):
        if not self.queue:
            return -1
        return self.queue.popleft()

    def popMiddle(self):
        if not self.queue:
            return -1

        temp = list(self.queue)

        # Frontmost middle element
        mid = (len(temp) - 1) // 2

        value = temp.pop(mid)
        self.queue = deque(temp)

        return value

    def popBack(self):
        if not self.queue:
            return -1
        return self.queue.pop()


# Main program
q = FrontMiddleBackQueue()

q.pushFront(1)
q.pushBack(2)
q.pushMiddle(3)
q.pushMiddle(4)

print(q.popFront())   # 1
print(q.popMiddle())  # 3
print(q.popMiddle())  # 4
print(q.popBack())    # 2
print(q.popFront())   # -1