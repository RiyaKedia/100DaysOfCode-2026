def number_of_steps(num):
    steps = 0

    while num > 0:
        if num & 1:          # Check if number is odd
            num -= 1
        else:                # Number is even
            num >>= 1        # Divide by 2
        steps += 1

    return steps


# Take input from user
num = int(input("Enter a number: "))

# Call the function
result = number_of_steps(num)

# Display result
print("Number of steps:", result)