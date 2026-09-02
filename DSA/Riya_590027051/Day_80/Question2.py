def is_power_of_two_or_zero(n):
    # 0 is also considered valid
    if n == 0:
        return True

    # A power of 2 has only one set bit
    return (n & (n - 1)) == 0


# Input
n = int(input("Enter a non-negative integer: "))

# Output
print(is_power_of_two_or_zero(n))