def hamming_distance(x, y):
    # XOR gives 1 where the bits are different
    xor_result = x ^ y

    # Count the number of set bits (1s)
    return xor_result.bit_count()


# Taking input from the user
x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Calculate and display the Hamming Distance
result = hamming_distance(x, y)

print("Hamming Distance:", result)