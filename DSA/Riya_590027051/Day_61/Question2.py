def minimum_groups(n, mentor):
    # depth[i] = group/level of student i
    depth = [0] * (n + 1)

    max_depth = 0

    for student in range(1, n + 1):
        current = student
        count = 1

        # Follow the mentor chain
        while mentor[current - 1] != -1:
            current = mentor[current - 1]
            count += 1

        depth[student] = count
        max_depth = max(max_depth, count)

    return max_depth


# Input
n = int(input("Enter number of students: "))

mentor = list(map(int, input("Enter mentor array: ").split()))

# Find minimum number of groups
result = minimum_groups(n, mentor)

print("Minimum number of groups:", result)