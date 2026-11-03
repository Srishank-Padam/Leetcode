class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        arr = sorted(zip(nums, cost))

        total = sum(cost)
        x = 0
        p = 0
        for num, c in arr:
            p += c
            if 2 * p >= total:
                x = num
                break
        
        ans  = 0
        for num, c in arr:
            ans += abs(num - x) * c
        
        return ans