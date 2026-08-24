import math

def encryption(s):
    # Remove spaces
    s = s.replace(" ", "")

    # Length of string
    length = len(s)

    # Find rows and columns
    root = math.sqrt(length)

    rows = math.floor(root)
    columns = math.ceil(root)

    # Make sure the grid can contain all characters
    if rows * columns < length:
        rows += 1

    result = []

    # Read column by column
    for col in range(columns):
        word = ""

        for row in range(rows):
            index = row * columns + col

            if index < length:
                word += s[index]

        result.append(word)

    return " ".join(result)


# Input
s = input("Enter the string: ")

# Output
print("Encrypted string:", encryption(s))