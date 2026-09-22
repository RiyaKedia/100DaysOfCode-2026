# Days Until a Warmer Temperature

# Taking input
temperatures = list(map(int, input("Enter the temperatures: ").split()))

# Result array
answer = [0] * len(temperatures)

# Stack stores indexes of temperatures
stack = []

# Traverse through all temperatures
for i in range(len(temperatures)):

    # While current temperature is warmer
    # than the temperature at the top of stack
    while stack and temperatures[i] > temperatures[stack[-1]]:

        previous_day = stack.pop()

        # Number of days between the two temperatures
        answer[previous_day] = i - previous_day

    # Store current day's index
    stack.append(i)

# Print the result
print("Days until a warmer temperature:", *answer)