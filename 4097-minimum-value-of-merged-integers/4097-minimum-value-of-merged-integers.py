class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        # arr = []
        # i, j = 0, 1

        # while j < len(nums):
        #     arr.append(int(str(nums[i]) + str(nums[j])))
        #     i += 2
        #     j += 2
        
        # return min(arr)
        ans = float('inf')

        for i in range(0, len(nums), 2):
            merged = int(str(nums[i]) + str(nums[i+1]))
            ans = min(ans, merged)

        return ans
