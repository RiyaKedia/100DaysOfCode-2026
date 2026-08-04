from collections import Counter

def most_frequent_even(nums):
    count = Counter()

    for num in nums:
        if num % 2 == 0:
            count[num] += 1

    if not count:
        return -1

    max_freq = max(count.values())

    ans = min(num for num, freq in count.items() if freq == max_freq)

    return ans


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(most_frequent_even(nums))