from collections import Counter

# Input
s = input().strip()

# Count character frequencies
freq = Counter(s)

# Check if all frequencies are equal
if len(set(freq.values())) == 1:
    print("true")
else:
    print("false")