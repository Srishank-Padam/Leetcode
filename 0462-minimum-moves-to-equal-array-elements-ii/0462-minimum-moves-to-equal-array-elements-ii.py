class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        total = 0
        target = nums[len(nums) // 2]

        for i in nums:
            total += abs(i - target)

        return total