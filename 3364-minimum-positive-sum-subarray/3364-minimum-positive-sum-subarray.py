class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float("inf")

        for n in range(l,r+1):
            j = n
            i = 0
            cumsum = sum(nums[:j])
            if cumsum > 0:
                ans = min(cumsum, ans)

            while j < len(nums):
                cumsum = cumsum + nums[j] - nums[i]
                if cumsum > 0:
                    ans = min(cumsum, ans)
                j += 1
                i +=1
        
        return ans if ans != float('inf') else -1
