class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        daHash = []
        for num in nums:
            if num in daHash:
                return num
            daHash.append(num)

        return 