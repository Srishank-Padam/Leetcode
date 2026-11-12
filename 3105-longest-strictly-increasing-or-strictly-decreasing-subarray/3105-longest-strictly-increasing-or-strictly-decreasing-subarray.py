class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_count = 1
        dec_count = 1
        max_count = 1

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc_count += 1
                dec_count = 1
                
            elif nums[i] < nums[i-1]:
                dec_count += 1
                inc_count = 1
            
            else:
                dec_count = inc_count = 1

            max_count = max(max_count, inc_count, dec_count)

        return max_count