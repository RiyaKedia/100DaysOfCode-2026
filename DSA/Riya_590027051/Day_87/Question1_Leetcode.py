def lemonade_change(bills):
    five = 0
    ten = 0

    for bill in bills:

        if bill == 5:
            five += 1

        elif bill == 10:
            if five == 0:
                return False

            five -= 1
            ten += 1

        elif bill == 20:
            # Prefer giving $10 + $5
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1

            # Otherwise give three $5 bills
            elif five >= 3:
                five -= 3

            else:
                return False

    return True


# Taking input
bills = list(map(int, input("Enter bills separated by spaces: ").split()))

# Calling function
result = lemonade_change(bills)

# Displaying output
print("Output:", result)