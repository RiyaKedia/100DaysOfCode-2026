# Can Place Flowers

# Take input from the user
flowerbed = list(map(int, input("Enter flowerbed: ").split()))
n = int(input("Enter number of flowers to plant: "))

# Check if no flowers need to be planted
if n == 0:
    print(True)
else:
    for i in range(len(flowerbed)):

        # Check if current plot is empty
        if flowerbed[i] == 0:

            # Check left side
            left = (i == 0 or flowerbed[i - 1] == 0)

            # Check right side
            right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            # If both sides are empty, plant a flower
            if left and right:
                flowerbed[i] = 1
                n -= 1

                # All flowers have been planted
                if n == 0:
                    break

    # Check whether all flowers were planted
    if n == 0:
        print(True)
    else:
        print(False)