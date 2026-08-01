# Assembly via Minimums

t = int(input())

for _ in range(t):
    n = int(input())

    b = list(map(int, input().split()))
    b.sort()

    a = []
    idx = 0

    for i in range(n - 1):
        a.append(b[idx])
        idx += (n - i - 1)

    a.append(1000000000)

    print(*a)