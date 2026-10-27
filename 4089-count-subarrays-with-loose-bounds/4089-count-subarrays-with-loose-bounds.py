class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        curr_count = 0
        total_subarr = 0

        for num in nums:
            if minK <= num <= maxK:
                curr_count += 1
                total_subarr += curr_count
            else:
                curr_count = 0
        return total_subarr