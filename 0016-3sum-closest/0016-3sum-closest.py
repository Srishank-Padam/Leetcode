class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i, a in enumerate(nums):
    
            if i > 0 and nums[i-1] == a:
                continue

            l, r = i+1, len(nums) - 1

            while l < r:
                cumsum = a + nums[l] + nums[r]
                
                if cumsum == target:
                    return cumsum

                if abs(cumsum - target) < abs(closest_sum - target):
                    closest_sum = cumsum

                if cumsum > target:
                    r -= 1
                else:
                    l += 1

        return closest_sum
                
