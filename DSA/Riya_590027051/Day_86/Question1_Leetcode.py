from collections import Counter

def longest_palindrome(s):
    count = Counter(s)

    length = 0
    has_odd = False

    for freq in count.values():
        # Use the largest even part of the frequency
        length += (freq // 2) * 2

        # We can use one odd-frequency character in the center
        if freq % 2 == 1:
            has_odd = True

    if has_odd:
        length += 1

    return length


# Take input from user
s = input("Enter a string: ")

# Display result
print("Length of longest palindrome:", longest_palindrome(s))