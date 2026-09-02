def hamming_weight(n):
    count = 0

    while n:
        n = n & (n - 1)
        count += 1

    return count


# Input
n = int(input("Enter a positive integer: "))

# Output
print("Number of set bits:", hamming_weight(n))