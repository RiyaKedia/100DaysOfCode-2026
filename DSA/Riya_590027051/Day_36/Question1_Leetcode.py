from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            return "Stack is empty"
        return self.q1.popleft()

    def top(self):
        if self.empty():
            return "Stack is empty"
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


# Driver Code
stack = MyStack()

n = int(input("Enter number of operations: "))

print("\nOperations:")
print("push x")
print("pop")
print("top")
print("empty")

for _ in range(n):
    operation = input().split()

    if operation[0] == "push":
        stack.push(int(operation[1]))
        print(f"Pushed {operation[1]}")

    elif operation[0] == "pop":
        print(stack.pop())

    elif operation[0] == "top":
        print(stack.top())

    elif operation[0] == "empty":
        print(stack.empty())

    else:
        print("Invalid operation")