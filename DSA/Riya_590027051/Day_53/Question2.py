from collections import Counter

def find_anagrams(log, pattern):
    result = []

    if len(pattern) > len(log):
        return result

    pattern_count = Counter(pattern)
    window_count = Counter(log[:len(pattern)])

    if window_count == pattern_count:
        result.append(0)

    for i in range(len(pattern), len(log)):
        # Add new character to the window
        window_count[log[i]] += 1

        # Remove the leftmost character from the window
        left_char = log[i - len(pattern)]
        window_count[left_char] -= 1

        # Remove the key if its count becomes 0
        if window_count[left_char] == 0:
            del window_count[left_char]

        # Compare frequency maps
        if window_count == pattern_count:
            result.append(i - len(pattern) + 1)

    return result


# Input
log = input("Enter the log string: ")
pattern = input("Enter the pattern: ")

# Output
print("Starting indices:", find_anagrams(log, pattern))