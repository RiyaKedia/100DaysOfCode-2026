def remove_outer_parentheses(s):
    result = []
    balance = 0

    for ch in s:
        if ch == '(':
            if balance > 0:
                result.append(ch)
            balance += 1
        else:
            balance -= 1
            if balance > 0:
                result.append(ch)

    return "".join(result)


# Input
s = input().strip()

# Output
print(remove_outer_parentheses(s))