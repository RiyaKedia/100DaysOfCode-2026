def insert_at_bottom(stack, x):
    if not stack:
        stack.append(x)
        return

    top = stack.pop()
    insert_at_bottom(stack, x)
    stack.append(top)


# Input
stack = list(map(int, input().split()))
x = int(input())

# Insert element at the bottom
insert_at_bottom(stack, x)

# Output
print(stack)