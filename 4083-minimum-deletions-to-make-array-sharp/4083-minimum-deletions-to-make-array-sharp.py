class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        count = 0
        l, r = 0, 1
        while r < len(nums) and l < r:
            if nums[l] ^ nums[r] == 0:
                count += 1
                l += 1
                r += 1
            else:
                l += 1
                r += 1

        return count