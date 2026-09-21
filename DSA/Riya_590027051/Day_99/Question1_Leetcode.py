class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Put every number x at index x - 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first index where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If 1 to n are all present
        return n + 1