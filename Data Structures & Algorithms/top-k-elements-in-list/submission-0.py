class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = [0] * k

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        top_k_keys = sorted(seen, key=seen.get, reverse=True)[:k]

        return top_k_keys

