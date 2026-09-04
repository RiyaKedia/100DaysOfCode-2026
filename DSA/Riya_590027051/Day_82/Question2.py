def turn_off_rightmost_set_bit(n):
    return n & (n - 1)


# Take input from user
n = int(input("Enter a positive integer: "))

# Turn off the rightmost set bit
result = turn_off_rightmost_set_bit(n)

# Display result
print("Result:", result)