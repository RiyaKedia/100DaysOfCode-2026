from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        # Add the new request
        self.requests.append(t)

        # Remove requests outside the range [t - 3000, t]
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of recent requests
        return len(self.requests)


# Main program
recent_counter = RecentCounter()

n = int(input("Enter number of requests: "))

for i in range(n):
    t = int(input("Enter request time: "))
    print("Recent requests:", recent_counter.ping(t))