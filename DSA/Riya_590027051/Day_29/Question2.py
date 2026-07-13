def reverse_string(s):
    stack = []

    # Push all characters onto the stack
    for ch in s:
        stack.append(ch)

    # Pop characters to form the reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str


# Input
s = input().strip()

# Output
print(reverse_string(s))