# Read number of username requests
n = int(input())

# Store existing usernames
registered = {}

# Store results
result = []

for _ in range(n):
    username = input().strip()

    if username not in registered:
        registered[username] = 1
        result.append("OK")
    else:
        new_username = username + str(registered[username])

        while new_username in registered:
            registered[username] += 1
            new_username = username + str(registered[username])

        result.append(new_username)
        registered[new_username] = 1
        registered[username] += 1

# Print results
for ans in result:
    print(ans)