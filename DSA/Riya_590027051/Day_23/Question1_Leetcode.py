g = list(map(int, input("Enter greed factors: ").split()))
s = list(map(int, input("Enter cookie sizes: ").split()))

g.sort()
s.sort()

i = 0  # Child index
j = 0  # Cookie index

while i < len(g) and j < len(s):
    if s[j] >= g[i]:
        i += 1
    j += 1

print(i)