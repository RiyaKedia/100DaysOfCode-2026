def postfix_to_prefix(postfix):
    stack = []

    for ch in postfix:
        if ch.isalpha():  # Operand
            stack.append(ch)
        else:  # Operator
            op2 = stack.pop()
            op1 = stack.pop()
            expression = ch + op1 + op2
            stack.append(expression)

    return stack[-1]


# Input
s = input().strip()

# Output
print(postfix_to_prefix(s))