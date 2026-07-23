# Time Needed to Buy Tickets

tickets = list(map(int, input("Enter ticket requirements: ").split()))
k = int(input("Enter the position k: "))

time = 0
target = tickets[k]

for i in range(len(tickets)):
    if i <= k:
        time += min(tickets[i], target)
    else:
        time += min(tickets[i], target - 1)

print("Time taken:", time)