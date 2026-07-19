# Week 5 — Among Us - The Imposter Variable
# VS Code Python Solution

class Stack:
    def __init__(self, size):
        self.SIZE = size
        self.stack = [0] * size
        self.top = -1

    # Push element
    def push(self, value):
        if self.top == self.SIZE - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    # Pop element
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None

        value = self.stack[self.top]
        self.top -= 1
        return value

    # Swap top two elements
    def swapTop(self):
        if self.top < 1:
            print("Not enough elements to swap")
            return

        self.stack[self.top], self.stack[self.top - 1] = (
            self.stack[self.top - 1],
            self.stack[self.top],
        )

    # Display stack from top to bottom
    def display(self):
        if self.top == -1:
            print("Stack is empty")
            return

        print("Remaining:", end=" ")
        for i in range(self.top, -1, -1):
            print(self.stack[i], end=" ")
        print()


# Driver Code
if __name__ == "__main__":
    s = Stack(10)

    s.push(101)
    s.push(102)
    s.push(103)
    s.push(104)

    s.swapTop()

    popped = s.pop()
    print("Popped:", popped)

    s.display()