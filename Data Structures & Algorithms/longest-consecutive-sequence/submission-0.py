class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        longest = 1
        count = 1

        for index in range(1, len(sorted_nums)):
            if sorted_nums[index] == sorted_nums[index - 1]:
                continue

            if sorted_nums[index] == sorted_nums[index - 1] + 1:
                count += 1
            else:
                count = 1

            longest = max(longest, count)

        return longest
