def copy_stack(st):
    temp = []
    copied = []

    # Move elements to temporary stack
    while st:
        temp.append(st.pop())

    # Restore original stack and build copied stack
    while temp:
        x = temp.pop()
        st.append(x)
        copied.append(x)

    return copied


# Input
st = list(map(int, input().split()))

# Copy stack
copied_stack = copy_stack(st)

# Output
print(copied_stack)