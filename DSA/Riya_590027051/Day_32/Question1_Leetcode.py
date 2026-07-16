def min_length(s):
    stack = []

    for ch in s:
        stack.append(ch)

        if len(stack) >= 2:
            if (stack[-2] == 'A' and stack[-1] == 'B') or \
               (stack[-2] == 'C' and stack[-1] == 'D'):
                stack.pop()
                stack.pop()

    return len(stack)


# Input
s = input().strip()

# Output
print(min_length(s))