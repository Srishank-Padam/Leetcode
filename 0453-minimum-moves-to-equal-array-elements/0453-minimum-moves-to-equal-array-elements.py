class Solution:
    def minMoves(self, nums: list[int]) -> int:
        total = 0
        x = min(nums)
        for i in nums:
            total += (i - x)

        return total
