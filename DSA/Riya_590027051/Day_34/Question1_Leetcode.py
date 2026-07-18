class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        return len(self.inStack) == 0 and len(self.outStack) == 0


# Driver Code
queue = MyQueue()

n = int(input("Enter number of operations: "))

print("Operations:")
print("push x")
print("pop")
print("peek")
print("empty")

for _ in range(n):
    operation = input().split()

    if operation[0] == "push":
        queue.push(int(operation[1]))
        print(f"Pushed {operation[1]}")

    elif operation[0] == "pop":
        if queue.empty():
            print("Queue is empty")
        else:
            print("Popped:", queue.pop())

    elif operation[0] == "peek":
        if queue.empty():
            print("Queue is empty")
        else:
            print("Front:", queue.peek())

    elif operation[0] == "empty":
        print(queue.empty())

    else:
        print("Invalid operation")