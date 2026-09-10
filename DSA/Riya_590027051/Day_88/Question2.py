def job_sequencing(deadline, profit):
    # Create jobs as (deadline, profit)
    jobs = []

    for i in range(len(deadline)):
        jobs.append((deadline[i], profit[i]))

    # Sort jobs according to profit in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Find the maximum deadline
    max_deadline = max(deadline)

    # Create slots
    slots = [-1] * (max_deadline + 1)

    total_profit = 0
    job_count = 0

    # Schedule each job
    for d, p in jobs:

        # Find an empty slot before or on the deadline
        for j in range(d, 0, -1):

            if slots[j] == -1:
                slots[j] = p
                total_profit += p
                job_count += 1
                break

    return job_count, total_profit


# Take input from the user
deadline = list(map(int, input("Enter deadlines: ").split()))
profit = list(map(int, input("Enter profits: ").split()))

# Call the function
job_count, total_profit = job_sequencing(deadline, profit)

# Display the result
print("Number of jobs scheduled:", job_count)
print("Maximum profit:", total_profit)