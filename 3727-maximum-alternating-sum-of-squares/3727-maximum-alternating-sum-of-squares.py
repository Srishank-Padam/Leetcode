class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # so even for negative numbers we can first sqr and next apply our sort condition
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i] 

        nums.sort()

        return - sum(nums[:n//2]) + sum(nums[n//2::])