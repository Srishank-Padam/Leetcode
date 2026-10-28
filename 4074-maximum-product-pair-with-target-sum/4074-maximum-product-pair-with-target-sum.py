class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        max_prod = float('-inf')
        pair = [-1, -1]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    if nums[i] > nums[j]:
                        prod = nums[i] * nums[j]

                        if prod > max_prod:
                            max_prod = prod
                            pair = [i, j]

        return pair
        # max_prod = float('-inf')
        # pair = [-1,-1]
        # seen = {}

        # for i, num in enumerate(nums):
        #     compl = target - num

        #     if compl in seen and num > compl:
        #         prod = compl * num

        #         if max_prod < prod:
        #             max_prod = prod
        #             pair = [i,seen[compl]]
                
        #     seen[num] = i
        
        # return pair
