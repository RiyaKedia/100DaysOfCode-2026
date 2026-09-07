def maximum_activities(start, end):
    # Create pairs of (start time, end time)
    activities = list(zip(start, end))

    # Sort activities by their end time
    activities.sort(key=lambda x: x[1])

    count = 0
    last_end = -1

    # Select activities greedily
    for start_time, end_time in activities:
        if start_time >= last_end:
            count += 1
            last_end = end_time

    return count


# Input
n = int(input("Enter number of activities: "))

start = list(map(int, input("Enter start times: ").split()))
end = list(map(int, input("Enter end times: ").split()))

# Find maximum number of activities
result = maximum_activities(start, end)

print("Maximum number of non-overlapping activities:", result)