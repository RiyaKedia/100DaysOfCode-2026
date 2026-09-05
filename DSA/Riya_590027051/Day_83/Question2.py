def count_set_bits(n):
    count = 0

    while n > 0:
        n = n & (n - 1)
        count += 1

    return count


# Input
n = int(input("Enter a non-negative integer: "))

# Output
print("Number of set bits:", count_set_bits(n))