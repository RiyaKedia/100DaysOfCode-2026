def compress(chars):
    write = 0
    read = 0
    n = len(chars)

    while read < n:
        current = chars[read]
        count = 0

        # Count consecutive occurrences
        while read < n and chars[read] == current:
            read += 1
            count += 1

        # Write the character
        chars[write] = current
        write += 1

        # Write the count if greater than 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


# Driver Code
chars = input("Enter characters separated by space: ").split()

new_length = compress(chars)

print("Compressed Array:", chars[:new_length])
print("New Length:", new_length)