class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        
        # return res

        smaller = 0
        equal = 0

        for num in nums:
            if num < target:
                smaller += 1
            if num == target:
                equal += 1
        
        return list(range(smaller, smaller + equal))