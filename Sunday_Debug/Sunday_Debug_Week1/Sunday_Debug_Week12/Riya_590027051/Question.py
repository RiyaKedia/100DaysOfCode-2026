def setBit(mask, pos):
    return mask | (1 << pos)


def isBitSet(mask, pos):
    return (mask & (1 << pos)) != 0


def clearBit(mask, pos):
    return mask & ~(1 << pos)


def toggleBit(mask, pos):
    return mask ^ (1 << pos)


def countAwakened(mask):
    count = 0

    for i in range(32):
        if (mask & (1 << i)) != 0:
            count += 1

    return count


# Main program
mask = 0

# Set bit at position 0
mask = setBit(mask, 0)
print(1 if isBitSet(mask, 0) else 0)

# Clear bit at position 0
mask = clearBit(mask, 0)
print(1 if isBitSet(mask, 0) else 0)

# Toggle bit at position 1
mask = toggleBit(mask, 1)
print(1 if isBitSet(mask, 1) else 0)

# Clear bit at position 1
mask = clearBit(mask, 1)
print(1 if isBitSet(mask, 1) else 0)

# Set two bits and count them
mask = setBit(mask, 0)
mask = setBit(mask, 1)
print(countAwakened(mask))